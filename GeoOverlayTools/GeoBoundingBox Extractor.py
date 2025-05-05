import json

with open   ("map.geojson", "r", encoding="utf-8") as f:
    data = json.load(f)

min_lon = float("inf")
min_lat = float("inf")
max_lon = float("-inf")
max_lat = float("-inf")

def process_coords(coords):
    global min_lon, min_lat, max_lon, max_lat
    for coord in coords:
        if isinstance(coord[0], list):
            process_coords(coord)
        else:
            lon, lat = coord
            min_lon = min(min_lon, lon)
            max_lon = max(max_lon, lon)
            min_lat = min(min_lat, lat)
            max_lat = max(max_lat, lat)

for feature in data["features"]:
    geom = feature["geometry"]
    if geom["type"] == "Polygon":
        process_coords(geom["coordinates"])
    elif geom["type"] == "MultiPolygon":
        for polygon in geom["coordinates"]:
            process_coords(polygon)

print("Bounding box for CustomSources.tsx:\n")
print(f"Top-left:     [{min_lon}, {max_lat}]")
print(f"Top-right:    [{max_lon}, {max_lat}]")
print(f"Bottom-right: [{max_lon}, {min_lat}]")
print(f"Bottom-left:  [{min_lon}, {min_lat}]")

print("\nPaste this in your CustomSources.tsx:\n")
print(f"""coordinates={[
    [{min_lon}, {max_lat}],
    [{max_lon}, {max_lat}],
    [{max_lon}, {min_lat}],
    [{min_lon}, {min_lat}],
]}""")