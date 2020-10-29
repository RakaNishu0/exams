# 021 문자열 인덱싱
# letters가 바인딩하는 문자열에서 첫번째와 세번째 문자를 출력하세요.
#
# >> letters = 'python'
# 실행 예
# p t
letters = 'python'
print(letters[0], letters[2])


# 022 문자열 슬라이싱
# 자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하세요.
#
# >> license_plate = "24가 2210"
# 실행 예: 2210
license_plate = "24가 2210"
print(license_plate[4:])


# 023 문자열 인덱싱
# 아래의 문자열에서 '홀' 만 출력하세요.
#
# >> string = "홀짝홀짝홀짝"
# 실행 예:
# 홀홀홀
string = "홀짝홀짝홀짝"
print(string[::2])      # [시작인덱스 : 끝인덱스 : 반복할 주기(오프셋)]
string = "1234567890"
print(string[::2])      # 홀수만 출력
print(string[1::2])     # 짝수만 출력


# 024 문자열 슬라이싱
# 문자열을 거꾸로 뒤집어 출력하세요.
#
# >> string = "PYTHON"
# 실행 예:
# NOHTYP
string = "PYTHON"
print(string[::-1])     # 처음부터 끝까지, 뒤에서부터 1자리마다 출력

# 025 문자열 치환
# 아래의 전화번호에서 하이푼 ('-')을 제거하고 출력하세요.
#
# >> phone_number = "010-1111-2222"
# 실행 예
# 010 1111 2222
phone_number = "010-1111-2222"
edit = phone_number.replace("-", " ")
print(edit)


# 026 문자열 다루기
# 25번 문제의 전화번호를 아래와 같이 모두 붙여 출력하세요.
#
# 실행 예
# 01011112222
phone_number = "010-1111-2222"
edit = phone_number.replace("-", "")
print(edit)


# 027 문자열 다루기
# url 에 저장된 웹 페이지 주소에서 도메인을 출력하세요.
#
# >> url = "http://sharebook.kr"
# 실행 예:
# kr
url = "http://sharebook.kr"
url1 = url.find(".")
print(url[url1 + 1:])
url2 = url.split(".")
print(url2[-1])


# 028 문자열은 immutable
# 아래 코드의 실행 결과를 예상해보세요.
#
# >> lang = 'python'
# >> lang[0] = 'P'
# >> print(lang)
lang = 'python'
# lang[0] = 'P'           # 문자열은 list가 아니기 때문에 변경/수정을 인덱스 넘버를 통해 할 수가 없다, replace()활용
print(lang)


# 029 replace 메서드
# 아래 문자열에서 소문자 'a'를 대문자 'A'로 변경하세요.
#
# >> string = 'abcdfe2a354a32a'
# 실행 예:
# Abcdfe2A354A32A
string = 'abcdfe2a354a32a'
string1 = string.replace("a", "A")
print(string1)

# 030 replace 메서드
# 아래 코드의 실행 결과를 예상해보세요.
#
# >> string = 'abcd'
# >> string.replace('b', 'B')
# >> print(string)
string = 'abcd'
string.replace('b', 'B')            # 문자열을 변경한 값이 저장될 변수가 없다. string 변수의 내용은 변하지 않았다.
print(string)
string = string.replace('c', 'CC')  # replace()의 결과값을 string 변수에 다시 집어넣기 때문에 내용이 달라졌다.
print(string)
