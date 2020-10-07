odd=[1,3,5,7]
list=[1,2,[1,2,3,],[3,4,5]]#리스트 안의 리스트
print(odd[1])
odd[1]=2
print(odd[1])
print(odd[1]+odd[3])
print(odd[-1])
print(list[-1])
print(list[-1][0])#이중리스트 인덱싱
print(list[-1][1])
print(list[-1][2])
#삼중리스트 인덱싱
list=[[[1,2,3],[1,2,3],[1,2,3]],[["Life"],["is","short"]]]
print(list[-1][-1][-1])
#리스트의 슬라이싱
a=[1,2,3,4,5]
print(a[0:2])#문자열이랑 똑같네
#처음부터 1까지, 2부터 마지막까지 출력해봐라
print(a[:2]+a[2:])#print(리스트+문자열)이거 안돼 보니까 파이썬은 출력때 한 자료형만 써줘야하는 듯하고 그게아니라면 포매팅해줘야하는것같은데
print(a*2)
print(len(a))
#연산은 같은 형끼리만
print(a[2]+3)
a=["Life","is","too","short"]
print(a[1]+" not")
a[1]+=" not"
print(a)
del a[1]
print(a)
del a[:1]
print(a)
a.append("right?")
print(a)
a.append([["or","not"]])
print(a)
a=[1,2,5,3]
a.sort()
print(a)
a.reverse()
print(a)
print(a.index(2))#a.sort(), a.reverse()는 왜 그대로 출력하면 None일까
#print(a.index(0))#없으면 오류
#요소 삽입
a.insert(0,4)
print(a)
del a[0]#인덱스로 지우기
print(a)
a.remove(5)#요소로 지우기
print(a)
print(a.pop())
print(a)
a=[1,2,3,4,5]
print(a.pop(1))
print(a)
print(a.count(1))
b=[6,7,8,9]
a.extend(b)
print(a)
c=["ss","dd"]
a.extend(c)
print(a)