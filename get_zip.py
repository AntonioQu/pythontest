# pip install XlsxWriter
# pip install requests beautifulsoup4

import requests
import bs4
import xlsxwriter
import datetime

name_workbook = 'zipcode_mexico.xlsx'
workbook = xlsxwriter.Workbook(name_workbook)

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
print(states)
print(states_link)

for i in range(0,lenth_states):
	flag = 1
	worksheet = workbook.add_worksheet(states[i])
	worksheet.write('A1', 'Asentamiento')
	worksheet.write('B1', 'Tipo de Asentamiento')
	worksheet.write('C1', 'Código Postal')
	worksheet.write('D1', 'Municipio')
	worksheet.write('E1', 'Ciudad')
	worksheet.write('F1', 'Zona')
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
	for k in range(0,lenth_cities):
		url_third = url + cities_link[k]
		response = requests.get(url_third)
		soup = bs4.BeautifulSoup(response.text, "html.parser")
		table_zip = soup.find('table')
		trs = table_zip.find_all('tr')
		lenth_trs = len(trs)
		for x in range(1,lenth_trs):
			tds = trs[x].find_all('td')
			lenth_tds = len(tds)
			if lenth_tds>5:
				for y in range(0,lenth_tds):
					worksheet.write(flag,y,tds[y].text)
				print(flag)
				flag +=1
	print('{:.2%}'.format(i / lenth_states))
workbook.close()
print('finished')



