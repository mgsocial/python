
# 자료형
from random import *
from math import *

print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3*(3+1))
print('풍선')
print("나비")
print('ㅋ'*9)
# 참/거짓
print(5 > 10)
print(5 < 10)
print(True)
print(False)
print(not True)  # not 반대
print(not (5 > 10))

# 변
# 애완동물을 소개해 주세요
animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3

'''
# print("우리집 강아지의 이름은 연탄이에요")
# print("연탄이는 4살이며, 산책을 좋아해요")
# print("연탄이는 어른일까요? True")
'''

print("우리집" + animal + "의 이름은" + name + "에요")
print(name + "는" + str(age) + "살이며, " + hobby + "을 좋아해요")
print(name, "는 어른일까요? ", str(is_adult))  # ,(콤마)가 들어가면 빈칸이 들어감

# Quiz) 변수를 이용하여 다음 문장을 출력하시

station = ["사당", "신도림", "인천공항"]

for i in station:
    print(i + "행 열차가 들어오고 있습니다.")


# 연산자
print(1+1)
print(3-2)
print(5*2)
print(6/3)

print(2**3)
print(5 % 2)  # 나머지 구하기
print(10 % 3)
print(5//3)  # 몫 구하기
print(10//3)

print(4 >= 7)
print(5 <= 5)

print(3 == 3)
print(4 != 2)
print(3 + 4 == 7)
print(1 != 3)  # 같지 않다
print(not(1 != 3))

print((3 > 0) and (3 < 5))
print((3 > 0) & (3 < 5))

print((3 > 0) or (3 > 5))
print((3 > 0) | (3 > 5))

print(5 > 4 > 3)
print(5 > 4 > 7)

print(2 + 3 * 4)
print((2 + 3) * 4)
number = 2 + 3 * 4
print(number)
number = number + 2
print(number)
number += 2
print(number)
number *= 2
print(number)
number /= 2
print(number)
number -= 2
print(number)
number %= 2
print(number)

# 숫지처리함수
print(abs(-5))
print(pow(4, 2))
print(max(5, 12))
print(min(5, 12))
print(round(3.14))
print(round(4.99))

# math 라이브러리
print(floor(4.99))
print(ceil(3.14))
print(sqrt(16))

# random 라이브러리

# print(random())  # 0.0 ~ 1.0 미만의 임의의 값 생성
# print(random() * 10) # 0.0 ~ 10.0 미만의 임의의 값 생성
# print(int(random() * 10))
# print(int(random() * 10))
# print(int(random() * 10))
# print(int(random() * 10) + 1)

print(int(random() * 45) + 1)
print(int(random() * 45) + 1)
print(int(random() * 45) + 1)
print(int(random() * 45) + 1)
print(int(random() * 45) + 1)
print(int(random() * 45) + 1)

print(randrange(1, 46))  # 1~46 미만의 임의의 값 생성

print(randint(1, 45))  # 1~45 이하의 임의의 값 생

# Quiz) 당신은 코딩 스터디 모임을 만들었습니다
# 월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했다
# 아래 조건에 맞는 오프라인 날짜를 정해주는 프로그램

# 조건 1 : 랜덤으로 날짜를 뽑아야 함
# 조건 2 : 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
# 조건 3 : 매월 1~3일은 스터디 준비를 해야 하므로 제외

print("오프라인 스터디 모임 날짜는 매월", randint(4, 28), "일로 선정되었습니다.")

date = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월 " + str(date) + "일로 선정되었습니다.")

# 문자열
sentence = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)

jumin = "990120-1234567"

print("성별 : " + jumin[7])
print("연 : " + jumin[:2])

print("생년월일 : " + jumin[:6])
print("뒤 7자리 : " + jumin[7:])
print("뒤 7자리 : " + jumin[-7:])

# 문자열 처리함수

python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index + 1)
print(index)

print(python.find("n"))
print(python.find("Java"))
# print(python.index("Java"))
print("hi")

print(python.count("n"))

# 문자열포맷
print("a" + "b")
print("a", "b")

