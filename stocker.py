import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import plotly.graph_objects as go

url = "https://finance.naver.com/sise/sise_market_sum.nhn?page=1"
res = requests.get(url)
soup = BeautifulSoup(res.text, 'lxml')

def Basic(url=None):
    stock_data=[]
    if url==None:
        url = "https://finance.naver.com/sise/sise_market_sum.nhn?page=1"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    stock_list = soup.find("table", attrs={"class": "type_2"}).find("tbody").find_all("tr")
    for stock in stock_list:
        if(len(stock)>1):
            tmp=stock.get_text().split()
            stock_data.append(tmp[len(tmp)-10])
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

def Kospi_All():
    code=[]
    current_value=[]
    for i in range(1,36):
        url = "https://finance.naver.com/sise/sise_market_sum.nhn?page="+str(i)
        print(url)
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'lxml')
        #print(soup)
        stock_Url=soup.find("table", attrs={"class": "type_2"}).find("tbody").find_all("a", attrs={"class": "tltle"})
        for index, stock in enumerate(stock_Url):
            code.append(stock['href'].split('=')[1])
        current_value.extend(Basic(url))
    print(current_value)
    dict={"Code":code, "Current_value":current_value}
    data=pd.DataFrame(dict)
    return data