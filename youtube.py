from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def get_recent_videos(path):
    driver = webdriver.Chrome(path)

    delay = 3
    driver.implicitly_wait(delay)
    driver.get('https://www.youtube.com/results?search_query=%EC%98%A4%EB%A7%88%EC%9D%B4%EA%B1%B8&sp=CAI%253D')
    #driver.maximize_window()

    body = driver.find_element_by_tag_name('body')

    num_of_pagedowns = 10
    while num_of_pagedowns:
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.3)
        num_of_pagedowns -= 1

    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    #titles = soup.find_all('a','yt-simple-endpoint style-scope ytd-video-renderer')
    #all_title = []
    #for title in titles:
    #    all_title.append(title.get_text())

    rawsource = soup.find_all(class_="style-scope ytd-video-renderer")
    title_link = []
    for raw in rawsource:
        parselink = raw.find("a","yt-simple-endpoint style-scope ytd-video-renderer")
        arg = []
        if(parselink != None):
            link = "https://www.youtube.com" + parselink.get("href").replace("..","").replace("./","",1)
            title = parselink.get_text().replace("\n","")
            arg.append(title)
            arg.append(link)
            title_link.append(arg)

    driver.close()
    return title_link
    # for key, value in title_link.items():
    #     print(key ,value)
