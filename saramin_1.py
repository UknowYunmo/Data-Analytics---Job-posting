from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request
import time
f=open('c:\\data\\gimo.txt','w',encoding='UTF-16')
binary = 'C:\chromedriver\chromedriver.exe'
browser = webdriver.Chrome(binary)
browser.get("http://www.saramin.co.kr/zf_user/search?search_area=main&search_done=y&search_optional_item=n&searchType=default_mysearch&searchword=%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EB%B6%84%EC%84%9D")
browser.maximize_window()
time.sleep(3)
browser.implicitly_wait(3)
html = browser.page_source
soup = BeautifulSoup(html, "lxml")
text=soup.select('span.count > b')[0].get_text() # 총 건수
print(text)
f.write(text)
browser.find_element_by_class_name('btn_detail_option').click() # 상세 조건 버튼
browser.find_element_by_class_name('btn_open_layer').click() # 경력 버튼
html = browser.page_source
soup = BeautifulSoup(html, "lxml")
#browser.find_element_by_class_name('lbl').click()
browser.find_element_by_xpath('//*[@id="sp_main_wrapper"]/div[1]/div[1]/div/div[1]/div[1]/label').click() # 신입
browser.find_element_by_xpath('//*[@id="sp_main_wrapper"]/div[1]/div[1]/div/div[1]/div[2]/label').click() # 경력
browser.find_element_by_xpath('//*[@id="sp_main_wrapper"]/div[1]/div[1]/div/div[1]/div[3]/label').click() # 무관
browser.find_element_by_xpath('//*[@id="btn_check_career_over0"]').click() # 경력 ~1년
browser.find_element_by_xpath('//*[@id="btn_check_career_over12"]').click() # 경력 ~12년
browser.find_element_by_xpath('//*[@id="sp_main_wrapper"]/div[1]/div[1]/div/div[3]/button[2]').click()
#browser.find_element_by_class_name('closeDefaultOptionLayer btn_basic_type02 btn_close').click()
time.sleep(2)
browser.implicitly_wait(2)
html = browser.page_source
soup = BeautifulSoup(html, "lxml")
text=soup.select('span.count > b')[0].get_text()
print(text)
#//*[@id="company_type_scale001"]
#//*[@id="sp_company_type"]/div/div[1]/ul/li[1]/span/label
#//*[@id="company_type_scale002"]
#//*[@id="sp_company_type"]/div/div[1]/ul/li[2]/span/label
#browser.find_element_by_xpath('//*[@id="sp_salary"]/div/div/button').click()
#browser.find_element_by_xpath('//*[@id="sal_min"]').click()
html = browser.page_source
soup = BeautifulSoup(html, "lxml")
browser.find_element_by_class_name('sri_select').click()
