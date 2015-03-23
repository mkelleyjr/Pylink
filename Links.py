#Michel L. Kelley Jr.
#3/21/2015
#Links.py
#Print all links from a given website. 
#pip install BeautifulSoup4 beforehand if on Mac OSX 



import urllib2
import bs4
from bs4 import BeautifulSoup


html_page = urllib2.urlopen("http://www.msn.com")  #specify website here. MSN for example
soup = BeautifulSoup(html_page)
for link in soup.findAll('a'):
	link.prettify()
	print link.get('href')


