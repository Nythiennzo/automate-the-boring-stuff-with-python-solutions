import os

root_folder = r'C://Program Files'
threshold = 2 ** 20 * 100

for folder_name, subforlder_names, filenames in os.walk(root_folder):
    for filename in filenames:
        file_absolute_path = folder_name + os.sep + filename
        if os.path.getsize(file_absolute_path) > threshold:
            print(file_absolute_path)