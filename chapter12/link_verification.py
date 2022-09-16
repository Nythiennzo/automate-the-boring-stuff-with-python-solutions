import requests, bs4, os, shutil, sys
from pathlib import Path

url = 'https://inventwithpython.com'
target_folder = r'C:\repos\python\automate_the_boring_stuff\chapter12\working_folder'

try:
    response = requests.get(url)
    response.raise_for_status()

    soup = bs4.BeautifulSoup(response.text, 'lxml')
except:
    print('The url was not valid')


windows_uncompatible_characters = ('#', '<', '$', '+', '%', '>', '!', '`', '{', '?', '"', '=', '}', '/', ':', '\\', '@')

url_folder_name = os.path.basename(url)

for character in windows_uncompatible_characters:
    url_folder_name = url_folder_name.replace(character, '_')

url_folder_path = Path(target_folder) / url_folder_name

if (url_folder_path).exists():
    shutil.rmtree(url_folder_path)

os.makedirs(url_folder_path)

a_tags = soup.select('a')
links = {a_tag.get('href', '').rstrip('/') for a_tag in a_tags} 

for link in links:
    if link == '' or link.startswith('#'):
        continue 

    filename = os.path.basename(link)
    
    for character in windows_uncompatible_characters:
        filename = filename.replace(character, '_')
    
    print('Downloading ' + link + ' in folder: ' + filename)

    try:
        link_response = requests.get(link)
    except:
        print(link + ' is broken')
        continue

    link_file = open(url_folder_path / filename, 'wb')
    for chunk in link_response.iter_content(100000):
            link_file.write(chunk)
    link_file.close()

print('Done!')