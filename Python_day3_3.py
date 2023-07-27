# Time 모듈
print('==== time 모듈 ====')
import time
#print(dir(time))
print(time.time())
print(time.gmtime())
print(time.localtime())


# DateTime 모듈
print('==== datetime 모듈 ====')
from datetime import * #모듈의 네임스페이스는 생략하고 가져온다 -> import time과 충돌하여 time이 다시 덮어써진다!
# print(dir())
d1 = date(2023,7,20)
print(d1)
d2 = date.today()
print(d2)
d3 = timedelta(days=100)
print(f'100일을 더하면 :{d2+d3}')
d4 = datetime.now()
print(d4)

# Random 모듈
print('==== random 모듈 ====')
import random
print(dir(random))
print(random.random())
print([random.randrange(20) for i in range(10)])
print(random.sample(range(20),5))

# 로또번호 만들기
print('==== 로또 번호만들기 ====')
lotto = list(range(1,46))
random.shuffle(lotto)
print(lotto[0:6])

# os 모듈
print('==== os.path 모듈 ====')
import os
#print(dir(os))
print(os.path.abspath('python.exe'))
#print(os.path.basename('c:\\python310\\python.exe'))
#if os.path.isfile('c:\\python310\\python.exe'):
#    print('파일있음')
#else :
#    print('파일없음')

print('운영체제 이름은 : ', os.name)
# print('환경변수 : ', os.environ)
# print(os.system('notepad.exe'))
print('현재폴더 :', os.getcwd())
os.chdir('..')
#os.chdir('c:\\work')

# glob 모듈
import glob
result = glob.glob('*.py')
print(result)

for item in glob.iglob('*.py'):
    print(item)

