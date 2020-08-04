from selenium import webdriver

browser = webdriver.Chrome(executable_path='/home/safwan/chromedriver_linux64/chromedriver')

browser.get('https://www.google.com')

search_input = browser.find_element_by_name('q')
search_input.send_keys('python web development')

