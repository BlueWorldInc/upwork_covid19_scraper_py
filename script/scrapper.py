html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

class Country:
	def __init__(self, countryName = None, totalCases = None, totalDeaths = None, newDeaths = None, totalRecovered = None, activeCases = None, seriousCritical = None, totCases1Mpop = None, deaths1Mpop = None, totalTests = None, tests1Mpop = None, population = None):
		self.countryName = countryName
		self.totalCases = totalCases
		self.totalDeaths = totalDeaths
		self.newDeaths = newDeaths
		self.totalRecovered = totalRecovered
		self.activeCases = activeCases
		self.seriousCritical = seriousCritical
		self.totCases1Mpop = totCases1Mpop
		self.deaths1Mpop = deaths1Mpop
		self.totalTests = totalTests
		self.tests1Mpop = tests1Mpop
		self.population = population

from bs4 import BeautifulSoup
import urllib.request

soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup.title.string)


# headers = {}
# headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"

# req = urllib.request.Request('https://www.worldometers.info/coronavirus/#countries', headers = headers)
# x = urllib.request.urlopen(req)
# # print(x.read())

file_name = "../csv_data/coronavirus_data.txt"
# f = open(file_name, "w", encoding="utf-8")
# f.write(x.read().decode('utf-8'))
# f.close()

def tr_with_void_style(tag):
    return tag.tr and tag.has_attr('style')

s = open(file_name, "r", encoding="utf-8")
soup = BeautifulSoup(s, 'html.parser')
# print(soup.find_all(tr_with_void_style)[2])
# print(soup.find("tr", style=''))
soup = soup.find_all("table")[0]
# soup = soup.find_all("tr", {'style': [None]}, limit=6)

soup = soup.find_all("tr", {'style': [""]}, limit=1)

# c = Country(totalCases = 500)
c = Country("USA")
c.activeCases = 100

print(c.activeCases)
print(c.countryName)


# print(soup.tr)



# print("hello world")


# def hello():
# 	print("hello")

# hello()