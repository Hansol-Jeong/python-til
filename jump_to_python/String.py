#문자열을 만드는 방법은 총 4가지
"~"
'~'
"""~"""
'''~''' #다 이유가 있다
#python's favorite food is perl
"python's favorite food is perl"
#'python's favorite food is perl' 안됨
"""python's favorite food is prel"""
'''python's favorite food is prel'''
#"python is very easy." he says.
#""python is very easy." he says." 안됨
'"python is very easy." he says.'
'''"python is very easy." he says.'''
""""python is very easy." he sasy."""
#이렇게 상황별 용도가 있다. 또는 \를 이용할 수도 있다.
print('python\'s favorite food is perl')
#pytnon\'s favorite food is perl
print('python\\\'s favorite food is perl')
#줄을 바꾸고 싶을 떈 \n
multiline = "Life is too short\n You need python"
print(multiline)#읽기 불편하고 줄이 길어진다.
multiline='''
Life is too shourt
You need python
'''
print(multiline)
#문자열 더해서 출력하기
head='python'
tail=' is fun!'
print(head+tail)
#문자열 곱하기
print((head+" ") *2)
print("="*50)
print("My program")
print("="*50)
#문자열 길이 구하기
print(len(multiline))
#문자열 인덱싱
print(multiline[3])
print(multiline[-1])#얜 왜안나와?
multiline="abc"
print(multiline[-1])
print(multiline[0:3])
print(multiline[0:])
print(multiline[:3])
print(multiline[:])
print(multiline[0:-1])
#날짜 구하기
a="20201005Rainy"
date=a[:8]
weather=a[8:]
print(date+" "+weather)
#또는
year=a[:4]
day=a[4:8]
weather=a[8:]
print(year+" "+day+" "+ weather)
#문자열 수정 10월05일이 아니라 10월 04일로 만들고 싶다
#day[-1]='4'이거 안돼 문자열은 바꿀 수 있는 자료형이 아니기 때문
day=day[:3]+'4'
print(day)
#문자열 포매팅
a= "I ate %d apples" %3
print(a)
a= "I ate %s apples" %"three"
print(a)
number =3
a= "I ate %d apples" %number
print(a)
day= 10
a= "I ate %d apples. so I was sick for %s days" %(number, day)
print(a)
#%d와 %가 같은 문자열에 존재 할 경우 %를 나타내려면 반드시 %%로 표현해야 한다.
"""a="%d%" %98
print(a)"""#요거 안돼
a="%d%%" %98
print(a)
#공백 만들기
a="%10s" %"hi"
print(a)
a="%-10sJane"%"hi"
print(a)
#소수점 표현하기
a=3.141592
b="%0.4f" %a
print(b)#자동 반올림되네
a-=0.00005
b="%0.4f" %a
print(b)
b="%10.4s" %a#알아서 문자열로 바뀌고 소수점 표현까지 해주네 그럼 다른포맷형 필요 없지않냐
print(b)
a=12345.1235
b="%3.3f" %a #정수자리가 부족하면 알아서 확장한다.(전체길이 3)
print(b)
#근데 쓰면서도 이걸 어캐 일일이해 하는 생각이 들었어 그래서 더 발전된 버전이 있대.
a="I ate {0} apples".format("five")
print(a)
a="I ate {0} apples".format(number)
print(a)
#한번 포맷함수로 초기화 하면 다시 초기화 할 수 없다.
a="I ate {0} apples. so i sick for {1} days".format(number, day)
print(a)
a="I ate {1} apples. so i sick for {0} days".format(number, day)
print(a)
a="I ate {number} apples. so i sick for {day} days".format(number=1, day=2)
print(a)
print(number)# 위에있는 number와 여기 number는 다른 number네
#인덱스와 이름을 혼용해서 넣기
a="I ate {0} apples.so I sick for {day} days. at {1}day".format(10,2,day=20)
print(a)
"""a="I ate {0} apples.so I sick for {day} days. at {1}day".format(10,day=20,2)
print(a)"""#이거 안돼 이름 변수 쓸거면 순서 변수 다 끝내고 써줘야돼
#왼쪽 정렬
a="{:<10}".format("hi")#처음부터, 왼쪽정렬, 10자리
print(a)
a="{0:>10}".format("hi")#처음부터, 오른쪽정렬, 10자리
print(a)
a="{:^10}".format("hi")#처음부터, 가운데정렬, 10자리
print(a)# EEEEhiEEEE
a="{:^9}".format("hi")#처음부터, 가운데정렬, 9자리
print(a)# ###hi#### 가운데에서 어긋나면 앞에서 채운다
#공백 채우기
a="{:!<10}".format("hi") #처음부터, !로 채우고, 왼쪽정렬, 10자리
print(a)
a="{:=^10}".format("hi") #처음부터, =로 채우고, 가운데 정렬, 10자리
print(a)
#소수점 표현하기
a="{:<3.3f}".format(1234.1234)#처음부터, 왼쪽정렬, 총 3자리, 소수점 이하 3자리, 부족한 자리 알아서 채움
print(a)
a="{:=^20.3f}".format(1234.1234)#처음부터, =로 채우고, 가운데정렬, 총 20자리, 소수점이하 3자리
print(a)
a="{{and}}".format()
print(a)
#생각해보자 {and}를 쓰고싶어 그러면 포맷을 해야돼 근데 포맷할건 없어 그니까 {{and}}.format()해서 {and}를 아무것도 포멧 안한다 뭐 글케되나바 그냥 그렇대 그냥 헷갈리는거 쓰고싶으면 두번쓰면 되나봄
#f 문자열 포매팅
a="나의 이름은 {name}입니다. 나이는 {age}입니다.".format(name="홍길동",age=123)
print(a)
#이렇게 안하고
name="홍길동"
age=123
a=f"나의 이름은 {name}입니다. 나이는 {age}입니다."
print(a)
#f문자열 포매팅은 표현식을 지원한다.
a=f"나의 이름은 {name}입니다. 나이는 {age+1}입니다."
print(a)
#딕셔너리 f포매팅 활용
d={"name":"홍길동", "age":30}
print(f"""나의 이름은 {d["name"]}입니다. 나이는 {d["age"]+1}입니다.""")
#f문자열 포매팅 정렬
a=f"{'hi':<10}"#hi를 처음부터, 왼쪽정렬, 10자리
print(a)
a=f'{"hi":>10}'#hi를 처음부터, 오른쪽 정렬, 10자리
print(a)
a=f'{"hi":^10}'#hi를 처음부터, 가운데 정렬, 10자리
print(a)
#f문자열 포매팅 공백 채우기
a=f'{"hi":=^10}'#처음부터, =로 채우고, hi를 가운데 정렬, 10자리
print(a)
#소수점 표현
a=f'{1234.1234:=^30.3f}'#처음부터 =로 채우고, 1234.1234를 가운데정렬, 총 30자리, 소숫점 이하 3자리 까지 근데 왜 빨간색이지
print(a)
#{}표현
a=f'{{and}}'
print(a)
#.format의 변수는  로컬 변수였는데 f문자열의 변수는 로컬변수를 쓰지 않음 다른데서 변수를 참조해 올 수 있다는게 차이점
#문자열 관련함수 count, find, index, join, upper, lower, lstrip, rstrip, strip, replace, split
a="hobby"
print(len(a))
print(a.count('b'))
print(a.find("b"))#처음 나온 b의 위치
print(a.find('x'))#존재하지 않으면 -1
print(a.index('b'))#find 랑 다 똑같지만
#print(a.index('x')#다른점은 find는 없는 문자 찾으면 -1 반환하지만 얘는 오류발생시켜서 중지됨
print(",".join(a))#해당 문자열에 삽입
print(a.upper())
a="HOBBY"
print(a.lower())
#왼쪽 공백 지우기
a="    hi"
print(a.lstrip())
#오른쪽
a="hi      "
print(a.rstrip())
#양쪽
a= "  hi  "
print(a.strip())
#문자열 바꾸기
a="Life is too short"
print(a.replace("Life", "Y0ur leg"))
#문자열 나누기
a="Life is to short"
print(a.split())
print(a.split(" "))
a="A:B:C:D"
print(a.split(":"))