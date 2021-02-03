import mysql.connector
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

config = {
    "user": "root",
    "password": "1234",
    "host": "192.168.56.101", #local
    "database": "orcl", #Database name
    "port": "3306" #port는 최초 설치 시 입력한 값(기본값은 3306)
}

conn = mysql.connector.connect(**config)

# db select, insert, update, delete 작업 객체
cursor = conn.cursor()


# 실행할 select 문 구성
sql = """ select pay,cnt from car_pay3
            where career='7년차';
           """
           
# cursor 객체를 이용해서 수행한다.
cursor.execute(sql)

# select 된 결과 셋 얻어오기
resultList = cursor.fetchall()  # tuple 이 들어있는 list
df = pd.DataFrame(resultList)
df.columns = ['연봉', '기업 수']
#print(df)

plt.ylabel('기업 수')
plt.ylim(0,90)
plt.xticks(rotation=40)
sns.barplot(data=df,x="연봉",y="기업 수",ci=None).set_title("7년차 공고 현황")
#sns.lineplot(data=df,x="경력",y="기업 수",marker='o',linestyle='--',color='red',ci=None).set_title("우수기업 공고 현황")
plt.legend(bbox_to_anchor=(1.05,1),loc=2,borderaxespad=0.)
plt.show()