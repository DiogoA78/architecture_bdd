import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
from pathlib import Path
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome('C:\Program Files\chromedriver_win32\chromedriver')

browser.get('https://www.uefa.com/uefaeuropaleague/statistics/players/attacking/')
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
df = df.replace({'Man United': "Man_United"}, regex=True)
df = df.replace({'Real Sociedad': "Real_Sociedad"}, regex=True)
df = df.replace({'Crvena zvezda': "Crvena_zvezda"}, regex=True)
df = df.replace({'AEK Larnaca': "AEK_Larnaca"}, regex=True)
df = df.replace({'Union Berlin': "Union_Berlin"}, regex=True)
df = df.replace({'Union SG': "Union_SG"}, regex=True)
df = df.replace({'Pep Biel': "Pep_Biel"}, regex=True)
df = df.replace({'Tokmac Nguen': "Tokmac_Nguen"}, regex=True)



filepath = Path(r'dataset\EL\el_stats_players_attack.csv')
filepath.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(filepath)
print(df)

browser.close()