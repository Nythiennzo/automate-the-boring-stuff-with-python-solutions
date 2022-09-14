import os, shutil
import pathlib
from pathlib import Path

source_folder = r'C:\repos\python\automate_the_boring_stuff'
file_extension = 'txt'
target_folder = r'C:\repos\python\automate_the_boring_stuff\chapter10\working_folder'


dot_file_extension = '.' + file_extension
target_folder_path = Path(target_folder)
for folder_name, subfolders, filenames in os.walk(Path(source_folder)):
    if Path(folder_name) == Path(target_folder):
        continue

    for filename in filenames:
        if not filename.endswith(dot_file_extension):
            continue

        clash_circumvention_part = ''
        filename_without_extention = filename[:-len(dot_file_extension)]

        while True:
            target_file_path = target_folder_path / (filename_without_extention + clash_circumvention_part + dot_file_extension)

            if not os.path.exists(target_file_path):
                shutil.copy(Path(folder_name) / filename, target_file_path)
                break
                
            clash_circumvention_part = '(' + str(int((clash_circumvention_part or '(0)')[1:-1]) + 1) + ')'

