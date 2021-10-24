import sys
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
from PyQt5 import QtWidgets

from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))

from File_Handling.txtFile import TxtFile
from File_Handling.randomn import Random


class Scrapping:
    def __init__(self, progressBar, startBtn, stopBtn, label, table) -> None:
        self.r = Random(r"TextFiles\Authors.txt", r"TextFiles\languages.txt", r"TextFiles\Types.txt")
        self.f = TxtFile()
        self.links = self.f.readFile(r"TextFiles\links.txt")
        self.link = r"https://archive.org/details/"
        self.driverPath = r'C:\ProgramData\Anaconda3\chromedriver.exe'
        self.progressBar = progressBar
        self.startBtn = startBtn
        self.stopBtn = stopBtn
        self.label = label
        self.table = table
        self.running = True
    
    def start_scrapping(self):

        self.df = pd.read_csv("CSV_Files/UI_Scrapped_data.csv")
        self.data = self.df.to_dict('records')
        row_number = 0
        self.table.setRowCount(len(self.data))
        for line in self.data:
            self.table.setItem(row_number, 0, QtWidgets.QTableWidgetItem(str(line['Name'])))
            self.table.setItem(row_number, 1, QtWidgets.QTableWidgetItem(str(line['Id'])))
            self.table.setItem(row_number, 2, QtWidgets.QTableWidgetItem(str(line['Price'])))
            self.table.setItem(row_number, 3, QtWidgets.QTableWidgetItem(str(line['Pages'])))
            self.table.setItem(row_number, 4, QtWidgets.QTableWidgetItem(str(line['Author'])))
            self.table.setItem(row_number, 5, QtWidgets.QTableWidgetItem(str(line['Language'])))
            self.table.setItem(row_number, 6, QtWidgets.QTableWidgetItem(str(line['Type'])))
            row_number += 1

        self.data = self.f.readFile(r"TextFiles\data.txt")
        self.start = int(self.data[0])
        self.counter = int(self.data[1])
        self.num = int(self.data[2])

        self.driver = webdriver.Chrome(self.driverPath)
        value = ((self.num) / 1000000)*100
        self.progressBar.setValue(value)
        self.progressBar.setFormat("%.0002f %%" % value)
        for j in range(self.start, len(self.links)):
            for i in range(self.counter, -1, -1):
                
                # setting the text of label for scrapping source
                self.label.setText(self.link + self.links[j] + str(i))
                self.label.adjustSize()
                
                self.driver.get(self.link + self.links[j] + str(i))
                self.script = "return document.getElementById('ikind--week').innerHTML"
                self.content = self.driver.execute_script(self.script)
                self.soup = BeautifulSoup(self.content)
                self.findContent(j, i)
                
                if self.running == False:
                    break
            
            if self.running == False:
                break

            self.counter = 133
    
    def findContent(self, j, i):
        self.Names = []
        self.Ids = []
        self.Prices = []
        self.Pages = []
        self.Authors = []
        self.Languages = []
        self.Types = []

        self.contents = self.soup.findAll(class_="item-ia hov")
        for k in self.contents:
            name = (k.find("div", class_="ttl")).text
            if name != "":
                self.Names.append(((name.replace("\n", "")).replace('"', '')).strip())
                self.Ids.append(self.r.GetID())
                self.Prices.append(self.r.GetPrice())
                self.Pages.append(self.r.GetPages())
                self.Authors.append(self.r.GetAuthor())
                self.Languages.append(self.r.Getlanguage())
                self.Types.append(self.r.GetType())
        
        self.df = pd.DataFrame({'Name': self.Names, 'ID': self.Ids, 'Price': self.Prices, 'Pages': self.Pages, 'Author': self.Authors, "Language": self.Languages, 'Type': self.Types})
        self.df.to_csv('CSV_Files/UI_Scrapped_data.csv', index=False, encoding='utf-8', mode="a", header= False)
        self.num += len(self.Names)
        self.f.WriteToFile(r"TextFiles\data.txt", [str(j), str(i-1), str(self.num)])
        value = ((self.num) / 1000000)*100
        self.progressBar.setValue(value)
        self.progressBar.setFormat("%.0002f %%" % value)

# if __name__ == "__main__":
#     scr = Scrapping()
#     scr.start_scrapping()