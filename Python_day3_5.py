# Sqllite3 사용 - 실제 DB파일 만들기
import os
import sqlite3

fpath = os.path.join(os.getcwd(), 'day3_5.db')

# 연결객체 생성
con = sqlite3.connect(fpath)  # 실제 파일 DB 연결 (없으면 만들어줌)

# 커서객체 생성
cur = con.cursor()

# 테이블 구조 생성
cur.execute('create table if not exists PhoneBook (id integer primary key autoincrement, name text, phoneNum text);')

# 입력 파라미터 처리
# 수기 입력
cur.execute('insert into PhoneBook (name, phoneNum) values ("홍길동", "010-1111");')

# 변수로 입력
name = '전우치'
phoneNumber = '010-2222'
cur.execute('insert into PhoneBook (name, phoneNum) values (?, ?);', (name, phoneNumber))

# 다중의 행을 입력
datalist = (('이순신', '010-3333'), ('박문수', '010-4444'))
cur.executemany('insert into PhoneBook (name, phoneNum) values (?, ?);', datalist)

# 검색 구문
print('-- fetchall --')
cur.execute('select * from PhoneBook;')
print(cur.fetchall())

# 작업 완료
con.commit()
