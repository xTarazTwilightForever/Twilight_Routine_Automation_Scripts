# GeoOverlayTools

## Description
This folder contains two Python scripts designed to assist in aligning raster overlays with geographic data and extracting bounding box coordinates from GeoJSON files. These tools are intended to streamline the workflow for developers working with map overlays, such as in `CustomSources.tsx`.

## Included Scripts

### 1. `GeoOverlayEditor.py`

A graphical utility that lets you visually align a `.png` overlay onto a map using reference coordinates.

#### Features
- Load `.png` and `.geojson` files interactively.
- Input initial coordinates manually (top-left, top-right, bottom-right, bottom-left).
- Adjust overlay position and scale using sliders or keyboard arrows.
- Save adjusted coordinates to clipboard and `.txt` file.

### 2. `GeoBoundingBoxExtractor.py`

A script that calculates the bounding box (min/max latitude and longitude) of any `.geojson` file.

#### Features
- Extracts top-left, top-right, bottom-right, and bottom-left coordinates.
- Prints ready-to-paste block for `coordinates=[...]` in `CustomSources.tsx`.

## Input
- A `.png` file (for the overlay editor).
- A `.geojson` file (for both scripts).

## Output
- A `.txt` file with `[x, y]` overlay coordinates.
- Printed bounding box coordinates for code use.

## Requirements

- Python 3.x
- Required libraries:
  - `json` (standard)
  - `tkinter` (standard)
  - `matplotlib`
  - `PIL` (`Pillow`)
  - `numpy`
  - `pyperclip`
  - `pathlib` (standard)

### Installation
Install required libraries (if not already installed):

```bash
pip install matplotlib pillow numpy pyperclip
```

### Usage

#### GeoOverlayEditor.py
- Run the script.
- Select a `.png` image and a `.geojson` file.
- Enter initial corner coordinates.
- Adjust position and scale using sliders or arrow keys.
- Press the "Save" button or `Shift+S` to copy/save final coordinates.

#### GeoBoundingBoxExtractor.py
- Place your `.geojson` file in the same folder.
- Run the script.
- Copy the bounding box block for use in frontend code.
