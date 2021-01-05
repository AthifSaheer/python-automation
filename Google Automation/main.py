from selenium import webdriver
import time

# --------------------------Google Automation---------------------
browser = webdriver.Chrome(executable_path='C:\chromedriver\chromedriver')
browser.get('http://www.google.com')
search = browser.find_element_by_name('q')
search.send_keys('instagram')
time.sleep(3)
search_btn = browser.find_element_by_css_selector('input[type="submit"]')
search_btn.click()

# ----------YouTube Automation-----------------------------

window = webdriver.Chrome(executable_path='C:\chromedriver\chromedriver')
window.get('http://youtube.com')
search_bar = window.find_element_by_name('search_query')
search_bar.send_keys('Django Automation')
time.sleep(2)
srch_btn = window.find_element_by_css_selector('button[id="search-icon-legacy"]')
srch_btn.click()
video = window.find_element_by_class_name('class="style-scope ytd-video-renderer"')
video.click()
