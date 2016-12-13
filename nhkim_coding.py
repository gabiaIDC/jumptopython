'''
    2016-12-09
    김남효 jumptopython 코딩 연습
'''
import sys

'''
print('hello world')

a=10
b=20
print(a+b)


# 집한 자료형 : 중복 허용 x, 순서가 없다.
s1 = set([1,2,3])
print(s1)

s2 = set("hello")
print(s2)



s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

print(s1&s2)
print(s1|s2)
print(s1.union(s2))

s1=set([1,2,3])
s2=s1.remove(2)
print(s2)

a = [1,2,3,4]
while a:
    print(a.pop())

if[1,2,3]:
    print("True")
else:
    print("False")

print(type(3))

print(sys.getrefcount(3))

a=3
b=3
print(a)
del(a)
del(b)
print(a)

x=3
y=2
print(x>y)

print('a' in ('a','b','c'))
'''
'''
함수
def 함수명(입력인수):
    수행할 문장1
    수행할 문장2


for i in range(10):
    print(i,end=' ')

'''
'''
f = open("C:/pytest/jumptopython/file.txt",'w')
for i in range(1,11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()
'''

f=open("C:/pytest/jumptopython/file.txt",'r')
while True:
    line=f.readline()
    if not line: break
    print(line)
f.close()

