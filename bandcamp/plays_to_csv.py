import os.path
import bs4
import json
from urllib.request import urlopen as u_req
from bs4 import BeautifulSoup
save_path = ''

def open_page(url):
    u_client = u_req(url)
    page_html = u_client.read()
    u_client.close()
    page = BeautifulSoup(page_html, "html.parser")
    return page


def open_file(file_name):
    name_of_file = file_name
    # add specifications for csv or text file via arg check if !(csv | txt) return nona
    complete_name = os.path.join(save_path, name_of_file + ".json")
    # line below probably better called in caller or add another arg
    file1 = open(complete_name, "a", encoding="utf-8")
    return file1

def to_csv(fn):
	with open(fn + '.json') as f:
		page = f.read()
		data = json.loads(page)
		# print(data['g']['breakout_data'])
	csv = open_file(fn + '.csv')
	breakout_data = data['g']['breakout_data']
	print(breakout_data)
	for month in data:
		print(month)
	# print(f)
	# parsed = json.loads(f)
	# print(parsed.keys)


to_csv('old_sol_plays')