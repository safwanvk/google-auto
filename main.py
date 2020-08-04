from selenium import webdriver
import time

browser = webdriver.Chrome(executable_path='/home/safwan/chromedriver_linux64/chromedriver')

browser.get('https://www.google.com')

time.sleep(2)

search_input = browser.find_element_by_name('q')
search_input.send_keys('python web development')

time.sleep(2)

search_btn = browser.find_element_by_css_selector('input[type="submit"]')
search_btn.click()

