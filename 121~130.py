# 121
# 사용자로부터 문자 한 개를 입력 받고, 소문자일 경우 대문자로, 대문자 일 경우, 소문자로 변경해서 출력하라.
# 힌트-1 : islower() 함수는 문자의 소문자 여부를 판별합니다. 만약 소문자일 경우 True, 대문자일 경우 False를 반환합니다.
# 힌트-2 : upper() 함수는 대문자로, lower() 함수는 소문자로 변경합니다.
character = input("alphabet >> ")
if character.islower():
    print(character.upper())
else:
    print(character.lower())


# 122
# 점수 구간에 해당하는 학점이 아래와 같이 정의되어 있다. 사용자로부터 score를 입력받아 학점을 출력하라.
# 점수	학점
# 81~100	A
# 61~80	B
# 41~60	C
# 21~40	D
# 0~20	E
# >> score: 83
# grade is A
score = input("score : ")
if 81 < int(score) <= 100:
    print("A")
elif 61 < int(score) <= 80:
    print("B")
elif 41 < int(score) <= 60:
    print("C")
elif 21 < int(score) <= 40:
    print("D")
elif 0 < int(score) <= 20:
    print("E")
else:
    print("Insert Correct Score...")

# 123
# 사용자로부터 달러, 엔, 유로, 또는 위안 금액을 입력받은 후 이를 원으로 변환하는 프로그램을 작성하라.
# 각 통화별 환율은 다음과 같다. 사용자는 100 달러, 1000 엔, 13 유로, 100 위안과 같이
# 금액과 통화명 사이에 공백을 넣어 입력한다고 가정한다.
# 통화명	환율
# 달러	1167
# 엔	1.096
# 유로	1268
# 위안	171
# >> 입력: 100 달러
# 116700.00 원
money = {"달러": 1167, "엔": 1.096, "유로": 1268, "위안": 171}
inp_money = input("money? : ")
# count = int(inp_money.split(" ")[0])
# won = inp_money.split(" ")[1]
count, won = inp_money.split()
if won in money.keys():
    print(count * money[won], "원")

# 124
# 사용자로부터 세 개의 숫자를 입력 받은 후 가장 큰 숫자를 출력하라.
#
# >> input number1: 10
# >> input number2: 9
# >> input number3: 20
# 20
inp_num = int(input("1st num? : "))
inp_num2 = int(input("2nd num? : "))
inp_num3 = int(input("3rd num? : "))
print(max(inp_num, inp_num2, inp_num3))


# 125
# 휴대폰 번호 앞자리에 따라 통신사는 아래와 같이 구분된다. 사용자로부터 휴대전화 번호를 입력 받고, 통신사를 출력하는 프로그램을 작성하라.
#
# 번호	통신사
# 011	SKT
# 016	KT
# 019	LGU
# 010	알수없음
# >> 휴대전화 번호 입력: 011-345-1922
# 당신은 SKT 사용자입니다.
inp_num = input("phone num? : ")
lst = inp_num.split("-")
if lst[0] == "011":
    print("SKT")
elif lst[0] == "016":
    print("KT")
elif lst[0] == "019":
    print("LGU")
else:
    print("Unknown")


# 126
# 우편번호는 5자리로 구성되는데, 앞의 세자리는 구를 나타낸다. 예를들어, 강북구의 경우 010, 011, 012 세 자리로 시작한다.
# -	0	1	2	3	4	5	6	7	8	9
# 01	강북구	강북구	강북구	도봉구	도봉구	도봉구	노원구	노원구	노원구	노원구
# 사용자로 부터 5자리 우편번호를 입력받고 구를 판별하라
# >> 우편번호: 01400
# 도봉구
inp_num = input("mail num? : ")
mail_num = inp_num[:3]
if mail_num in ["010", "011", "012"]:
    print("강북")
elif mail_num in ["013", "014", "015"]:
    print("도봉")
elif mail_num in ["016", "017", "018", "019"]:
    print("노원")
else:
    print("Please insert correct number")


