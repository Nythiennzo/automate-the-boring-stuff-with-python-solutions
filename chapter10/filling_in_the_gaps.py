import sys
from pathlib import Path
import shutil

prefix = 'content'
folder = r'C:\repos\python\automate_the_boring_stuff\chapter10\working_folder'

folder_path = Path(folder)
files_with_prefix = list(folder_path.glob(prefix + '*'))

if len(files_with_prefix) == 0:
    print('The folder does not contain any files')
    sys.exit()

if len({file_with_prefix.suffix for file_with_prefix in files_with_prefix}) != 1:
    print('The folder contains more that one type of file')
    sys.exit()

new_name_mapping = []
number_part_max_length = 0

for index, file_with_prefix in enumerate(files_with_prefix):
    target_file_number = index + 1
    numbered_part = file_with_prefix.stem[len(prefix):]

    if  not numbered_part.isdigit(): 
        print('The folder contains non numbered files')
        sys.exit()

    new_name_mapping.append((file_with_prefix, target_file_number))

    number_part_max_length = max([number_part_max_length, len(numbered_part)])
    


for old_filename, target_file_number in new_name_mapping:
    new_filename = prefix + str(target_file_number).rjust(number_part_max_length, '0') + old_filename.suffix
    print(new_filename)
    shutil.move(folder_path / old_filename, folder_path / new_filename)
