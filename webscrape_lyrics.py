#- * -coding: utf - 8 - * -

from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import urllib.error
import ssl
import json
import ast
import os
from urllib.request import Request, urlopen

# ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# prompts user input for individual song URL
url = input('Enter Genius Song Lyrics Url: ')

# make scrape request appear as browser
req = Request(url, headers = {'User-Agent' : 'Mozilla/5.0'})
webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')
html = soup.prettify('utf-8')
song_json = {}
song_json['Lyrics'] = []
# song_json['Comments'] = []

# extract title of the song
for title in soup.findAll('title'):
    song_json['Title'] = title.text.strip()

# extract the release date of the song
# uncomment to scrape song metadata
# for span in soup.findAll('span', attrs = {'class':
#     'metadata_unit-info metadata_unit-info--text_only'}):
#         song_json['Release date'] = span.text.strip()

# extract the commments on the song
# uncomment to scrape song comments
# for div in soup.findAll('div', attrs = {'class':
#     'rich_text_formatting'}):
#         comments = div.text.strip().split('\n')
#         for comment in comments:
#             if comment != '':
#                 song_json['Comments'].append(comment)

# extract the lyrics of the song
for div in soup.findAll('div', attrs = {'class': 'lyrics'}):
    song_json['Lyrics'].append(div.text.strip().split('\n'))

# save the json created with the file name as title + .json
with open(song_json['Title'] + '.json', 'w') as outfile:
    json.dump(song_json, outfile, indent=4, ensure_ascii=False)

# save html content into html file with name as title + .html
# with open(song_json['Title'] + '.html', 'wb') as file:
#     file.write(html)

print('-------extraction of data complete - check json file ------')