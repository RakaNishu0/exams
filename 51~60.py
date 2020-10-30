# 051 리스트 생성
# 2016년 11월 영화 예매 순위 기준 top3는 다음과 같습니다. 영화 제목을 movie_rank 이름의 리스트에 저장해보세요. (순위 정보는 저장하지 않습니다.)
#
# 순위	영화
# 1	닥터 스트레인지
# 2	스플릿
# 3	럭키
movie_rank = ["Doctor Strange", "Split", "Lucky"]
print(movie_rank)

# 052 리스트에 원소 추가
# 051의 movie_rank 리스트에 "배트맨"을 추가하라.
movie_rank.append("BatMan")
print(movie_rank)

# 053
# movie_rank 리스트에는 아래와 같이 네 개의 영화 제목이 바인딩되어 있다. "슈퍼맨"을 "닥터 스트레인지"와 "스플릿" 사이에 추가하라.
# movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
movie_rank.insert(1, "SuperMan")
print(movie_rank)

# 054
# movie_rank 리스트에서 '럭키'를 삭제하라.
# movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']
movie_rank.remove("Lucky")
print(movie_rank)

# 055
# movie_rank 리스트에서 '스플릿' 과 '배트맨'을 를 삭제하라.
#
# movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']
movie_rank.remove("Split")      # split() 은 해당 데이터를 삭제하고
del movie_rank[2]               # del ~ [x] 는 인덱싱을 이용하여 삭제한다. 슬라이스 해서 ~까지, ~부터 등의 방법도 가능
print(movie_rank)

# 056
# lang1과 lang2 리스트가 있을 때 lang1과 lang2의 원소를 모두 갖고 있는 langs 리스트를 만들어라.
#
# >> lang1 = ["C", "C++", "JAVA"]
# >> lang2 = ["Python", "Go", "C#"]
# 실행 예:
# >> langs
# ['C', 'C++', 'JAVA', 'Python', 'Go', 'C#']
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs = lang1 + lang2
print(langs)

# 057
# 다음 리스트에서 최댓값과 최솟값을 출력하라. (힌트: min(), max() 함수 사용)
# nums = [1, 2, 3, 4, 5, 6, 7]
# 실행 예:
# max:  7
# min:  1
nums = [1, 2, 3, 4, 5, 6, 7]
print(f"max: {max(nums)}\nmin: {min(nums)}")


# 058
# 다음 리스트의 합을 출력하라.
# nums = [1, 2, 3, 4, 5]
# 실행 예:
# 15
nums = [1, 2, 3, 4, 5]
print(sum(nums))            # 리스트 데이터의 합을 구한다. 문자데이터가 있다면 에러를 반환한다.
print(sum(nums[:1]))        # 슬라이스 by index 도 가능
# print(sum(max(nums), min(nums)))        # 각각의 정수를 더하는 것은 불가. List 내의 데이터가 아니므로.
print(sum([max(nums), min(nums)]))      # 하지만, 각각의 정수를 List [ ] 로 묶어버리면 실행된다.

# 059
# 다음 리스트에 저장된 데이터의 개수를 화면에 구하하라.
#
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
print(len(cook))

# 060
# 다음 리스트의 평균을 출력하라.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 실행 예:
# 3.0
average = sum(nums) / len(nums)
print(f"평균 : {str(average)}")
