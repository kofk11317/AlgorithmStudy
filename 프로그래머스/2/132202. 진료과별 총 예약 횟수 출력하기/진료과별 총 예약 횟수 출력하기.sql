-- 코드를 입력하세요
# DATETIME: 데이터베이스에 입력한 값과 동일한 형태로 저장됩니다. 즉, 입력한 날짜 및 시간 정보가 그대로 문자열로 저장됩니다. 

# TIMESTAMP: UTC를 기준으로 1970년 1월 1일 00:00:01부터 경과한 "초"가 숫자형으로 저장됩니다.
SELECT MCDP_CD as  '진료과코드' ,count(APNT_YMD) as  '5월예약건수'
from APPOINTMENT 
where APNT_YMD like "2022-05-%"
group by MCDP_CD # 진료과코드에서 로우별로 같은 이름을 가진애들끼리 모아줌
order by count(APNT_YMD) asc ,MCDP_CD asc
# SELECT
#     MCDP_CD as "진료과코드"
#     , count(APNT_NO) as "5월예약건수"
# from APPOINTMENT
# where APNT_YMD like "2022-05-%"
# group by MCDP_CD
# order by 2 asc, 1 asc