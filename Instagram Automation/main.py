from selenium import webdriver
# from .config import Username, Password
import time

friends = ['nihal_linox', 'online_shopping_cafe']

browser = webdriver.Chrome(executable_path='C:\chromedriver\chromedriver')
browser.maximize_window()
browser.get('http://www.instagram.com/')

time.sleep(2)

username = browser.find_element_by_name('username')
username.send_keys('lite_book')

password = browser.find_element_by_name('password')
password.send_keys('Instagram.com29')

time.sleep(2)

Signin_btn = browser.find_element_by_css_selector('button[type="submit"]')
Signin_btn.click()

time.sleep(2)

for friend in friends:
    browser.get(f'https://www.instagram.com/{friend}/')
    posts, followers, following = browser.find_elements_by_class_name('g47SY')
    #print(posts.text, followers.text, following.text)
    time.sleep(1)
    bio = browser.find_element_by_class_name('-vDIg')
    #print(bio.text)

    with open(f"{friend}.txt", 'w', encoding="utf-8") as file:
        file.write(
            f"Number Posts: {posts.text}\nFollowers: {followers.text}\nFollowing{following.text}\n\nBio:\n{bio.text}")

    time.sleep(1)