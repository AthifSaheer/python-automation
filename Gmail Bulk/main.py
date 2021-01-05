from selenium import webdriver
from config import Email
from excel import data
import time


browser = webdriver.Edge(executable_path='C:\edgedriver_win64/msedgedriver')
# browser.maximize_window()
browser.get('https://onlinenotebook.net/')


for i in data.index:
    print(data.loc[i]['Name'])


text_body = browser.find_element_by_class_name('quick')
text_body.send_keys(data)
