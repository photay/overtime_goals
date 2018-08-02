# import libraries
import urllib2
from urllib import urlopen
from bs4 import BeautifulSoup

url_2018 = "https://www.google.com/search?ei=QDphW_yCPauUjwSJv6bQBg&q=world+cup+2018&oq=world+cup+2018&gs_l=psy-ab.3..0i67k1l4j0l2j0i67k1j0j0i20i264k1j0.1652504.1656710.0.1657009.16.15.1.0.0.0.143.1412.11j4.15.0....0...1.1.64.psy-ab..0.16.1414...35i39k1j0i131k1j0i20i263k1j0i10i67k1j0i10k1.0.1Id8GeA3t98#sie=lg;/m/06qjc4;2;/m/030q7;mt;fp;1"
# url_2018 = "https://www.fifa.com/worldcup/matches/match/300331503/#match-liveblog"
try:
    # page = urllib2.urlopen(url_2018)
    page = urlopen(url_2018)
except Exception as e:
    print(e);
soup = BeautifulSoup(page, 'html.parser')
print soup
# name_box = soup.find('h1', attr={'class':'name'})
# name = name_box.text.strip() # strip() is used to remove starting and trailing
# print name
