# GeoJSON Null ID Replacement

## Description
This script processes all `.geojson` files located in the `Input_Files` folder. It checks each feature for a `null` value in the `id` property, and replaces any `null` values with a randomly generated ID between 1000 and 9999. The modified files are saved in the `Output_Files` folder.

## Input
- Any `.geojson` files located in the `Input_Files` folder.

## Output
- Modified `.geojson` files saved in the `Output_Files` folder with the filename format `Output_{OriginalFileName}.geojson`.

## Functionality
For each file, the script:
- Loads the GeoJSON file.
- Searches for features with a `null` value in the `id` property.
- Replaces the `null` `id` values with random integers between 1000 and 9999.
- Saves the modified data as a new file with the `Output_` prefix.

## Requirements
The script requires Python 3.x and the following libraries:

### Installation

No additional installation is required for the libraries used in this script, as `os`, `json`, and `random` are part of the Python standard library.

To ensure Python is installed, you can check with the following command:

```bash
python --version
```
If Python is not installed, you can download and install it from https://www.python.org/downloads/.

### Usage
1. Place all `.geojson` input files in the `Input_Files` folder.
2. Run the script.
3. The processed files will appear in the `Output_Files` folder with the `Output_` prefix.
