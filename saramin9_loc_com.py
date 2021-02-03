from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request
import time
import csv
f = open('c:\\data\\saram444.csv','w', newline='')
wr = csv.writer(f)
wr.writerow(['경력','기업형태','기업수'])
car_cnt=-1
com_cnt=-1
wel_cnt=-1
pay_cnt=-1
binary = 'C:\chromedriver\chromedriver.exe'
browser = webdriver.Chrome(binary)
browser.get("http://www.saramin.co.kr/zf_user/search?search_area=main&search_done=y&search_optional_item=n&searchType=default_mysearch&searchword=%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EB%B6%84%EC%84%9D")
browser.maximize_window()
time.sleep(3)
browser.implicitly_wait(3)
pay=['2400만 이상','2600만 이상','2800만 이상','3000만 이상','3200만 이상','3400만 이상','3600만 이상','3800만 이상','4000만 이상','5000만 이상','6000만 이상','7000만 이상','8000만 이상']
browser.find_element_by_class_name('btn_detail_option').click() # 상세 조건 버튼
browser.find_element_by_xpath('//*[@id="sp_company_type"]/div/div[6]/button[2]').click() # 기업 펼치기
career=['신입','6개월','1년차','2년차','3년차','4년차','5년차','6년차','7년차','8년차','9년차','10년차']
company=['대기업','매출1000대기업','중견기업','중소기업','스타트업','외국계(법인/투자)','금융기관','공기업','교육기관','수출입기업','코스닥','코스피','코넥스','벤처','강소기업','이노비즈','메인비즈','우수기업']
for i in range(12): #13
    car_cnt+=1
    browser.find_element_by_class_name('btn_open_layer').click() # 경력 버튼
    if i==0:
        #print('신입이에용')
        browser.find_element_by_xpath('//*[@id="sp_main_wrapper"]/div[1]/div[1]/div/div[1]/div[1]/label').click() # 신입
        browser.find_element_by_xpath('//*[@id="sp_main_wrapper"]/div[1]/div[1]/div/div[1]/div[3]/label').click() # 무관
        browser.find_element_by_xpath('//*[@id="sp_main_wrapper"]/div[1]/div[1]/div/div[3]/button[2]').click() # 경력창 닫기
    else:
        #print(str(i)+'년 차다')
        browser.find_element_by_xpath('//*[@id="btn_check_career_over'+str(i)+'"]').click()
        browser.find_element_by_xpath('//*[@id="btn_check_career_over0"]').click()
        browser.find_element_by_xpath('//*[@id="sp_main_wrapper"]/div[1]/div[1]/div/div[3]/button[2]').click() # 경력창 닫기
    for a in range(1,5):
        for b in range(1,6):
            if a==3 and b>=4:
                continue
            com_cnt+=1
            browser.find_element_by_xpath('//*[@id="sp_company_type"]/div/div['+str(a)+']/ul/li['+str(b)+']/span/label').click() # 기업 선택
            time.sleep(2)
            browser.implicitly_wait(2)
            html = browser.page_source
            soup = BeautifulSoup(html, "lxml")
            text=soup.select('span.count > b')[0].get_text()
            #print(text)
            print([career[car_cnt],company[com_cnt],str(text)])
            wr.writerow([career[car_cnt],company[com_cnt],str(text)])
            browser.find_element_by_xpath('//*[@id="sp_company_type"]/div/div[6]/button[1]').click() # 초기화
    com_cnt=-1
f.close()
    