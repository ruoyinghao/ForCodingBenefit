#This python file uses BeautifulSoup to Scrap Amazon Trade-In Prices for an item
#The item in this file is Foundations of Higher Mathematics
#TODO:Scraping the price on a weekly basis
#The file needs a local csv file to run smoothly
#07/26/2016


from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import time
import csv

def getValue(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        getValue(url)
   
    bsObj = BeautifulSoup(html.read())
    value = bsObj.find(id="tradeInButton_tradeInValueLine")
    tradePrice=value.span.string
    return tradePrice


price=getValue("https://www.amazon.com/dp/053495166X")

time=time.strftime('%Y-%m-%d',time.localtime(time.time()))

file=open('FoundationsOfHigherMathematics.csv', 'a')
writer = csv.writer(file)
writer.writerow([time,price])

file.close()
print("recording is done")
