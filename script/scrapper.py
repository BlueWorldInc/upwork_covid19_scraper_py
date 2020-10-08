class Country:
	def __init__(self, column_header_list):
		self.headersDict = {}
		for header in column_header_list:
			self.headersDict[header] = None

	def to_string(self):
		s = ""
		for header in self.headersDict:
			s += self.headersDict[header] + ";"
		return s

	def print_content(self):
		print(self.to_string())

	def to_csv(self, filepath, separator):
		f = open(filepath, "a", encoding="utf-8")
		separator = separator
		csv_line = ""
		for header in self.headersDict:
			csv_line += str(self.headersDict[header]) + separator
		csv_line = csv_line[:-1] + "\n"
		f.write(csv_line)
		f.close()

class CountriesHandler:
	def __init__(self, soup = None):
		self.soup = soup
		self.list_countries_all = [[], [], []]
		self.list_world_total_all = []
		self.column_header_list =  ["countryRank", "countryName", "totalCases", "newCases", "totalDeaths", "newDeaths",  \
									"totalRecovered", "newRecovered", "activeCases", "seriousCritical", "totCases1Mpop", \
									"deaths1Mpop", "totalTests", "tests1Mpop", "population"]
		
	def createCountries(self):
		for i in range(3):
			main_table_countries = self.soup.find_all("table")[i].find_all("tr")
			for tr in main_table_countries:
				if (tr.has_attr("style")) and not (tr.has_attr("class")):
					c = Country(self.column_header_list)
					td_list = tr.find_all("td")
					self.fillCountryInfo(c, td_list)
					self.list_countries_all[i].append(c)

	def createWorldTotal(self):
		for i in range(3):
			for tr in self.soup.find_all("table")[i].find_all("tr"):
				if (tr.has_attr("class")) and tr["class"][0] == "total_row_world" and len(tr["class"]) == 1:
					worldTotal = Country(self.column_header_list)
					td_list = tr.find_all("td")
					self.fillCountryInfo(worldTotal, td_list)
					self.list_world_total_all.append(worldTotal)

	def fillCountryInfo(self, country, td_list):
		for index, header in enumerate(self.column_header_list):
			if len(td_list[index].contents) > 0: country.headersDict[header] = td_list[index].contents[0].string.strip()
	
	def worldTotal_to_csv(self, filepath, separator):
		timestamp = "Updated at :" + str(datetime.datetime.now())
		titles = ["World Total Today:", "World Total Yesterday:", "World Total Yesterday 2:"]
		header = separator.join(self.column_header_list)
		self.add_line_text(filepath, "----------------------------------------------------------------------------------")
		self.add_line_text(filepath, timestamp)
		for index, w in enumerate(self.list_world_total_all):
			self.add_line_text(filepath, titles[index])
			self.add_line_text(filepath, header)
			w.to_csv(filepath, separator)
			self.add_new_line(filepath)

	def countries_to_csv(self, filepath, separator):
		timestamp = "Updated at :" + str(datetime.datetime.now())
		titles = ["Countries Today:", "Countries Yesterday:", "Countries Yesterday 2:"]
		header = separator.join(self.column_header_list)
		self.add_line_text(filepath, "----------------------------------------------------------------------------------")
		self.add_line_text(filepath, timestamp)
		for index, countries in enumerate(self.list_countries_all):
			self.add_line_text(filepath, titles[index])
			self.add_line_text(filepath, header)
			for c in countries:
				c.to_csv(filepath, separator)
			self.add_new_line(filepath)

	def add_new_line(self, filepath):
		f = open(filepath, "a", encoding="utf-8")
		f.write("\n")
		f.close()
	
	def add_line_text(self, filepath, text):
		f = open(filepath, "a", encoding="utf-8")
		text += "\n"
		f.write(text)
		f.close()


