import json
import re
import requests
from bs4 import BeautifulSoup

conn = psycopg2.connect(database="kazami", user="kazami", password="dj4xji4", host="127.0.0.1", port="5432")

cur = conn.cursor()

res = requests.get('http://rent.591.com.tw/index.php?module=search&action=rslist&is_new_list1&type=1&searchtype=1&region=1&orderType=desc')

soup = BeautifulSoup(res.text, "html.parser")

