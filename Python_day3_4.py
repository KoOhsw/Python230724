# Sqllite3 사용 - 메모리 DB
import os
import sqlite3

fpath = os.getcwd()
#print(fpath)

#연결객체 생성
con = sqlite3.connect(':memory:') #메모리 이용 DB연결

#커서객체 생성
cur = con.cursor()

#테이블 구조 생성
cur.execute('create table if not exists PhoneBook (id integer primary key autoincrement, name text, phoneNum text);')

#입력 파라미터 처리
#수기 입력
cur.execute('insert into PhoneBook (name,phoneNum) values ("홍길동", "010-1111");')

#변수로 입력
name = '전우치'
phoneNumber = '010-2222'
cur.execute('insert into PhoneBook (name,phoneNum) values (?, ?);',(name,phoneNumber))

#다중의 행을 입력
datalist = (('이순신', '010-3333'), ('박문수','010-4444'))
cur.executemany('insert into PhoneBook (name,phoneNum) values (?, ?);',datalist)


#검색구문
cur.execute('select * from PhoneBook;')
print('-- fetchone --')
print(cur.fetchone())

print('-- fetchmany --')
print(cur.fetchmany(2))

print('-- fetchall --')
cur.execute('select * from PhoneBook;')
print(cur.fetchall())

# for row in cur:
#     print(row)