# 127
# 주민등록번호 뒷 자리 7자리 중 첫째 자리는 성별을 나타내는데, 1, 3은 남자 2, 4는 여자를 의미한다.
# 사용자로부터 13자리의 주민등록번호를 입력 받은 후 성별 (남자, 여자)를 출력하는 프로그램을 작성하라.
# >> 주민등록번호: 821010-1635210
# 남자
inp_num = input("id num? : ")
id_num = int(inp_num.split("-")[1][0])
if id_num in [1, 3]:
    print("Man")
elif id_num in [2, 4]:
    print("Woman")
else:
    print("Wrong nums")


# 128
# 주민등록번호의 뒷 자리 7자리 중 두번째와 세번째는 지역코드를 의미한다.
# 주민 등록 번호를 입력 받은 후 출생지가 서울인지 아닌지 판단하는 코드를 작성하라
# 지역코드	출생지
# 00 ~ 08	서울
# 09 ~ 12	부산
# >> 주민등록번호: 821010-1635210
# 서울이 아닙니다.
# >> 주민등록번호: 861010-1015210
# 서울 입니다.
inp_num = input("id num? : ")
id_num = int(inp_num.split("-")[1][1:3])
print(id_num, type(id_num))
if id_num <= 8:
    print("in Seoul")
else:
    print("non seoul")


# 129
# 주민등록번호는 13자리로 구성되는데 마지막 자리수는 주민등록번호의 유효성을 체크하는데 사용된다.
# 먼저 앞에서부터 12자리의 숫자에 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5를 차례로 곱한 뒤 그 값을 전부 더한다.
# 연산 결과 값을 11로 나누면 나머지가 나오는데 11에서 나머지를 뺀 값이 주민등록번호의 마지막 번호가 된다.
#   8 2 1 0 1 0 - 1 6 3 5 2 1 0
# x 2 3 4 5 6 7   8 9 2 3 4 5
# -----------------------------
# 1차 계산: (8*2 + 2*3 + 1*4 + 0*5 + 1*6 + 0*7 + 1*8 + 6*9 + 3*2 + 5*3 + 2*4 + 1*5) = (128 % 11) = 7
# 2차 계산: 11 -7 = 4
# 위와 같이 821010-1635210에 대해서 계산을 해보면 마지막 자리는 4가 되어야 함을 알 수 있다. 즉, 821010-1635210은 유효하지 않은 주민등록번호임을 알 수 있다.
# 다음과 같이 사용자로부터 주민등록번호를 입력받은 후 주민등록번호가 유효한지를 출력하는 프로그램을 작성하라.
# >> 주민등록번호: 821010-1635210
# 유효하지 않은 주민등록번호입니다.
num = "821010-1635210"
num = input("input id num : ")
num = num.replace("-", "")
i = 0
j = 0
# while i < 12:
for i in range(12):
    if i <= 7:
        num1 = int(num[i]) * (i + 2)
        # j = j + num1
    elif 8 <= i:
        num1 = int(num[i]) * (i - 6)
    j = j + num1

num2 = 11 - (j % 11)
if num2 == int(num[-1:]):
    print("correct")
else:
    print("Wrong")


# 130
# 아래 코드는 비트코인의 가격 정보를 딕셔너리로 가져오는 코드이다.
#
import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
# btc 딕셔너리 안에는 시가, 종가, 최고가, 최저가 등이 저장되어 있다.
# 최고가와 최저가의 차이를 변동폭으로 정의할 때 (시가 + 변동폭)이 최고가 보다 높을 경우 "상승장",
# 그렇지 않은 경우 "하락장" 문자열을 출력하라.
# Key Name	Description
# opening_price	최근 24시간 내 시작 거래금액 = 시가
# closing_price	최근 24시간 내 마지막 거래금액 = 종가
# min_price	최근 24시간 내 최저 거래금액
# max_price	최근 24시간 내 최고 거래금액
change = int(btc["max_price"]) - int(btc["min_price"])
if int(btc["max_price"]) < int(btc["opening_price"]) + change:
    print("High price")
else:
    print("Low price")
