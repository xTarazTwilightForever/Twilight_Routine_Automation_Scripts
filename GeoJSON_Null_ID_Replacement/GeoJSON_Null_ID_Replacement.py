import os
import json
import random

# Function to replace null 'id' properties in GeoJSON features
def replace_null_id(input_file, output_file):
    # Load the input file
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Process each feature and replace null 'id' values
    for feature in data['features']:
        if feature['properties'].get('id') is None:
            feature['properties']['id'] = random.randint(1000, 9999)

    # Save the modified data to the output file
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# Directories
input_folder = 'Input_Files'
output_folder = 'Output_Files'

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Process all GeoJSON files in the Input_Files directory
for filename in os.listdir(input_folder):
    if filename.endswith('.geojson'):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, f'Output_{filename}')
        replace_null_id(input_path, output_path)

        # Print success message for each processed file
        print(f"File '{filename}' has been successfully processed.\n")

# Final message after processing all files
print("All files have been successfully processed.")
