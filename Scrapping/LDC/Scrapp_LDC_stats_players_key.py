import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
from pathlib import Path


browser = webdriver.Chrome('C:\Program Files\chromedriver_win32\chromedriver')

browser.get('https://www.uefa.com/uefachampionsleague/')
time.sleep(2)

browser.maximize_window()
time.sleep(2)

cookies = browser.find_element_by_xpath('/html/body/div[6]/div[2]/div/div[1]/div/div[2]/div/button[3]')
cookies.click()
time.sleep(2)

ucl = browser.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/nav/div[4]/div/ul/li[7]/a')
ucl.click()
time.sleep(2)

player = browser.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[1]/div[2]/div/div/div/pk-carousel/div/div[3]/pk-button/span')
player.click()
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
df = df.replace({'Van Dijk': "Van_Dijk"}, regex=True)
df = df.replace({'Diogo Costa': "Diogo_Costa"}, regex=True)
df = df.replace({'Nuno Tavares': "Nuno_Tavares"}, regex=True)

filepath = Path('C:/Users/diogo/OneDrive/Documents/GitHub/Projet-big-data/work/data/LDC/ucl_players_key.csv')
filepath.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(filepath)
print(df)

browser.close()