import requests 
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup

reponse  = requests.get('https://www.nchmf.gov.vn/kttv/')
soup = BeautifulSoup(reponse.content,'html.parser')
data = soup.find_all('div',class_='wt-city uk-position-relative uk-box-shadow-small')
link=[]
province_name =[]
temp=[]
for item in data:
    title = item.find('h2').text
    data1 = item.find_all('li')
    for j in data1:
        link.append(j.a.get('href'))
        province_name.append(j.find('a',class_='name-wt-city').text.strip())
    for item2 in data1:
        temp.append(item2.find('div',class_='temp-wt-city').text)
print(title)
df = pd.DataFrame({'province_name':province_name,
                   'temp':temp,
                   'link':link})
df.to_csv(r'D:\project_data\1.1_requests_weather\data\nhiet_do_ca_nuoc.csv')








































