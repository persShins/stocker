import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import plotly.graph_objects as go
url = "https://finance.naver.com/sise/sise_market_sum.nhn?page=1"
res = requests.get(url)
soup = BeautifulSoup(res.text, 'lxml')
def Basic():
    stock_data=[]
    url = "https://finance.naver.com/sise/sise_market_sum.nhn?page=1"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    stock_list = soup.find("table", attrs={"class": "type_2"}).find("tbody").find_all("tr")
    for stock in stock_list:
        if len(stock) > 1 :
            stock_data.append(stock.get_text().split()[2])
    return stock_data
def Kospi50():
    code=[]
    stock_Url=soup.find("table", attrs={"class": "type_2"}).find("tbody").find_all("a", attrs={"class": "tltle"})
    for index, stock in enumerate(stock_Url):
        code.append(stock['href'].split('=')[1])
    current_value=Basic()
    dict={"Code":code, "Current_value":current_value}
    Data=pd.DataFrame(dict)
    return Data
def Kospi500():#I've only thought about scrapping the first page of kospi
    code=[]
    while True:
        url = "https://finance.naver.com/sise/sise_market_sum.nhn?page="+36
        print(url)
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'lxml')
        stock_Url=soup.find("table", attrs={"class": "type_2"}).find("tbody").find_all("a", attrs={"class": "tltle"})
        for index, stock in enumerate(stock_Url):
            code.append(stock['href'].split('=')[1])
    current_value=Basic()
    dict={"Code":code, "Current_value":current_value}
    Data=pd.DataFrame(dict)
    return Data
