import requests, bs4, os
from pathlib import Path

target_folder = r'C:\repos\python\automate_the_boring_stuff\chapter17\working_folder'
target_web_site = 'https://xkcd.com/'

web_site_response = requests.get(target_web_site)

soup = bs4.BeautifulSoup(web_site_response.text, 'lxml')

img_tag = soup.select('#comic > img')
img_src = 'http:' + img_tag[0].get('src')
img_basename = os.path.basename(img_src)

target_image_path = Path(target_folder) / img_basename

if target_image_path.exists():
    print('No new comic available')
else:
    print('New comic available')
    image_response = requests.get(img_src)

    image_file = open(target_image_path, 'wb')
    for chunk in image_response.iter_content(100000):
            image_file.write(chunk)
    image_file.close()
    print('New comic downloaded')
    