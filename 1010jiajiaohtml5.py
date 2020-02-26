from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException

import os
import time
import requests

#turl = input("网址 url\n")
#loc = input("保存路径\n")
turl = "http://www.1010jiajiao.com/html5app/daan/answer/id/1247317" 
loc = "./tfqy9-b/"


ff_options = webdriver.firefox.options.Options()
#ff_options.add_argument('--headless')
work = webdriver.Firefox(options=ff_options)

if __name__ == "__main__":
    work.get(turl)
    os.system("rm -rf " + loc)
    os.mkdir(loc)
    cnt = int()
    arr = work.find_elements_by_css_selector("#scroll_pic_nav li")
    for tmp in arr:
        cnt = cnt + 1
        tmp.click()
        time.sleep(0.8)
        url = work.find_element_by_css_selector("#image_zoom_" + str(cnt - 1) + " img").get_attribute('src')
        with open(loc + '/' + str(cnt) + '.jpg', 'wb+') as f:
            f.write(requests.get(url).content)
        print('download page ' + str(cnt) + ' succesfully')

    print(cnt)
