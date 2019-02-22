from selenium import webdriver
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
# options.add_argument('headless')
options.add_argument('window-size=1920x1080')

driver = webdriver.Chrome('/Users/dojun/Downloads/chromedriver', chrome_options=options)
driver.get('https://www.instagram.com/lee_dojun/')

driver.implicitly_wait(3)
html = driver.page_source
soup = BeautifulSoup(html, 'lxml')
# driver.find_elements_by_css_selector('div.v1Nh3 > a')
divs = soup.find_all('div', class_='v1Nh3')

for div in divs:
    driver.get(f'https://www.instragram.com{div.find("a")["href"]}')
    driver.implicitly_wait(3)
    break


# a[0].click()
driver.get_screenshot_as_file('test.png')

# driver.quit()


# token 1497160209.d0ce4d7.d61dd80839b14bf49162e00e52e363a9