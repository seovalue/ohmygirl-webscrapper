
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def get_recent_videos(path):

    driver = webdriver.Chrome(path)

    delay = 3
    driver.implicitly_wait(delay)
    driver.get('https://tv.naver.com')
    #driver.maximize_window()
    elem = driver.find_element_by_id('searchQuery')
    elem.send_keys('오마이걸')
    time.sleep(0.5)
    elem.submit()

    driver.find_element_by_xpath('//*[@id="searchClip"]/div[1]/a').click()
    time.sleep(0.5)
    driver.find_element_by_xpath('//*[@id="clip_sort"]/ul/li[2]/a').click()

    html = driver.page_source
    soup = BeautifulSoup(html ,'lxml')
    rawsource = soup.find("div" ,{"class" :"cds_area"})

    title_link = []

    for raw in rawsource.find_all('a'):
        arg = []
        link = "https://tv.naver.com" + raw.get('href').replace("..", "").replace("./", "", 1)
        title = raw.get('title')
        arg.append(title)
        arg.append(link)
        title_link.append(arg)

    title_link = list(set(title_link))
    driver.close()
    return title_link