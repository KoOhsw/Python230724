# Sqllite3 사용
import sqlite3

#연결객체 생성
con = sqlite3.connect(':memory:')

#커서객체 생성
cur = con.cursor()

#테이블 구조 생성
cur.execute('create table if not exists PhoneBook (id integer primary key autoincrement, name text, phoneNum text);')

#입력
cur.execute('insert into PhoneBook (name,phoneNum) values ("홍길동", "010-1111");')

#검색구문
cur.execute('select * from PhoneBook;')

for row in cur:
    print(row)

