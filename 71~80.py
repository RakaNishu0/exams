# 071
# my_variable 이름의 비어있는 튜플을 만들라.
my_variable = ()
print(type(my_variable))

# 072
# 2016년 11월 영화 예매 순위 기준 top3는 다음과 같다. 영화 제목을 movie_rank 이름의 튜플에 저장하라. (순위 정보는 저장하지 않는다.)
#
# 순위	영화
# 1	닥터 스트레인지
# 2	스플릿
# 3	럭키
movie_rank = ("Strange", "Split", "Lucky")
print(movie_rank)

# 073
# 숫자 1 이 저장된 튜플을 생성하라.
#
tpl = (1)
print(type(tpl))            # (1) 은 튜플이 아니라 정수(int)로 인식한다.
tpl = (1, )
print(type(tpl))            # 이를 튜플로 만들어주려면 , 를 찍어줘야 함.

# 074
# 다음 코드를 실행해보고 오류가 발생하는 원인을 설명하라.
#
# >> t = (1, 2, 3)
# >> t[0] = 'a'
# Traceback (most recent call last):
#   File "<pyshell#46>", line 1, in <module>
#     t[0] = 'a'
# TypeError: 'tuple' object does not support item assignment
t = (1, 2, 3)
# t[0] = 'a'        # 튜플은 아이템을 추가하거나 삭제할 수 없는 자료형이다.


# 075
# 아래와 같이 t에는 1, 2, 3, 4 데이터가 바인딩되어 있다. t가 바인딩하는 데이터 타입은 무엇인가?
#
t = 1, 2, 3, 4          # 튜플은 편의성을 위해 괄호를 생략하여도 사용할 수 있다고 한다.
print(type(t))


# 076
# 변수 t에는 아래와 같은 값이 저장되어 있다. 변수 t가 ('A', 'b', 'c') 튜플을 가리키도록 수정 하라.
#
t = ('a', 'b', 'c')             # 튜플은 element(원소)의 값을 변경하거나 추가, 삭제할 수 없다.
print(t)
t = ('A', 'B', 'c')             # 새로운 튜플을 정의하면 기존의 튜플을 대체한다.
print(t)

# 077
# 다음 튜플을 리스트로 변환하라.
#
interest = ('삼성전자', 'LG전자', 'SK Hynix')
lst = list(interest)            # 튜플을 리스트로 변환한 것을 넣어줄 변수가 필요하다. list() 로 감싼다고 바로 데이터타입이 변화되지 않는다.
print(lst, type(lst))
print(interest, type(interest))

# 078
# 다음 리스트를 튜플로 변경하라.
#
interest = ['삼성전자', 'LG전자', 'SK Hynix']
data = tuple(interest)
print(data, type(data))


# 079 튜플 언팩킹
# 다음 코드의 실행 결과를 예상하라.
#
temp = ('apple', 'banana', 'cake')
a, b, c = temp              # 튜플은 복수의 변수에 복수의 데이터를 동시에 할당할 수 있다.
print(a, b, c)


# 080 range 함수
# 1 부터 99까지의 정수 중 짝수만 저장된 튜플을 생성하라.
#
# (2, 4, 6, 8 ... 98)
data_tpl = tuple(range(2, 99, 2))       # range('start', 'stop', 'step')
data_lst = list(range(2, 99, 2))        # 범위만큼의 정수를 생성한다.
data_set = set(range(2, 99, 2))         # 리스트/튜플/집합 등의 데이터를 생성하거나, 해당 자료형 내의 데이터를 호출할 수 있다.
print(data_tpl)
print(data_set)
print(data_lst)
