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

# soup = soup.find_all("tr", {'style': [""]})
soup = soup.find_all("tr")
# soup.find_all("tr", {'style': [""]})

# def total_row_world_class_only(css_class):
    # return css_class is not None and css_class == 'total_row_world'



# soup = soup.find_all("tr", class_="total_row_world")

first_row_index = 0

# for s in soup:
# 	first_row_index += 1
# 	if (s.has_attr('class')) and len(s['class']) == 1 and s['class'][0] == "total_row_world":
# 		print(s['class'][0])
# 		break

# print(first_row_index)

for s in soup:
	if (s.has_attr("style")) and not (s.has_attr("class")):
		f = s.find_all("td")
		# if (len(f)) > 0 and s['style'] == "":
		countryRank = f[0].string
		countryName = f[1].string
		totalCases = f[2].string
		totalDeaths = f[3].string
		newDeaths = f[4].string
		totalRecovered = f[5].string
		activeCases = f[6].string
		seriousCritical = f[7].string
		totCases1Mpop = f[8].string
		deaths1Mpop = f[9].string
		totalTests = f[10].string
		tests1Mpop = f[11].string
		population = f[12].string
		print(countryRank)
		# print(s['style'])

# print(len(soup))

# for s in soup:
	# print(s.has_attr('style'))

# for a in soup:
	# print(a.find_all("td")[0].string)

# countryRank = soup.find_all("td")[0].string
# countryName = soup.find_all("td")[1].string
# totalCases = soup.find_all("td")[2].string
# totalDeaths = soup.find_all("td")[3].string
# newDeaths = soup.find_all("td")[4].string
# totalRecovered = soup.find_all("td")[5].string
# activeCases = soup.find_all("td")[6].string
# seriousCritical = soup.find_all("td")[7].string
# totCases1Mpop = soup.find_all("td")[8].string
# deaths1Mpop = soup.find_all("td")[9].string
# totalTests = soup.find_all("td")[10].string
# tests1Mpop = soup.find_all("td")[11].string
# population = soup.find_all("td")[12].string

# print(countryRank, end="    ")
# print(countryName, end="    ")
# print(totalCases, end="    ")
# print(totalDeaths, end="    ")
# print(newDeaths, end="    ")
# print(totalRecovered, end="    ")
# print(activeCases, end="    ")
# print(seriousCritical, end="    ")
# print(totCases1Mpop, end="    ")
# print(deaths1Mpop, end="    ")
# print(totalTests, end="    ")
# print(tests1Mpop, end="    ")
# print(population)

# print(soup)

# c = Country(totalCases = 500)
# c = Country("USA")
# c.activeCases = 100

# print(c.activeCases)
# print(c.countryName)


# print(soup.tr)



# print("hello world")


# def hello():
# 	print("hello")

# hello()