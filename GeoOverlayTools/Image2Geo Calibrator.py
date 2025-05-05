import json
import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
from PIL import Image
from pathlib import Path
import numpy as np
import pyperclip

class OverlayEditor:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()
        self.image_path = filedialog.askopenfilename(title="Select image", filetypes=[("PNG files", "*.png")])
        if not self.image_path:
            print("No image selected.")
            return
        self.image = np.array(Image.open(self.image_path))
        self.image_name = Path(self.image_path).stem
        self.geojson_path = filedialog.askopenfilename(title="Select GeoJSON", filetypes=[("GeoJSON files", "*.geojson")])
        if not self.geojson_path:
            print("No GeoJSON selected.")
            return
        self.geojson = json.load(open(self.geojson_path, encoding="utf-8"))
        self.set_initial_coordinates()

    def set_initial_coordinates(self):
        print("\nEnter coordinates one by one in the format: x, y or [x, y],")
        self.coords = []
        labels = ["Top-left", "Top-right", "Bottom-right", "Bottom-left"]
        for label in labels:
            raw = input(f"{label}: ")
            try:
                cleaned = raw.replace("[", "").replace("]", "").replace(",", " ").split()
                x, y = map(float, cleaned[:2])
                self.coords.append([x, y])
            except Exception as e:
                print("Invalid input:", e)
                return

        self.tx = 0
        self.ty = 0
        self.sx = 1
        self.sy = 1
        self.move_step = 0.00001

        self.fig, self.ax = plt.subplots()
        self.fig.canvas.manager.set_window_title("Image Position Editor")
        self.fig.subplots_adjust(bottom=0.45)
        self.img_obj = None
        self.sliders = {}

        self.draw_geojson()
        self.draw_overlay()
        self.add_widgets()
        self.fig.canvas.mpl_connect("key_press_event", self.on_key)
        self.fig.canvas.mpl_connect("key_press_event", self.key_combo_handler)
        plt.show()

    def draw_geojson(self):
        for feature in self.geojson["features"]:
            geometry = feature["geometry"]
            if geometry["type"] == "Polygon":
                for polygon in [geometry["coordinates"]]:
                    for ring in polygon:
                        xs, ys = zip(*ring)
                        self.ax.plot(xs, ys, linewidth=0.8, color="cyan")
            elif geometry["type"] == "MultiPolygon":
                for polygon in geometry["coordinates"]:
                    for ring in polygon:
                        xs, ys = zip(*ring)
                        self.ax.plot(xs, ys, linewidth=0.8, color="cyan")

    def draw_overlay(self):
        if self.img_obj:
            self.img_obj.remove()
        width = self.coords[1][0] - self.coords[0][0]
        height = self.coords[0][1] - self.coords[3][1]
        left = self.coords[0][0] + self.tx
        top = self.coords[0][1] + self.ty
        extent = [
            left,
            left + width * self.sx,
            top - height * self.sy,
            top,
        ]
        self.img_obj = self.ax.imshow(self.image, extent=extent, zorder=1, alpha=0.5)
        self.ax.set_xlim(-0.001, 0.009)
        self.ax.set_ylim(-0.014, 0.001)
        self.fig.canvas.draw_idle()

    def add_widgets(self):
        axcolor = "lightgrey"
        params = [
            ("Move X", 0.29, -0.01, 0.01, self.tx),
            ("Move Y", 0.24, -0.01, 0.01, self.ty),
            ("Scale X", 0.19, 0.1, 3.0, self.sx),
            ("Scale Y", 0.14, 0.1, 3.0, self.sy),
            ("Move Step", 0.09, 0.000001, 0.001, self.move_step),
        ]
        for label, y, valmin, valmax, valinit in params:
            ax_slider = plt.axes([0.25, y, 0.65, 0.035], facecolor=axcolor)
            slider = Slider(ax_slider, label, valmin, valmax, valinit=valinit)
            slider.on_changed(self.update_from_sliders)
            self.sliders[label] = slider

        save_ax = plt.axes([0.25, 0.02, 0.12, 0.045])
        save_button = Button(save_ax, "Save")
        save_button.on_clicked(self.save_coordinates)

    def update_from_sliders(self, val):
        self.tx = self.sliders["Move X"].val
        self.ty = self.sliders["Move Y"].val
        self.sx = self.sliders["Scale X"].val
        self.sy = self.sliders["Scale Y"].val
        self.move_step = self.sliders["Move Step"].val
        self.draw_overlay()

    def on_key(self, event):
        if event.key == "left":
            self.sliders["Move X"].set_val(self.tx - self.move_step)
        elif event.key == "right":
            self.sliders["Move X"].set_val(self.tx + self.move_step)
        elif event.key == "up":
            self.sliders["Move Y"].set_val(self.ty + self.move_step)
        elif event.key == "down":
            self.sliders["Move Y"].set_val(self.ty - self.move_step)

    def key_combo_handler(self, event):
        if event.key == "S":  # Shift + S
            self.save_coordinates(None)

    def save_coordinates(self, event):
        if len(self.coords) != 4:
            print("Invalid number of coordinates.")
            return

        width = self.coords[1][0] - self.coords[0][0]
        height = self.coords[0][1] - self.coords[3][1]
        left = self.coords[0][0] + self.tx
        top = self.coords[0][1] + self.ty
        right = left + width * self.sx
        bottom = top - height * self.sy
        result = [
            [left, top],
            [right, top],
            [right, bottom],
            [left, bottom],
        ]
        lines = ["    [" + f"{x:.15f}, {y:.15f}" + "]," for x, y in result]
        final = "\n".join(lines)
        pyperclip.copy(final)

        base_name = self.image_name
        filename = base_name + ".txt"
        while Path(filename).exists():
            base_name = "T" + base_name
            filename = base_name + ".txt"

        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(final + "\n")
            print(f"Saved to: {filename}")
        except Exception as e:
            print("Error saving file:", e)

OverlayEditor()
