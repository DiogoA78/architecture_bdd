import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
from pathlib import Path
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome('C:\Program Files\chromedriver_win32\chromedriver')

browser.get('https://www.uefa.com/uefachampionsleague/statistics/players/disciplinary/')
time.sleep(2)

browser.maximize_window()
time.sleep(2)

cookies = browser.find_element_by_xpath('/html/body/div[6]/div[2]/div/div[1]/div/div[2]/div/button[3]')
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
df = df.replace({'Abu Fani': "Abu_Fani"}, regex=True)
df = df.replace({'Pedro Gonçalves': "Pedro_Gonçalves"}, regex=True)
df = df.replace({'Gonçalo Ramos': "Gonçalo_Ramos"}, regex=True)
df = df.replace({'Kolo Muani': "Kolo_Muani"}, regex=True)
df = df.replace({'J. Timber': "J._Timber"}, regex=True)


filepath = Path('C:/Users/diogo/OneDrive/Documents/GitHub/Projet-big-data/work/data/LDC/ucl_players_discip.csv')
filepath.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(filepath)
print(df)

browser.close()