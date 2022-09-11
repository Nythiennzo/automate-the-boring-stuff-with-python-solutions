import re
from pathlib import Path

folder_path = r'C:/repos/python/automate_the_boring_stuff/chapter9/folder_of_files'

re_search_string = input('Regular Expression to search: ')
re_search = re.compile(re_search_string)

for txt_file in Path(folder_path).glob('*.txt'):
    if re_search.search(open(txt_file).read()) != None:
        print(txt_file)