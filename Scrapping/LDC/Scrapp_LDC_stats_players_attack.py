import time
from selenium import webdriver
import pandas as pd
from pathlib import Path

browser = webdriver.Chrome('C:\Program Files\chromedriver_win32\chromedriver')

browser.get('https://www.uefa.com/uefachampionsleague/statistics/players/attacking/')
time.sleep(2)

browser.maximize_window()
time.sleep(2)

cookies = browser.find_element_by_xpath('/html/body/div[7]/div[2]/div/div[1]/div/div[2]/div/button[3]')
cookies.click()
time.sleep(2) 

team= browser.find_elements_by_tag_name("pk-table-row")
list_team = [elem.text for elem in team]
print(list_team)

df = pd.DataFrame(list(zip(list_team)),
                columns =['team'])
                
df = df.replace({r'\n': " "}, regex=True)
df = df.replace({'Man City': "Man_City"}, regex=True)
df = df.replace({'Real Madrid': "Real_Madrid"}, regex=True)
df = df.replace({'Shakhtar Donetsk': "Shakhtar_Donetsk"}, regex=True)
df = df.replace({'Club Brugge': "Club_Brugge"}, regex=True)
df = df.replace({'Dinamo Zagreb': "Dinamo_Zagreb"}, regex=True)
df = df.replace({'M. Haifa': "M._Haifa"}, regex=True)
df = df.replace({'Sporting CP': "Sporting_CP"}, regex=True)
df = df.replace({'Czech Republic': "Czech_Republic"}, regex=True)
df = df.replace({'João Cancelo': "João_Cancelo"}, regex=True)
df = df.replace({'Diogo Jota': "Diogo_Jota"}, regex=True)
df = df.replace({'De Bruyne': "De_Bruyne"}, regex=True)
df = df.replace({'Di María': "Di_María"}, regex=True)
df = df.replace({'André Silva': "André_Silva"}, regex=True)
df = df.replace({'Zambo Anguissa': "Zambo_Anguissa"}, regex=True)
df = df.replace({'Vinícius Júnior': "Vinícius_Júnior"}, regex=True)
df = df.replace({'Rafa Silva': "Rafa_Silva"}, regex=True)
df = df.replace({'Alexis Sánchez': "Alexis_Sánchez"}, regex=True)




filepath = Path(r'dataset\LDC\ucl_players_attack.csv')
filepath.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(filepath)
print(df)

browser.close()