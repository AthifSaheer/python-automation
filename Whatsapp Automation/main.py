from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from config import CHROME_PROFILE_PATH
from selenium import webdriver
import pyperclip
import time
import sys

try:
    if sys.argv[1]:
        with open(sys.argv[1], "r", encoding="utf-8") as f:
            groups = [group.strip() for group in f.readlines()]
except IndexError:
    print("Provid File Name With Extention")

with open("message.txt", "r", encoding="utf8") as f:
    msg = f.read()

non_qrcode = webdriver.ChromeOptions()
non_qrcode.add_argument(CHROME_PROFILE_PATH)

browser = webdriver.Chrome(executable_path='C:\chromedriver\chromedriver', options=non_qrcode)
browser.maximize_window()
browser.get('https://web.whatsapp.com/')
time.sleep(1)

for group in groups:
    search_xpath = '//div[@contenteditable="true"][@data-tab="3"]'

    search_box = WebDriverWait(browser, 500).until(
        EC.presence_of_element_located((By.XPATH, search_xpath))
    )

    pyperclip.copy(group)
    search_box.send_keys(Keys.CONTROL + "v")

    time.sleep(1)
    group_title_xpath = f'//span[@title="{group}"]'
    group_title = browser.find_element_by_xpath(group_title_xpath)
    group_title.click()

    time.sleep(1)
    message_xpath = '//div[@contenteditable="true"][@data-tab="6"]'
    message_box = browser.find_element_by_xpath(message_xpath)
    pyperclip.copy(msg)
    message_box.send_keys(Keys.CONTROL + "v")
    message_box.send_keys(Keys.ENTER)

    try:
        sys.argv[2] 
        attach_xpath = '//div[@aria-disabled="false"][@title="Attach"]'
        attach_btn = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, attach_xpath)))
        attach_btn.click()

        image_btn = browser.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
        image_btn.send_keys(sys.argv[2])
        time.sleep(2)

        caption = browser.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="6"]')
        caption.send_keys(sys.argv[3])
        time.sleep(1)

        send_btn = browser.find_element_by_xpath('//span[@data-icon="send"]')
        send_btn.click()
        time.sleep(2)

    except IndexError:
        pass
    