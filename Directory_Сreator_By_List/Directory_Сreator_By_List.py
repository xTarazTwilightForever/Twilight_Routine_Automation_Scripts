import os

# Paths for input and output
input_dir = 'Input_Files'
output_dir = 'Output_Files'

# Templates for the different .md files
course_template = """---
tags:
  - Курсы
author: 
начал проходить: 
Статус: 
создал заметку: 
Заданий: ""
кол.заметок: ""
моя оценка:
---
### Резюме

"""

section_template = """---
tags:
  - 
---
### Резюме

"""

lesson_template = """---
tags:
  - Course_Completed_Task_Code_Basics_HTML
---
### Резюме

```



```

"""

# Function to read and parse the input file
def parse_input_file(file_path):
    structure = {}
    current_section = None
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:  # Skip empty lines
                continue
            if not line.startswith('\t') and not line[0].isdigit():  # Section
                current_section = line
                structure[current_section] = []
            elif line.startswith('\t') or line[0].isdigit():  # Lesson
                lesson = line.strip() + ".md"  # Keep the lesson number in the name
                structure[current_section].append(lesson)
    return structure

# Function to create directories and .md files based on parsed data
def create_directories_and_files(course_name, file_structure):
    course_output_path = os.path.join(output_dir, course_name)
    
    # Create the main course directory
    if not os.path.exists(course_output_path):
        os.makedirs(course_output_path)
    
    # Create the main course .md file
    with open(os.path.join(course_output_path, f"{course_name}.md"), 'w', encoding='utf-8') as f:
        f.write(course_template)
    
    # Create the section .md files and lessons
    for section, lessons in file_structure.items():
        section_dir = os.path.join(course_output_path, section)
        
        # Create section .md file
        with open(os.path.join(course_output_path, f"{section}.md"), 'w', encoding='utf-8') as f:
            f.write(section_template)
        
        # Create directory for each section
        if not os.path.exists(section_dir):
            os.makedirs(section_dir)
        
        # Create lesson .md files in the section
        for lesson in lessons:
            with open(os.path.join(section_dir, lesson), 'w', encoding='utf-8') as f:
                f.write(lesson_template)

# Process all .txt files in the input directory
for file_name in os.listdir(input_dir):
    if file_name.endswith('.txt'):
        course_name = os.path.splitext(file_name)[0]
        file_path = os.path.join(input_dir, file_name)
        file_structure = parse_input_file(file_path)
        create_directories_and_files(course_name, file_structure)

print("All directories and files have been created successfully.")
