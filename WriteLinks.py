#Michel L. Kelley Jr.
#3/21/2015
#WritesLinks.py
#Write all links from a given website to a file called Links.txt 
#pip install BeautifulSoup4 beforehand if on Mac OSX



import urllib2
import bs4
from bs4 import BeautifulSoup


html_page = urllib2.urlopen("http://www.msn.com")  #specify website here
soup = BeautifulSoup(html_page)


with open('Links.txt', 'w') as f:
	for link in soup.findAll('a'):
		f.write(link.get('href'))



