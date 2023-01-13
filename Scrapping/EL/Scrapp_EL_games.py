import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
from pathlib import Path


browser = webdriver.Chrome('/Users/arounekrishnaraj/Desktop/BIGDATA projet/chromedriver')

browser.get('https://www.flashscore.com/')
time.sleep(2)

browser.maximize_window()
time.sleep(2)

cookies = browser.find_element_by_id('onetrust-accept-btn-handler')
cookies.click()
time.sleep(2)

el = browser.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/aside/div/div[2]/div[2]/div[1]/div[9]/a')
el.click()
time.sleep(2)

results = browser.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/main/div[4]/div[1]/div[3]/div/a[2]') 
results.click()
time.sleep(2)

date = browser.find_elements_by_class_name('event__time')
list_date= [elem.text for elem in date]
print(list_date)

equipe_dom = browser.find_elements_by_class_name('event__participant--home')
list_equipe_dom = [elem.text for elem in equipe_dom]
print(list_equipe_dom)

score_dom = browser.find_elements_by_class_name('event__score--home')
list_score_dom = [elem.text for elem in score_dom]
print(list_score_dom)

score_ext = browser.find_elements_by_class_name('event__score--away')
list_score_ext = [elem.text for elem in score_ext]
print(list_score_ext)

equipe_ext = browser.find_elements_by_class_name('event__participant--away')
list_equipe_ext = [elem.text for elem in equipe_ext]
print(list_equipe_ext)

df = pd.DataFrame(list(zip(list_date, list_equipe_dom, list_score_dom, list_score_ext, list_equipe_ext)),
                columns =['date', 'equipe_dom',  'score_dom', 'score_ext', 'equipe_ext'])

df = df.drop(df.index[[96,97,98,99,100,101,102,103,104]])

filepath = Path('/Users/arounekrishnaraj/Documents/Projet-big-data/dataset/EL/el_games.csv')
filepath.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(filepath)
print(df)

browser.close()
