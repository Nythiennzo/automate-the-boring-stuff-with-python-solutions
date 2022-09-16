import requests, bs4, urllib.parse, os, shutil
from pathlib import Path

search_term = 'Thanos'
target_folder = r'C:\repos\python\automate_the_boring_stuff\chapter12\working_folder'


image_site_base_query = 'https://imgur.com/search?q='

search_folder_path = Path(target_folder) / search_term

if (search_folder_path).exists():
    shutil.rmtree(search_folder_path)
os.makedirs(search_folder_path)


response = requests.get(image_site_base_query + urllib.parse.quote(search_term))

soup = bs4.BeautifulSoup(response.text, 'lxml')

img_tags = soup.select('.image-list-link > img')

for img_tag in img_tags:
    image_url = 'https:' + img_tag.get('src')

    filename = os.path.basename(image_url)

    image_response = requests.get(image_url)

    image_file = open(search_folder_path / filename, 'wb')
    for chunk in image_response.iter_content(100000):
            image_file.write(chunk)
    image_file.close()


print('Done!')