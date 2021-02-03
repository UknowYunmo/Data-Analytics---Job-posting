from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request
import time
import csv
f = open('c:\\data\\saram101.csv','w', newline='')
wr = csv.writer(f)
wr.writerow(['경력','연봉','기업수'])
pay_cnt=-1
car_cnt=-1
binary = 'C:\chromedriver\chromedriver.exe'
browser = webdriver.Chrome(binary)
browser.get("http://www.saramin.co.kr/zf_user/search?search_area=main&search_done=y&search_optional_item=n&searchType=default_mysearch&searchword=%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EB%B6%84%EC%84%9D")
browser.maximize_window()
time.sleep(3)
browser.implicitly_wait(3)
browser.find_element_by_class_name('btn_detail_option').click() # 상세 조건 버튼
browser.find_element_by_xpath('//*[@id="sp_company_type"]/div/div[6]/button[2]').click() # 기업 펼치기
career=['신입','6개월','1년차','2년차','3년차','4년차','5년차','6년차','7년차','8년차','9년차','10년차']
pay=['2400만 이상','2600만 이상','2800만 이상','3000만 이상','3200만 이상','3400만 이상','3600만 이상','3800만 이상','4000만 이상','5000만 이상','6000만 이상','7000만 이상','8000만 이상']
for i in range(len(career)):
    car_cnt+=1
    browser.find_element_by_class_name('btn_open_layer').click() # 경력 버튼
    if i==0: # 신입
        browser.find_element_by_xpath('//*[@id="sp_main_wrapper"]/div[1]/div[1]/div/div[1]/div[1]/label').click() # 신입
        browser.find_element_by_xpath('//*[@id="sp_main_wrapper"]/div[1]/div[1]/div/div[1]/div[3]/label').click() # 무관
        browser.find_element_by_xpath('//*[@id="sp_main_wrapper"]/div[1]/div[1]/div/div[3]/button[2]').click() # 경력창 닫기
    else:
        browser.find_element_by_xpath('//*[@id="btn_check_career_over'+str(i)+'"]').click()
        browser.find_element_by_xpath('//*[@id="btn_check_career_over0"]').click()
        browser.find_element_by_xpath('//*[@id="sp_main_wrapper"]/div[1]/div[1]/div/div[3]/button[2]').click() # 경력창 닫기
    for a in range(6,19):
        pay_cnt+=1
        browser.find_element_by_class_name('sri_select').click() # 연봉 체크박스 버튼
        browser.find_elements_by_class_name('link_opt')[a].click() # 체크박스 6번째 (2400만원)
        time.sleep(4)
        browser.implicitly_wait(4)
        html = browser.page_source
        soup = BeautifulSoup(html, "lxml")
        text=soup.select('span.count > b')[0].get_text()
        print([career[car_cnt],pay[pay_cnt],str(text)])
        wr.writerow([career[car_cnt],pay[pay_cnt],str(text)])
    pay_cnt=-1
f.close()
    