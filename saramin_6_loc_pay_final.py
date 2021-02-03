from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request
import time
import csv
f = open('c:\\data\\saram902.csv','w', newline='')
wr = csv.writer(f)
wr.writerow(['지역','연봉','기업수'])
com_cnt=-1
pay_cnt=-1
loc_cnt=-1
binary = 'C:\chromedriver\chromedriver.exe'
browser = webdriver.Chrome(binary)
browser.get("http://www.saramin.co.kr/zf_user/search?search_area=main&search_done=y&search_optional_item=n&searchType=default_mysearch&searchword=%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EB%B6%84%EC%84%9D")
browser.maximize_window()
time.sleep(3)
browser.implicitly_wait(3)
loc=[]
for i in range(51):
    loc.append(i)
pay=['2400만 이상','2600만 이상','2800만 이상','3000만 이상','3200만 이상','3400만 이상','3600만 이상','3800만 이상','4000만 이상','5000만 이상','6000만 이상','7000만 이상','8000만 이상']
for i in range(3):
    if i==0: # 서울
        code='seoul-'
        for j in range(2,27):
            loc_cnt+=1
            browser.find_element_by_xpath('//*[@id="sp_main_wrapper"]/div[2]/ul/li[2]/button/span[1]').click() # 지역 선택 버튼
            if j==2:
                browser.find_element_by_xpath('//*[@id="sp_main_wrapper"]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div/div/button[1]').click() # 지역 펼치기
            browser.find_element_by_xpath('//*[@id="depth1_btn_101000"]/button').click() # 서울 지역 선택
            browser.find_element_by_xpath('//*[@id="sp_main_wrapper"]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div/div/button[2]').click() # 서울 지역 선택
            browser.find_element_by_xpath('//*[@id="sp_area_lastDepth_101000"]/li['+str(j)+']/div/label').click() # 강남구 지역 선택
            browser.find_element_by_class_name('btn_detail_option').click() # 상세 조건 버튼
            for a in range(6,19):
                pay_cnt+=1
                browser.find_element_by_class_name('sri_select').click() # 연봉 체크박스 버튼
                browser.find_elements_by_class_name('link_opt')[a].click() # 체크박스 6번째 (2400만원)
                time.sleep(3)
                browser.implicitly_wait(3)
                html = browser.page_source
                soup = BeautifulSoup(html, "lxml")
                text=soup.select('span.count > b')[0].get_text()
                print([code+str(loc[loc_cnt]),pay[pay_cnt],str(text)])
                wr.writerow([code+str(loc[loc_cnt]),pay[pay_cnt],str(text)])
            pay_cnt=-1
    elif i==1: # 경기
        code='kyung-'
        loc_cnt=0 # 통일을 위해
        for j in range(2,53):
            loc_cnt+=1
            browser.find_element_by_xpath('//*[@id="sp_main_wrapper"]/div[2]/ul/li[2]/button/span[1]').click() # 지역 선택 버튼
            if j==2:
                browser.find_element_by_xpath('//*[@id="sp_area_lastDepth_101000"]/li[26]/div/label').click() # 마지막 서울 마지막 구 해제
            browser.find_element_by_xpath('//*[@id="depth1_btn_102000"]/button').click() # 경기 지역 선택
            browser.find_element_by_xpath('//*[@id="sp_main_wrapper"]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div/div/button[2]').click() # 지역 초기화
            browser.find_element_by_xpath('//*[@id="sp_area_lastDepth_102000"]/li['+str(j)+']/div/label').click() # 가평군 지역 선택
            browser.find_element_by_class_name('btn_detail_option').click() # 상세 조건 버튼
            for a in range(6,19):
                pay_cnt+=1
                browser.find_element_by_class_name('sri_select').click() # 연봉 체크박스 버튼
                browser.find_elements_by_class_name('link_opt')[a].click() # 체크박스 6번째 (2400만원)
                time.sleep(3)
                browser.implicitly_wait(3)
                html = browser.page_source
                soup = BeautifulSoup(html, "lxml")
                text=soup.select('span.count > b')[0].get_text()
                print([code+str(loc[loc_cnt]),pay[pay_cnt],str(text)])
                wr.writerow([code+str(loc[loc_cnt]),pay[pay_cnt],str(text)])
            pay_cnt=-1
            loc_cnt=-1
    elif i==2: # 인천
        code='incheon-'
        loc_cnt=0 # 통일을 위해
        for j in range(2,12):
            loc_cnt+=1
            browser.find_element_by_xpath('//*[@id="sp_main_wrapper"]/div[2]/ul/li[2]/button/span[1]').click() # 지역 선택 버튼
            if j==2:
                browser.find_element_by_xpath('//*[@id="sp_area_lastDepth_102000"]/li[52]/div/label').click()
            browser.find_element_by_xpath('//*[@id="depth1_btn_108000"]/button').click() # 인천 지역 선택
            browser.find_element_by_xpath('//*[@id="sp_main_wrapper"]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div/div/button[2]').click() # 지역 초기화
            browser.find_element_by_xpath('//*[@id="sp_area_lastDepth_108000"]/li['+str(j)+']/div/label').click() # 강화군 지역 선택
            browser.find_element_by_class_name('btn_detail_option').click() # 상세 조건 버튼
            for a in range(6,19):
                pay_cnt+=1
                browser.find_element_by_class_name('sri_select').click() # 연봉 체크박스 버튼
                browser.find_elements_by_class_name('link_opt')[a].click() # 체크박스 6번째 (2400만원)
                time.sleep(3)
                browser.implicitly_wait(3)
                html = browser.page_source
                soup = BeautifulSoup(html, "lxml")
                text=soup.select('span.count > b')[0].get_text()
                print([code+str(loc[loc_cnt]),pay[pay_cnt],str(text)])
                wr.writerow([code+str(loc[loc_cnt]),pay[pay_cnt],str(text)])
            pay_cnt=-1
            loc_cnt=-1
f.close()
    