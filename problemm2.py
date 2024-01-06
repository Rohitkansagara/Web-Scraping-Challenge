pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup
import csv
import time
import pandas as pd


product_name=[]
prices=[]
reviews=[]
Description=[]


for i in range(2,10):
  url="https://www.flipkart.com/search?q=iPhone&page="+str(i)
  r = requests.get(url)
  #print(r)
  soup = BeautifulSoup(r.text,'lxml') #for print html data\
  box=soup.find("div",class_="_1YokD2 _3Mn1Gg")

  names=soup.find_all("div",class_="_4rR01T")

  for i in names:
    name =i.text
    product_name.append(name)

  #print(product_name)

  prices=soup.find_all("div",class_="_30jeq3 _1_WHN1")  
  for i in prices:
    name=i.text
    prices.append(name)

  #print(prices)

  desc=soup.find_all("ul",class_="_1xgFaf")

  for i in desc:
    name=i.text
    Description.append(name)

  #print(Description)

   
  reviews=soup.find_all("div",class_="_3LWZlK")

  for i in reviews:
    name=i.text
    reviews.append(name)

 
  

df=pd.DataFrame({"Product Name":product_name,"prices":prices,"Description":Description,"Review":reviews})
print(df)
  
df.to_csv('flipkart_iphones.csv', index=False)




