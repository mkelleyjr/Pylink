
# Michael L. Kelley Jr.
# March 3, 2018
# PrintLinks.py
# Print the links found within a given web page
# Updated for Python 3.6 
# Uses BeautifulSoup 4, lxml, requests, first do: 
# pip install bs4, pip install lxml, pip install requests


import requests
from bs4 import BeautifulSoup

# specifiy the page we want to grab HTML of 
page = requests.get("http://www.columbia.edu/~fdc/sample.html")

# parse the page 
soup = BeautifulSoup(page.content, "lxml")

# find all links on the page with 'a'

links = soup.find_all('a')

# print the links out 

print(links)
