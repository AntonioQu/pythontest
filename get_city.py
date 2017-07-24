# pip install XlsxWriter
# pip install requests beautifulsoup4

import requests
import bs4
import xlsxwriter
import sys


def progress_bar(percent, bar_length=30):
        hashes = '#' * int(round(percent * bar_length))
        spaces = '-' * (bar_length - len(hashes))
        sys.stdout.write("\rPercent: [{0}] {1}%".format(hashes + spaces, int(round(percent * 100))))
        sys.stdout.flush()

name_workbook = 'cities_mexico_1.xlsx'
workbook = xlsxwriter.Workbook(name_workbook)
worksheet = workbook.add_worksheet('states')
url = 'http://micodigopostal.org'
response = requests.get(url)
soup = bs4.BeautifulSoup(response.text, "html.parser")
table = soup.find('table')
states = []
states_link =[]
tds = table.find_all('td')
for td in tds:
	href = td.find('a')
	span = td.find('span')
	states_link.append(href['href'])
	states.append(span.text)
lenth_states = len(states)
worksheet.write_column('A1', states)

for i in range(0,lenth_states):
	worksheet = workbook.add_worksheet(states[i])
	url_second = url + states_link[i]
	response = requests.get(url_second)
	soup = bs4.BeautifulSoup(response.text, "html.parser")
	table = soup.find('table')
	cities = []
	cities_link = []
	tds = table.find_all('td')
	for td in tds:
		href = td.find('a')
		span = td.find('span')
		if span is not None and href is not None:
			cities_link.append(href['href'])
			cities.append(span.text)
	lenth_cities = len(cities)
	worksheet.write_column('A1', cities)
	percent = (i+1) / lenth_states
	progress_bar(percent)
workbook.close()
print('finished')



