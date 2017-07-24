# pip install XlsxWriter
# pip install requests beautifulsoup4

import requests
import bs4
import xlsxwriter
import datetime
import sys

date_now = datetime.datetime.now().strftime("%Y-%m-%d")
date_7_ago = datetime.datetime.now()-datetime.timedelta(days=7)
date_7_ago = date_7_ago.strftime("%Y-%m-%d")

def getDOF_7(start_date, end_date):
    dof_7 = []
    url = 'http://www.dof.gob.mx/indicadores_detalle.php?cod_tipo_indicador=158&dfecha=' + start_date[8:10] + '%2F' + start_date[5:7] + '%2F' + start_date[0:4] + '&hfecha=' + end_date[8:10]  + '%2F' + end_date[5:7] + '%2F' + end_date[0:4]
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    tabels = soup.find('table',{'class':'Tabla_borde'})
    trs = tabels.find_all('tr',{'class':'Celda 1'})
    lenth_trs = len(trs)
    for tr in trs:
        td = tr.find_all('td')
        dof_7.append([td[0].text.strip(), float(td[1].text.strip())])
    return dof_7


def progress_bar(percent, bar_length=30):
    hashes = '#' * int(round(percent * bar_length))
    spaces = '-' * (bar_length - len(hashes))
    sys.stdout.write("\rPercent: [{0}] {1}%".format(hashes + spaces, int(round(percent * 100))))
    sys.stdout.flush()

def getDOF(start_date, end_date):
    if len(start_date) !=10:
        start_date='1991-11-13'
    if len(end_date) !=10:
        end_date=date_now
    print('wainting for get page......')
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
    print('start downloading......')
    for tr in trs:
        td = tr.find_all('td')
        worksheet.write('A' + str(i), td[0].text.strip())
        worksheet.write('B'+ str(i), float(td[1].text.strip()))
        percent = i/lenth_trs
        progress_bar(percent)
        i += 1
    workbook.close()
    print('\nfile saved as name:' + name_workbook)
    
if __name__ == '__main__':
    dof_7 = getDOF_7(date_7_ago, date_now)
    print("-------------------recently DOF-------------------\n")
    for dof in dof_7:
        print(dof[0] + "  :  " + str(dof[1]) + '\n')
    print("-----------check DOF between any dates-----------\n")
    start_date=input("Enter start date, format YYYY-MM-DD:\n")
    end_date=input("Enter end date, format YYYY-MM-DD:\n")
    getDOF(start_date, end_date)
    input('press any key to quit...')