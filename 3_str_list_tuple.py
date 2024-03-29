# print(type('hello world'))      #str
# print(isinstance("83", str))    #true
# print(isinstance(83, str))      #false, int이기 때문

# #문자 자료형은 변경불가능한 객체이다
# sentence  = "system and control"
# print(sentence[1]) #y: 두번째 문자
# #문자 자료형은 시퀀스 자료형이다. 
# #시퀀스 자료형은 문자 자료형, 리스트, 튜플 자료형 등이 있다.

# #enter : \n
# #tab : \t
# print("hello,,,\n,,,\t bye")

# #문자열 형식지정, 형식화 구문
# # https://pyformat.info
# #format을 이용하여 자리 표시자를 값으로 대체
# print("{name}is {age} years old".format(name = "johnny", age = "28"))
# #8자 이상이 되도록 선행공백으로 문자열 채우기
# print("{item: >8}".format(item = 'johnny'))

# #f-문자열: format문자를 사용하지 않아도 됨
# batman = 10     #int
# catwoman = 23
# print(f"Batman has {batman} apples. Catwoman has {catwoman} apples. In total, {batman + catwoman} apples.")
# x=7.0
# print(f"class of x is {type(x)} and its value is {x}. The statement x is greater than 5 is {x>5}. ")

# #변수를 왜 이용할까?
# company_name = 'naver'
# ceo_name = 'johnny'
# age = 28
# print("the name of company is "+company_name+" and the CEO is "+ceo_name+" .")
# print("His age is "+str(age)+". ")

# #LIST(목록 자료형)
# #대괄호를 이용하여 사용가능
# list_ex = [3, 3.5, None, True, 'Hello']
# print(list_ex)
# print(isinstance(list_ex , list))

# x='hello'
# list_ex2 = [2<3 , x.capitalize(), 2**3, [1,2]]
# #대괄호 안의 연산이 완료된 상태로 프린트 됨
# print(list_ex2)
# print(list(x)) #sequence x 를 리스트로 만듦, 순서가 중요함을 알  수 있음
# y='ehllo'
# print(list(x)==list(y)) #False
# #인덱싱, 슬라이싱
# print(len(x) == len(y)) #True, 리스트의 크기 비교
# #인덱싱
# print(x[0])
# print(x[1])
# #슬라이싱
# print(x[0:3]) #0부터 3이전까지 가겠다. 즉, 0,1,2.

# #리스트는 변경 가능 한 객체.
# x = [1,2,3,4,5]
# x[1]  = 'apple'
# print(x)

# #append, extend
# #append: list 끝에 추가함
# x =[1,2,3,4,5]
# x.append("hello")
# print(x)
# #extend: list화 시킨 후 append 함
# x.extend('world') # = x.extend(list('world'))
# print(x)
# x.extend(['world']) # = x.append('world')
# print(x)

# #pop, remove
# #pop: 인덱스로 접근, 반환 후 삭제
# #remove: 해당 value(인덱스 아님)를 반환 없이 삭제
# x = [2,4,6,8]
# print(x)
# print(x.pop(1))
# print(x.remove(2))
# print(x)

# #시퀀스 예시 정리
# #list 
# x=[1,2,3]
# #문자열
# 'hello world'
# #tuple
# ('a', False, 0)
# #Numpy array
# x= numpy.ndarray([2,4]) 


# #튜플 / tuple
# x= ('a', False, 0, 2**3)
# y= (3,) #y = (3)는 tuple 이 아님.
# print(x)
# print(type(x))
# print(type(y))

# #list vs tuple
# #list 변경가능
# #tuple 변경불가

# x= [1, 'develop', None]
# y= (1, 'develop', None)

# print(x[0:1])#슬라이싱 비교
# print(y[0:1])

# x[0] = True #변경 가능
# print(x)
# #y[0] = True #변경 불가

# #tuple 자료형 변화
# c = 'apple'
# print(tuple(x))
# print(tuple(c))

#객체가 시퀀스 안에 있는지 확인하는 방법: obj in seq
x = [1,2,'a']
y = (1,2,'a')
z = 'apple'
print(z)
print(tuple(z))

print('a' in x) #True
print('a' in y) #True
print('a' in z) #True

#시퀀스 합치기
x = (1,2,'a')
y = (2,3,5)
z = x + y
print(z)

#시퀀스 슬라이싱
x = 'abcdefg'
print(x[0:3]) #x[0,1,2]
#인덱스 지정
print(x[0:3:1]) #x[0,1,2]
print(x[1:4:2]) #stepsize:2
print(x[:])
print(x[::2])
print(x[::-1]) #역순으로 출력, 음수는 끝부터 카운트
print(x[-2:])  #fg
print(x[:-2])  #abcde 