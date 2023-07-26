# 입출력

for i in range(0,10):
    url = 'http://www.credu.com/?page='+str(i)
    print(url)

print('==== 오른쪽 정렬 ====')
for x in range(1,6):
    print(x,"*",x,'=',str(x*x).rjust(5))

print('==== 0 채우기 ====')
for x in range(1,6):
    print(x,'*',x,'=',str(x*x).zfill(5))

print('==== 서식지정 ====')
print('{0:x}\n{1:b}\n{2:,}\n{3:e}\n{4:f}\n{5:.2f}'.format(10,10,1500,4/3,4/3,4/3))

# 파일 쓰기
f = open('c:\\work\\demo.txt','wt',encoding='utf-8')
f.write('First\nSecond\nThird')
f.close()

# 파일읽기
f = open(r'c:\work\demo.txt','rt',encoding='utf-8')
result = f.read()
f.close()
print(result)

