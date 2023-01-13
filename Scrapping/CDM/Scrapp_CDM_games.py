import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
from pathlib import Path


browser = webdriver.Chrome('C:\Program Files\chromedriver_win32\chromedriver')

browser.get('https://www.flashscore.com/')
time.sleep(2)

browser.maximize_window()
time.sleep(2)

cookies = browser.find_element_by_id('onetrust-accept-btn-handler')
cookies.click()
time.sleep(3)

cdm = browser.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/aside/div/div[2]/div[2]/div[3]/div[2]/a/span[2]')
cdm.click()
time.sleep(2)

fixtures = browser.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/main/div[4]/div[1]/div[3]/div/a[3]') 
fixtures.click()
time.sleep(2)

date = browser.find_elements_by_class_name('event__time')
list_date= [elem.text for elem in date]
print(list_date)

equipe_dom = browser.find_elements_by_class_name('event__participant--home')
list_equipe_dom = [elem.text for elem in equipe_dom]
print(list_equipe_dom)

equipe_ext = browser.find_elements_by_class_name('event__participant--away')
list_equipe_ext = [elem.text for elem in equipe_ext]
print(list_equipe_ext)

df = pd.DataFrame(list(zip(list_date, list_equipe_dom, list_equipe_ext)),
                columns =['date', 'equipe_dom', 'equipe_ext'])

filepath = Path('C:/Users/diogo/OneDrive/Documents/GitHub/Projet-big-data/dataset/CDM/cdm_games.csv')
filepath.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(filepath)
print(df)

browser.close()
