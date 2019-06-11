import requests
import urllib.requests
import time
from bs4 import BeautifulSoup

url = 'https://cleartax.in/s/gst-law-goods-and-services-tax'
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
soup.findAll('a')

