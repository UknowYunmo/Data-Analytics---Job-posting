from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request
import time
f=open('c:\\data\\gimo3.txt','w',encoding='UTF-16')
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
f.write(str(text)+'\n')
browser.find_element_by_xpath('//*[@id="sp_main_wrapper"]/div[2]/ul/li[2]/button/span[1]').click() # 지역 선택 버튼
browser.find_element_by_xpath('//*[@id="depth1_btn_102000"]/button').click() # 경기 지역 선택
browser.find_element_by_xpath('//*[@id="sp_area_lastDepth_102000"]/li[15]/div/label').click() # 부천시 선택
time.sleep(2)
browser.implicitly_wait(2)
html = browser.page_source
soup = BeautifulSoup(html, "lxml")
text=soup.select('span.count > b')[0].get_text()
print(text)
f.write(str(text)+'\n')
browser.find_element_by_class_name('btn_detail_option').click() # 상세 조건 버튼
browser.find_element_by_class_name('btn_open_layer').click() # 경력 버튼
html = browser.page_source
soup = BeautifulSoup(html, "lxml")
browser.find_element_by_xpath('//*[@id="sp_main_wrapper"]/div[1]/div[1]/div/div[1]/div[1]/label').click() # 신입
browser.find_element_by_xpath('//*[@id="sp_main_wrapper"]/div[1]/div[1]/div/div[1]/div[2]/label').click() # 경력
browser.find_element_by_xpath('//*[@id="sp_main_wrapper"]/div[1]/div[1]/div/div[1]/div[3]/label').click() # 무관
browser.find_element_by_xpath('//*[@id="btn_check_career_over0"]').click() # 경력 ~1년
browser.find_element_by_xpath('//*[@id="btn_check_career_over12"]').click() # 경력 ~12년
browser.find_element_by_xpath('//*[@id="sp_main_wrapper"]/div[1]/div[1]/div/div[3]/button[2]').click() # 경력창 닫기
time.sleep(2)
browser.implicitly_wait(2)
html = browser.page_source
soup = BeautifulSoup(html, "lxml")
text=soup.select('span.count > b')[0].get_text()
print(text)
f.write(str(text)+'\n')
browser.find_element_by_class_name('sri_select').click() # 연봉 체크박스 버튼
browser.find_elements_by_class_name('link_opt')[6].click() # 체크박스 6번째 (2400만원)
###업데이트 복붙###
time.sleep(2)
browser.implicitly_wait(2)
html = browser.page_source
soup = BeautifulSoup(html, "lxml")
text=soup.select('span.count > b')[0].get_text()
print(text)
f.write(str(text)+'\n')
###업데이트 복붙###
browser.find_element_by_xpath('//*[@id="sp_company_type"]/div/div[1]/ul/li[1]/span/label').click() # 대기업 선택
browser.find_element_by_class_name('btn_welfare').click() # 복리후생 선택
browser.find_element_by_xpath('//*[@id="sp_welfare_layer"]/div[2]/table/tbody/tr[2]/td[1]/ul/li[1]/span/label').click()
# 복리후생 첫번째 (건강검진)
browser.find_element_by_xpath('//*[@id="sp_welfare_layer"]/div[2]/table/tbody/tr[4]/td[3]/ul/li[16]/span/label').click()
# 복리후생 마지막 (시간제 연차)
browser.find_element_by_xpath('//*[@id="sp_welfare_layer"]/div[3]/button').click() # 세부 선택 닫기
###업데이트 복붙###
time.sleep(2)
browser.implicitly_wait(2)
html = browser.page_source
soup = BeautifulSoup(html, "lxml")
text=soup.select('span.count > b')[0].get_text()
print(text)
f.write(str(text)+'\n')
f.close()
###업데이트 복붙###