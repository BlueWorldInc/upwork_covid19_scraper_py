class Country:
	def __init__(self, countryRank =  None, countryName = None, totalCases = None, newCases = None, totalDeaths = None, newDeaths = None, totalRecovered = None, newRecovered= None, activeCases = None, seriousCritical = None, totCases1Mpop = None, deaths1Mpop = None, totalTests = None, tests1Mpop = None, population = None):
		self.countryRank = countryRank
		self.countryName = countryName
		self.totalCases = totalCases
		self.newCases = newCases
		self.totalDeaths = totalDeaths
		self.newDeaths = newDeaths
		self.totalRecovered = totalRecovered
		self.newRecovered = newRecovered
		self.activeCases = activeCases
		self.seriousCritical = seriousCritical
		self.totCases1Mpop = totCases1Mpop
		self.deaths1Mpop = deaths1Mpop
		self.totalTests = totalTests
		self.tests1Mpop = tests1Mpop
		self.population = population

	def to_string(self):
		print(
			self.countryRank,
			self.countryName,
			self.totalCases,
			self.newCases,
			self.totalDeaths,
			self.newDeaths,
			self.totalRecovered,
			self.newRecovered,
			self.activeCases,
			self.seriousCritical,
			self.totCases1Mpop,
			self.deaths1Mpop,
			self.totalTests,
			self.tests1Mpop,
			self.population)

	def to_csv(self, filepath, separator):
		f = open(filepath, "a", encoding="utf-8")
		separator = separator
		newline = "\n"
		csv_line = (str(self.countryRank) + separator
					+ str(self.countryName) + separator
					+ str(self.totalCases) + separator
					+ str(self.newCases) + separator
					+ str(self.totalDeaths) + separator
					+ str(self.newDeaths) + separator
					+ str(self.totalRecovered) + separator
					+ str(self.newRecovered) + separator
					+ str(self.activeCases) + separator
					+ str(self.seriousCritical) + separator
					+ str(self.totCases1Mpop) + separator
					+ str(self.deaths1Mpop) + separator
					+ str(self.totalTests) + separator
					+ str(self.tests1Mpop) + separator
					+ str(self.population) + newline)
		f.write(csv_line)
		f.close()


from bs4 import BeautifulSoup
import urllib.request

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

# soup = soup.find_all("tr", {'style': [None]}, limit=6)

# soup = soup.find_all("tr", {'style': [""]})
# soup.find_all("tr", {'style': [""]})

# def total_row_world_class_only(css_class):
    # return css_class is not None and css_class == 'total_row_world'



# soup = soup.find_all("tr", class_="total_row_world")

# first_row_index = 0

# for s in soup:
# 	first_row_index += 1
# 	if (s.has_attr('class')) and len(s['class']) == 1 and s['class'][0] == "total_row_world":
# 		print(s['class'][0])
# 		break

# print(first_row_index)

# soup = soup.find_all("table")[0]
# soup = soup.find_all("tr")

main_table_countries_today = soup.find_all("table")[0].find_all("tr")
main_table_countries_yesterday = soup.find_all("table")[1].find_all("tr")
main_table_countries_yesterday2 = soup.find_all("table")[2].find_all("tr")

list_countries_today = []
list_countries_yesterday = []
list_countries_yesterday2 = []

for s in main_table_countries_today:
	if (s.has_attr("style")) and not (s.has_attr("class")):
		c = Country()
		f = s.find_all("td")
		if len(f[0].contents) > 0: c.countryRank = f[0].contents[0].string
		if len(f[1].contents) > 0: c.countryName = f[1].contents[0].string
		if len(f[2].contents) > 0: c.totalCases = f[2].contents[0].string
		if len(f[3].contents) > 0: c.newCases = f[3].contents[0].string
		if len(f[4].contents) > 0: c.totalDeaths = f[4].contents[0].string.strip()
		if len(f[5].contents) > 0: c.newDeaths = f[5].contents[0].string
		if len(f[6].contents) > 0: c.totalRecovered = f[6].contents[0].string
		if len(f[7].contents) > 0: c.newRecovered = f[7].contents[0].string
		if len(f[8].contents) > 0: c.activeCases = f[8].contents[0].string
		if len(f[9].contents) > 0: c.seriousCritical = f[9].contents[0].string
		if len(f[10].contents) > 0: c.totCases1Mpop = f[10].contents[0].string
		if len(f[11].contents) > 0: c.deaths1Mpop = f[11].contents[0].string
		if len(f[12].contents) > 0: c.totalTests = f[12].contents[0].string
		if len(f[13].contents) > 0: c.tests1Mpop = f[13].contents[0].string
		if len(f[14].contents) > 0: c.population = f[14].contents[0].string
		list_countries_today.append(c)

