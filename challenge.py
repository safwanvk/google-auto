from selenium import webdriver
import time

browser = webdriver.Chrome(executable_path='/home/safwan/chromedriver_linux64/chromedriver')

browser.get('https://jasim.tech/automation/one')

time.sleep(2)

search_input = browser.find_element_by_css_selector('input[type="text"]')
search_input.send_keys('safwanvk')

time.sleep(2)


search_btn = browser.find_element_by_css_selector('input[type="submit"]')
search_btn.click()