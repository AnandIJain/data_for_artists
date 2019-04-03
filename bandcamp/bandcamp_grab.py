import os.path
from bs4 import BeautifulSoup
import requests

from album_grab import album_grab

def bandcamp_grab(base_url, file_name):
    # grabs the titles and lengths of songs from a bandcamp
    # stores data in csv
    page = requests.get(base_url)
    page_bs = BeautifulSoup(page.content, 'html.parser')
    data = page_bs.find("div", class_="leftMiddleColumns").find_all("li")
    for li in data:
        incomplete_album_link = li.find('a', href=True)
        album_url = base_url + incomplete_album_link['href']
        print(album_url)
        album_grab(album_url, file_name)
