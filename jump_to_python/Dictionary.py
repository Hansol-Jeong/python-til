dic={'name':'pey', 'phone':'01026763987','birth':'1118'}
a={'a':[1,2,3]}
print(a['a'])
#딕셔너리 쌍 추가하기
a['b']=[2,4,5]
print(a)
#elrtusjfl dyth tkrwpgkrl
del a['b']
print(a)
#딕셔너리에서 Key 사용해 Value얻기
grade = {'pey':10, 'jully':99}
print(grade["pey"])
print(grade["jully"])
#중복된 Key값을 사용하면 한 쌍을 제외한 나머지 쌍은 모두 무시된다.
a={1:'A',1:'B'}
print(a)
#Key 에는 변하는 값을 넣을 수 없다. 때문에 리스트는 Key값에 오지 못하지만 튜플은 올 수 있다. 한번 해보자
#a={[1,2]:'A'}#응 잘가고
a={(1,2):'a'}
print(a[(1,2)])#잘 되는 것을 볼 수 있다.
#딕셔너리 함수
#Key 리스트 만들기
a={1:1, 2:2, 3:3}
b={1:1, 2:2, 4:4}
print(a.keys())#dict_keys객체를 반환해 준다면 하나 더만들면 곤란해지겟는데?
#print(a.keys()+b.keys())역시이건 안됨 dict객체가 두개가 되버리니까
print(b.keys())
