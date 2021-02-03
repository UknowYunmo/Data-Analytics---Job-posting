from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request
import time
import csv
f = open('c:\\data\\car_1.csv','w', newline='')
wr = csv.writer(f)
wr.writerow(['경력','기업형태','복리후생','기업수'])
car_cnt=-1
com_cnt=-1
wel_cnt=-1
binary = 'C:\chromedriver\chromedriver.exe'
browser = webdriver.Chrome(binary)
browser.get("http://www.saramin.co.kr/zf_user/search?search_area=main&search_done=y&search_optional_item=n&searchType=default_mysearch&searchword=%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EB%B6%84%EC%84%9D")
browser.maximize_window()
time.sleep(3)
browser.implicitly_wait(3)
browser.find_element_by_class_name('btn_detail_option').click() # 상세 조건 버튼
browser.find_element_by_xpath('//*[@id="sp_company_type"]/div/div[6]/button[2]').click() # 기업 펼치기
career=['1년차']
company=['대기업','매출1000대기업','중견기업','중소기업','스타트업','외국계(법인/투자)','금융기관','공기업','교육기관','수출입기업','코스닥','코스피','코넥스','벤처','강소기업','이노비즈','메인비즈','우수기업']
welfare=[]
for i in range(1,40):
    welfare.append(i)
for i in range(1): #13
    car_cnt+=1
    browser.find_element_by_class_name('btn_open_layer').click() # 경력 버튼
    if i==0:
        #print('신입이에용')
        browser.find_element_by_xpath('//*[@id="sp_main_wrapper"]/div[1]/div[1]/div/div[1]/div[1]/label').click() # 신입
        browser.find_element_by_xpath('//*[@id="sp_main_wrapper"]/div[1]/div[1]/div/div[1]/div[3]/label').click() # 무관
        browser.find_element_by_xpath('//*[@id="btn_check_career_over2"]').click()
        browser.find_element_by_xpath('//*[@id="btn_check_career_over0"]').click()
        browser.find_element_by_xpath('//*[@id="sp_main_wrapper"]/div[1]/div[1]/div/div[3]/button[2]').click() # 경력창 닫기
    for a in range(1,5):
        for b in range(1,6):
            if a==3 and b>=4:
                continue
            com_cnt+=1
            browser.find_element_by_xpath('//*[@id="sp_company_type"]/div/div['+str(a)+']/ul/li['+str(b)+']/span/label').click() # 기업 선택
            browser.find_element_by_class_name('btn_welfare').click() # 복리후생 선택
            for j in range(8):
                for k in range(1,34):
                    wel_cnt+=1
                    if j==0:
                        code='A'
                        if k>=23:
                            continue
                        browser.find_element_by_xpath('//*[@id="sp_welfare_layer"]/div[2]/table/tbody/tr[2]/td[1]/ul/li['+str(k)+']/span/label').click() #복리후생 체크
                    elif j==1:
                        code='B'
                        if k>=18:
                            continue
                        browser.find_element_by_xpath('//*[@id="sp_welfare_layer"]/div[2]/table/tbody/tr[2]/td[2]/ul/li['+str(k)+']/span/label').click() #복리후생 체크
                    elif j==2:
                        code='C'
                        if k>=11:
                            continue
                        browser.find_element_by_xpath('//*[@id="sp_welfare_layer"]/div[2]/table/tbody/tr[2]/td[3]/ul/li['+str(k)+']/span/label').click() #복리후생 체크
                    elif j==3:
                        code='D'
                        browser.find_element_by_xpath('//*[@id="sp_welfare_layer"]/div[2]/table/tbody/tr[2]/td[4]/ul/li['+str(k)+']/span/label').click() #복리후생 체크
                    elif j==4:
                        code='E'
                        if k>=31:
                            continue
                        browser.find_element_by_xpath('//*[@id="sp_welfare_layer"]/div[2]/table/tbody/tr[2]/td[5]/ul/li['+str(k)+']/span/label').click() #복리후생 체크
                    elif j==5:
                        code='F'
                        if k>=15:
                            continue
                        browser.find_element_by_xpath('//*[@id="sp_welfare_layer"]/div[2]/table/tbody/tr[4]/td[1]/ul/li['+str(k)+']/span/label').click() #복리후생 체크
                    elif j==6:
                        code='G'
                        if k>=21:
                            continue
                        browser.find_element_by_xpath('//*[@id="sp_welfare_layer"]/div[2]/table/tbody/tr[4]/td[2]/ul/li['+str(k)+']/span/label').click() #복리후생 체크
                    elif j==7:
                        code='H'
                        if k>=17:
                            continue
                        browser.find_element_by_xpath('//*[@id="sp_welfare_layer"]/div[2]/table/tbody/tr[4]/td[3]/ul/li['+str(k)+']/span/label').click() #복리후생 체크
                    time.sleep(2)
                    browser.implicitly_wait(2)
                    html = browser.page_source
                    soup = BeautifulSoup(html, "lxml")
                    text=soup.select('span.count > b')[0].get_text()
                    #print(text)
                    print([career[car_cnt],company[com_cnt],code+str(welfare[wel_cnt]),str(text)])
                    wr.writerow([career[car_cnt],company[com_cnt],code+str(welfare[wel_cnt]),str(text)])
                    browser.find_element_by_xpath('//*[@id="sp_welfare_layer"]/div[1]/button').click()
                wel_cnt=-1
            browser.find_element_by_xpath('//*[@id="sp_welfare_layer"]/div[3]/button').click() # 복리후생 선택완료
            browser.find_element_by_xpath('//*[@id="sp_company_type"]/div/div[6]/button[1]').click() # 초기화
    com_cnt=-1
f.close()
    