import os.path
from bs4 import BeautifulSoup
import requests
import codecs

def song_grab(url_to_grab, file_name, track_num):
    page = requests.get(url_to_grab)
    page_bs = BeautifulSoup(page.content, 'html.parser')
    file = codecs.open(file_name, "a+", "utf-8")

    song_name = page_bs.find("h2", {"class": "trackTitle"}).text.strip()
    abt_divfind = page_bs.find("div", {"class": "tralbumData tralbum-about"})
    if abt_divfind is not None:
        abt_text = abt_divfind.text
        abt = ' '.join(abt_text.split())
    else:
        abt = ""
    track_creds = page_bs.find("div", {"class": "tralbumData tralbum-credits"})
    if track_creds is not None:
        creds_text = track_creds.text
        creds2 = ' '.join(creds_text.split())
        creds = creds2.split(",")[2]
    song_duration = page_bs.find("meta", {"itemprop": "duration"})['content']
    write_string = str(track_num) + ", " + song_name + ", " + song_duration + ", " + abt + ", " + creds + "\n"
    # is it better to do one write all at once, maybe dont want 'abt' to add a new line for example
    file.write(write_string)
    file.close()

