import requests
import bs4
from bs4 import BeautifulSoup
import pandas as pd
import re

nano = requests.get('https://nano.tatamotors.com/price')
nano
#<Response [200]>
nanosoup = BeautifulSoup(nano.text)
nanosoup
nanofigcap = nanosoup.find_all('figcaption')
type(nanofigcap)
#bs4.element.ResultSet
Model = []
Engine = []
Price = []
for i in nanofigcap:
    data = i.text
    
    ########################## Model #################
    mn = re.findall(r'[GE]\w+\s\w+',data)
    #print(mn)
    Model.append(''.join(mn))
    
    ##################### Engine #####################
    et = re.findall(r'[PC]\w*',data)
    #print(et)
    Engine.append(''.join(et))
    
    ##################### Price ######################
    pr = re.findall(r'\d+\W\d+\W\d+',data)
    #print(pr)
    Price.append(''.join(pr))
    Model = list(filter(lambda item: item.strip(), Model))
#len(Variant)
Engine = list(filter(lambda item: item.strip(), Engine))
Price = list(filter(lambda item: item.strip(), Price))
#len(Price)
df = pd.DataFrame()
df['Model'] = Model
df['EngineType'] = Engine
df['Price'] = Price
df
##OUTPUT:::
     Model	 EngineType	 Price
0	   GenX XE	 Petrol	 2,36,447
1	   GenX XM	 Petrol	 2,72,223
2	   GenX XT	 Petrol	 2,92,667
3	   GenX XMA	 Petrol	 3,14,815
4	   GenX XTA	 Petrol	 3,34,768
5	EMax XM	CNG	2,96,662
