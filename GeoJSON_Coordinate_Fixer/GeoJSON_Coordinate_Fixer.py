import os
import json

# Convert the coordinates of polygons with a scaling factor
def convert_coordinates(coords):
    factor_x = 0.00001
    factor_y = 0.00001
    
    converted_coords = []
    for multipolygon in coords:
        new_multipolygon = []
        for polygon in multipolygon:
            new_polygon = []
            for point in polygon:
                new_point = [(point[0] * factor_x), (point[1] * factor_y)]
                new_polygon.append(new_point)
            new_multipolygon.append(new_polygon)
        converted_coords.append(new_multipolygon)
    return converted_coords

# Fix coordinates in GeoJSON file
def fix_geojson(input_file, output_file):
    # Load the input GeoJSON file
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Apply coordinate conversion to MultiPolygon features
    for feature in data['features']:
        if feature['geometry']['type'] == 'MultiPolygon':
            feature['geometry']['coordinates'] = convert_coordinates(feature['geometry']['coordinates'])
    
    # Save the modified GeoJSON to the output file
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# Process all GeoJSON files in the input folder
def process_directory(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    for filename in os.listdir(input_folder):
        if filename.endswith(".geojson"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, 'fixed_' + filename)
            fix_geojson(input_path, output_path)
            print(f"File '{filename}' has been successfully processed.\n")

# Define input and output folders
input_folder = 'Input_Files'
output_folder = 'Output_Files'

# Process the directory
process_directory(input_folder, output_folder)

# Final message after processing all files
print("All files have been successfully processed.")
