import bs4
import pandas as pd
import requests as r
import re
import traceback
import numpy as np

df = pd.read_csv('billie_lyrcs.csv')

url = 'https://genius.com/artists/Billy-joel'