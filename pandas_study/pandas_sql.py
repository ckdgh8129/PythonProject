from sqlalchemy import create_engine
import pandas as pd


# create_engine("mysql+pymsql://계정명 : 비번@ 주소:3306/db명")
eng = create_engine(
    "mysql+pymysql://ho:159123@localhost:3306/ho"
)

conn = eng.connect()
print("연결 성공")
conn.close()

query = "select * from item"
df = pd.read_sql(query, eng)
print(df)

# Database -> DataFrame -> 파일 저장
# 위 과정을 사용하는 경우 보고서 작성이나
# 다른 시스템에 데이터를 전달하기 위함

# 회사에서는 데이터 수집( 파일, 스크랩핑 등)
#-> DataFrame ->Database 위 과정으로 사용하는게 일반적이다.

# 카테고리별 수량
print(df['category'].value_counts())

# status 컬럼에서 sale 개수와 soldout 개수는?
print (df['status'].value_counts())

# status가 sale 인 총은 전체 몇개인가?
# print(df[
#         (df['status'] == 'sale') &
#         (df['category']=="총")].value_counts())

gun = df[ df['category']=="총"]
gun_cnt = gun['status'].value_counts()
print(gun_cnt['sale'])

# 문제 3 미사일 중에서 수량 (item_qa) 이 10 개 이상인
# 미사일의 이름을 출력하세요

m = df[(df['category'] == "미사일") &
       (df['item_qa'] >= 10)]['item_name']
print(m.to_string(index=False))
