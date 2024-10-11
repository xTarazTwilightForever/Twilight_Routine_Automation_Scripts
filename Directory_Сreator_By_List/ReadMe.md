# Directory Creator By List

## Description
This script processes all `.txt` files located in the `Input_Files` folder. It reads sections and lessons from each file, creates directories for sections, and generates `.md` files for both the sections and the lessons. The generated files are saved in the `Output_Files` folder.

## Input
- Any `.txt` files located in the `Input_Files` folder that follow the format:
  - Sections without indentation (e.g., **"Introduction to CSS"**).
  - Lessons with indentation or starting with a number (e.g., **"1. Cascading Style Sheets"**).

## Output
- A directory structure that mirrors the sections and lessons in the `.txt` file.
  - Each section gets its own directory, and within each directory, `.md` files are created for the lessons.
  - The root folder contains a `.md` file for each section and a main `.md` file for the course.

## Functionality
For each `.txt` file, the script:
- Reads sections and lessons.
- Creates directories for each section.
- Generates `.md` files for both sections and lessons, placing the lesson files inside the section directories.
- The structure reflects the content of the `.txt` files.

## Requirements
The script requires Python 3.x and does not use any external libraries beyond the standard library.

### Installation
No additional installation is required for this script, as `os` is part of the Python standard library.

To ensure Python is installed, you can check with the following command:

```bash
python --version
```

If Python is not installed, you can download and install it from the official [Python website](https://www.python.org/downloads/).

Usage
1. Place all .txt input files in the Input_Files folder.
2. Run the script:

```bash
python Directory_Creator_By_List.py
```

The generated files and directories will appear in the Output_Files folder, reflecting the structure of the input files.