class Scrapper:
	def __init__(self, configPath):
		cfg = configparser.ConfigParser()
		cfg.read(configPath)
		self.website = cfg["scrapper_config"]["website"].strip('"')
		self.user_agent = cfg["scrapper_config"]["user_agent"].strip('"')
		self.filepath_country = cfg["scrapper_config"]["filepath_country"].strip('"')
		self.filepath_world = cfg["scrapper_config"]["filepath_world"].strip('"')
		self.filepath_copy = cfg["scrapper_config"]["filepath_copy"].strip('"')
		self.max_file_size_kb = int(cfg["scrapper_config"]["max_file_size_kb"])
		self.interval_in_sec = int(cfg["scrapper_config"]["interval_in_sec"])
		self.separator = cfg["scrapper_config"]["separator"].strip('"')
		self.get_ride_of_space_in_totalDeaths = bool(cfg["scrapper_config"]["get_ride_of_space_in_totalDeaths"])
		self.with_headers = cfg["scrapper_config"]["with_headers"].strip('"')
		self.website_content = None
		self.soup = None

	def extract_website_content(self):
		headers = {}
		headers['User-Agent'] = self.user_agent
		req = urllib.request.Request(self.website, headers = headers)
		open_req = urllib.request.urlopen(req)
		read_req = open_req.read().decode('utf-8')
		self.website_content = read_req
		self.soup = BeautifulSoup(self.website_content, 'html.parser')

	def save_to_csv(self):
		c = CountriesHandler(self.soup)
		c.createCountries()
		c.createWorldTotal()
		c.countries_to_csv(self.filepath_country, self.separator)
		c.worldTotal_to_csv(self.filepath_world, self.separator)

	def update_data(self):
		starttime = time.time()
		while True:
			COLOR_OKGREEN = '\033[92m'
			COLOR_ENDC = '\033[0m'
			print(f"{COLOR_OKGREEN}Extracting...{COLOR_ENDC}")
			self.extract_website_content()
			print(f"{COLOR_OKGREEN}Saving...{COLOR_ENDC}")
			self.save_to_csv()
			time.sleep(self.interval_in_sec - ((time.time() - starttime) % self.interval_in_sec))
			self.copy_file()

	def copy_file(self):
		COLOR_OKGREEN = '\033[92m'
		COLOR_ENDC = '\033[0m'
		filepahts = [self.filepath_country, self.filepath_world]
		for filepath in filepahts:
			if (Path(filepath).stat().st_size / 1000 > self.max_file_size_kb):
				print(f"{COLOR_OKGREEN}Copying...{COLOR_ENDC}")
				if (filepath == self.filepath_country):
					copyFilePath = self.filepath_copy + "coronavirus_data_countries_save_" + \
						datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".csv"
				if (filepath == self.filepath_world):
					copyFilePath = self.filepath_copy + "coronavirus_data_world_total_save_" + \
						datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".csv"

				shutil.copy2(filepath, copyFilePath)

				print(f"{COLOR_OKGREEN}Cleaning...{COLOR_ENDC}")
				f = open(self.filepath_country, "w")
				f.truncate()
				f.close()

		

from bs4 import BeautifulSoup
from pathlib import Path
import urllib.request
import configparser
import time
import datetime
import shutil

s = Scrapper("./config_scrapper.ini")
# s.extract_website_content()
# s.save_to_csv()
s.update_data()
# s.check_file_size()

# cfg = configparser.ConfigParser()
# cfg.read("./config_scrapper.ini")
# ss = cfg["scrapper_config"]
# for a in ss:
	# print(ss[a])
	
# headers = {}
# headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"

# req = urllib.request.Request('https://www.worldometers.info/coronavirus/#countries', headers = headers)
# x = urllib.request.urlopen(req)
# # print(x.read())

# file_name = "../csv_data/coronavirus_data.txt"
# f = open(file_name, "w", encoding="utf-8")
# f.write(x.read().decode('utf-8'))
# f.close()

# def tr_with_void_style(tag):
    # return tag.tr and tag.has_attr('style')

# s = open(file_name, "r", encoding="utf-8")
# soup = BeautifulSoup(s, 'html.parser')
# print(soup.find_all(tr_with_void_style)[2])
# print(soup.find("tr", style=''))

# soup = soup.find_all("tr", {'style': [None]}, limit=6)

# soup = soup.find_all("tr", {'style': [""]})
# soup.find_all("tr", {'style': [""]})

# def total_row_world_class_only(css_class):
    # return css_class is not None and css_class == 'total_row_world'

# print(cfg.scrapper_config["website"])

# print(first_row_index)

# soup = soup.find_all("table")[0]
# soup = soup.find_all("tr")




# c = CountriesHandler(soup)
# c.createCountries()
# c.createWorldTotal()
# c.countries_to_csv("../csv_data/coronavirus_data.csv", ";")
# c.worldTotal_to_csv("../csv_data/coronavirus_data_total.csv", ";")
