#튜플의 자료형
t1=()
t2=(1,)
t3=(1,2,3)
t4=1,2,3
t5=('a','b',('ab','cd'))
#튜우플은 몇 가지점을 제외하곤 리스트랑 같은 자료형이다. 일단 []대신에 ()을 쓰고, 튜플은 자료값을 바꿀 수 없다.
#한번 지워보자
#del t3[0]#역시나 오류가 생긴다.
#튜플의 요소값을 변경해보자
#t3[0]='c'#여쿠시나 오류가 생긴다.
#튜플다루기-인덱싱하기, 슬라이싱하기
print(t3[:])
#튜플 더하기
print(t1+t2+t3)
#튜플 곱하기
print(t3*2)
#튜플 길이 구하기
print(len(t3))

#1,2,3이라는 튜플값에 4를 추가하여 1,2,3,4를 만들어 출력해보자-이 의미가 튜플에 넣으라는 소린 아니겟지? 자료값을 바꿀수 없다햇잖아 출력만 그렇게 하면 되겟지
t6=(4,)
print(t3+t6)