for s in main_table_countries_yesterday:
	if (s.has_attr("style")) and not (s.has_attr("class")):
		c = Country()
		f = s.find_all("td")
		if len(f[0].contents) > 0: c.countryRank = f[0].contents[0].string
		if len(f[1].contents) > 0: c.countryName = f[1].contents[0].string
		if len(f[2].contents) > 0: c.totalCases = f[2].contents[0].string
		if len(f[3].contents) > 0: c.newCases = f[3].contents[0].string
		if len(f[4].contents) > 0: c.totalDeaths = f[4].contents[0].string.strip()
		if len(f[5].contents) > 0: c.newDeaths = f[5].contents[0].string
		if len(f[6].contents) > 0: c.totalRecovered = f[6].contents[0].string
		if len(f[7].contents) > 0: c.newRecovered = f[7].contents[0].string
		if len(f[8].contents) > 0: c.activeCases = f[8].contents[0].string
		if len(f[9].contents) > 0: c.seriousCritical = f[9].contents[0].string
		if len(f[10].contents) > 0: c.totCases1Mpop = f[10].contents[0].string
		if len(f[11].contents) > 0: c.deaths1Mpop = f[11].contents[0].string
		if len(f[12].contents) > 0: c.totalTests = f[12].contents[0].string
		if len(f[13].contents) > 0: c.tests1Mpop = f[13].contents[0].string
		if len(f[14].contents) > 0: c.population = f[14].contents[0].string
		list_countries_yesterday.append(c)

for s in main_table_countries_yesterday2:
	if (s.has_attr("style")) and not (s.has_attr("class")):
		c = Country()
		f = s.find_all("td")
		if len(f[0].contents) > 0: c.countryRank = f[0].contents[0].string
		if len(f[1].contents) > 0: c.countryName = f[1].contents[0].string
		if len(f[2].contents) > 0: c.totalCases = f[2].contents[0].string
		if len(f[3].contents) > 0: c.newCases = f[3].contents[0].string
		if len(f[4].contents) > 0: c.totalDeaths = f[4].contents[0].string.strip()
		if len(f[5].contents) > 0: c.newDeaths = f[5].contents[0].string
		if len(f[6].contents) > 0: c.totalRecovered = f[6].contents[0].string
		if len(f[7].contents) > 0: c.newRecovered = f[7].contents[0].string
		if len(f[8].contents) > 0: c.activeCases = f[8].contents[0].string
		if len(f[9].contents) > 0: c.seriousCritical = f[9].contents[0].string
		if len(f[10].contents) > 0: c.totCases1Mpop = f[10].contents[0].string
		if len(f[11].contents) > 0: c.deaths1Mpop = f[11].contents[0].string
		if len(f[12].contents) > 0: c.totalTests = f[12].contents[0].string
		if len(f[13].contents) > 0: c.tests1Mpop = f[13].contents[0].string
		if len(f[14].contents) > 0: c.population = f[14].contents[0].string
		list_countries_yesterday2.append(c)

# for c in list_countries_today:
	# c.to_string()

# for c in list_countries_today:
	# c.to_string()
# for c in list_countries_yesterday:
	# c.to_string()
# for c in list_countries_yesterday2:
	# c.to_string()

for c in list_countries_yesterday2:
	c.to_csv("../csv_data/coronavirus_data.csv", ";")

# c = list_countries_today[0]

# f = open("../csv_data/coronavirus_data.csv", "w")
# separator = " "
# csv_line = c.countryRank + separator + c.countryName
# f.write(csv_line)
# f.close()














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