# 방법 1
print("나는 %d살입니다." % 20)
print("나는 %s을 좋아해요." % "파이썬")
print("Apple 은 %c로 시작해요." % "A")

print("나는 %s살입니다." % 20)
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

# 방법 2
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age=20, color="빨간"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(color="빨간", age=20))

# 방법 4
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

# 탈출문자
print("백문이 불여일견 \n백견이 불여일타")  # 줄바꿈

print("저는 \"나도코딩\"입니다.")    # \
print('저는 \'나도코딩\'입니다.')    # \

print("\\Users\\billy\\Downloads")

print("Red Apple\rPine")  # 커서를 맨앞으로

print("Redd\bApple")  # 백스페이스 (한 글자 삭제)

print("Red\tApple")

# Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

# 예) http://naver.com
# 규칙1 : http:// 부분은 제외 => naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 "e" 갯수 + "!"로 구성

site = "http://naver.com"
password = site[7:site.index(".")][:3] + str(len(site[7:site.index(".")])
                                             ) + str(site[7:site.index(".")].count('e')) + "!"

print(password)

url = "http://naver.com"
url = "http://youtube.com"
my_str = url.replace("http://", "")  # 규칙1
my_str = my_str[:my_str.index(".")]
password = my_str[:3] + str(len(my_str)) + str(my_str.count('e')) + "!"
print(password)
print("{0}의 비밀번호는 {1} 입니다.".format(url, password))

# 리스트
subway = ["유재석", "조세호", "박명수"]
print(subway)
print(subway.index('조세호'))
subway.append("하하")
print(subway)
subway.insert(1, "정형돈")  # 집어넣기
print(subway)

print(subway.pop())  # 꺼내기
print(subway)

print(subway.append("유재석"))
print(subway.count("유재석"))

num_list = [5, 2, 3, 1, 6]
num_list.sort()
print(num_list)

num_list.reverse()
print(num_list)

num_list.clear()  # 모두 지우기
print(num_list)

num_list = [5, 2, 4, 3, 1]
mix_list = ["조세호", 20, True]
print(mix_list)

num_list.extend(mix_list)  # 확장
print(num_list)

# 딕셔너리
cabinet = {3: "유재석", 100: "김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
# print(cabinet[5])
print(cabinet.get(5))
print(cabinet.get(5, "사용 가능"))

print(3 in cabinet)
print(5 in cabinet)

cabinet = {"A-3": "유재석", "B-100": "김태호"}
print(cabinet["A-3"])

cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

del cabinet["A-3"]
print(cabinet)

print(cabinet.keys())
print(cabinet.values())
print(cabinet.items())  # 쌍으로 출력

cabinet.clear()
print(cabinet)

# 튜플
menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

# menu.add("생성까스")
print(menu)

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)

# 세트
# 중복 안됨, 순서 없음
my_set = {1, 2, 3, 3, 3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

print(java & python)  # 교집합
print(java.intersection(python))

print(java | python)  # 합집합
print(java.union(python))

print(java - python)  # 차집합
print(java.difference(python))

python.add("김태호")
print(python)

java.remove("김태호")
print(java)

# 자료구조의 변경
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))

# Quiz) 학교의 파이썬 코딩 대회를 주최합니다
# 참석률을 높이기 위해 댓글 이벤트 진행
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 구폰을 받게 됩니다
# 추첨 프로그램을 작성하시오

# 조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
# 조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
# 조건3 : random 모듈의 shuffle과 sample을 활용

apply = list(range(1, 21))
ck = apply[randint(1, 20)-1]
apply.remove(ck)
cf = sample(apply, 3)

print(f"""
\-\- 당첨자 발표 \-\-
치킨 당첨자 : {ck}
커피 당첨자 : {cf}
\-\- 축하합니다 \-\-
""")

lst = [1, 2, 3, 4, 5]
print(lst)
shuffle(lst)
print(lst)
print(sample(lst, 1))

users = list(range(1, 21))
shuffle(users)
print(users)

winners = sample(users, 4)
print(" -- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("-- 축하합니다 --")
