# pip install XlsxWriter
# pip install requests beautifulsoup4

import requests
import bs4
import xlsxwriter
import datetime
from tkinter import *

fields = ['Fecha Inicio', 'Fecha Final']

def getDOF(entries):
	start_date=entries[0][1].get()
	end_date=entries[1][1].get()
	url = 'http://www.dof.gob.mx/indicadores_detalle.php?cod_tipo_indicador=158&dfecha=' + start_date[8:10] + '%2F' + start_date[5:7] + '%2F' + start_date[0:4] + '&hfecha=' + end_date[8:10]  + '%2F' + end_date[5:7] + '%2F' + end_date[0:4]
	response = requests.get(url)
	soup = bs4.BeautifulSoup(response.text, "html.parser")
	tabels = soup.find('table',{'class':'Tabla_borde'})
	trs = tabels.find_all('tr',{'class':'Celda 1'})
	lenth_trs = len(trs)
	name_workbook = 'DOF' + start_date +' to ' + end_date + '.xlsx'
	workbook = xlsxwriter.Workbook(name_workbook)
	worksheet = workbook.add_worksheet()
	worksheet.write('A1', 'Date')
	worksheet.write('B1', 'DOF')
	i = 2
	for tr in trs:
		td = tr.find_all('td')
		worksheet.write('A' + str(i), td[0].text.strip())
		worksheet.write('B'+ str(i), float(td[1].text.strip()))
		i += 1
		if i % 10 == 0:
			print('{:.2%}'.format(i / lenth_trs))
	workbook.close()
	print('file saved as name:' + name_workbook)
	
def fetch(entries):
    for entry in entries:
        field = entry[0]
        text  = entry[1].get()
     # print('%s: "%s"' % (field, text)) 

def makeform(root, fields):
    entries = []
    for field in fields:
        row = Frame(root)
        lab = Label(row, width=15, text=field, anchor='w')
        ent = Entry(row)
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)
        entries.append((field, ent))
    entries[1][1].insert(0,datetime.datetime.now().strftime("%Y-%m-%d"))
    return entries

if __name__ == '__main__':
    root = Tk()
    root.title("Get DOF")
    w = 300 # width for the Tk root
    h = 300 # height for the Tk root

    # get screen width and height
    ws = root.winfo_screenwidth() # width of the screen
    hs = root.winfo_screenheight() # height of the screen

    # calculate x and y coordinates for the Tk root window
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    # set the dimensions of the screen 
    # and where it is placed
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.resizable(width=False, height=False)
    ents = makeform(root, fields)
    root.bind('<Return>', (lambda event, e=ents: fetch(e)))   
    b1 = Button(root, text='Show', command=(lambda e=ents: getDOF(e)))
    b1.pack(side=RIGHT, padx=50, pady=5)
    b2 = Button(root, text='Quit', command=root.quit)
    b2.pack(side=LEFT, padx=50, pady=5)
    w = Canvas(root, width=200, height=100)
    w.pack(side=BOTTOM, expand=YES, fill=X)
    w.create_rectangle(50, 25, 150, 75, fill="blue")
    root.mainloop()
