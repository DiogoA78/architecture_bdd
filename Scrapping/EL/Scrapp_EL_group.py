import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
from pathlib import Path


browser = webdriver.Chrome('/Users/arounekrishnaraj/Desktop/BIGDATA projet/chromedriver')

browser.get('https://www.uefa.com/uefaeuropaleague/')
time.sleep(2)

browser.maximize_window()
time.sleep(2)

cookies = browser.find_element_by_xpath('/html/body/div[6]/div[2]/div/div[1]/div/div[2]/div/button[3]')
cookies.click()
time.sleep(2)

el = browser.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/nav/div[4]/div/ul/li[4]/a')
el.click()
time.sleep(2)

team= browser.find_elements_by_class_name('js-team-name')
list_team = [elem.text for elem in team]
print(list_team)

match= browser.find_elements_by_class_name('js-played')
list_match = [elem.text for elem in match]
print(list_match)

win = browser.find_elements_by_class_name('js-won')
list_win = [elem.text for elem in win]
print(list_win)

draw = browser.find_elements_by_class_name('js-drawn')
list_draw = [elem.text for elem in draw]
print(list_draw)

lose = browser.find_elements_by_class_name('js-lost')
list_lose = [elem.text for elem in lose]
print(list_lose)

GF = browser.find_elements_by_class_name('js-goalsFor')
list_GF = [elem.text for elem in GF]
print(list_GF)

GA = browser.find_elements_by_class_name('js-goalsAgainst')
list_GA = [elem.text for elem in GA]
print(list_GA)

GD = browser.find_elements_by_class_name('js-goalDifference')
list_GD = [elem.text for elem in GD]
print(list_GD)

pts = browser.find_elements_by_class_name('js-points')
list_pts = [elem.text for elem in pts]
print(list_pts)

df = pd.DataFrame(list(zip(list_team, list_match, list_win, list_draw, list_lose, list_GF, list_GA, list_GD, list_pts)),
                columns =['team', 'nb_match',  'win', 'draw', 'lose', 'GF', 'GA', 'GD', 'pts'])

filepath = Path('/Users/arounekrishnaraj/Documents/Projet-big-data/dataset/EL/el_group.csv')
filepath.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(filepath)
print(df)

browser.close()
