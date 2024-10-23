# Fix Lng/Lat Problem

## Description
This script processes all `.geojson` files located in the `Input_Files` folder. It fixes longitude and latitude values by applying a scaling factor to the coordinates of `MultiPolygon` geometries. The modified files are saved in the `Output_Files` folder with the prefix `fixed_`.

## Input
- Any `.geojson` files located in the `Input_Files` folder.

## Output
- Modified `.geojson` files saved in the `Output_Files` folder with the filename format `fixed_{OriginalFileName}.geojson`.

## Functionality
For each file, the script:
- Loads the GeoJSON file.
- Applies a scaling factor of 0.00001 to the `MultiPolygon` coordinates.
- Saves the modified data as a new file with the `fixed_` prefix.

## Requirements
The script requires Python 3.x and the following libraries:

### Installation

No additional installation is required for the libraries used in this script, as `os` and `json` are part of the Python standard library.

To ensure Python is installed, you can check with the following command:

```bash
python --version
```
If Python is not installed, you can download and install it from https://www.python.org/downloads/.

### Usage
1. Place all `.geojson` input files in the `Input_Files` folder.
2. Run the script.
3. The processed files will appear in the `Output_Files` folder with the `Output_` prefix.
