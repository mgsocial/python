# 함수

def open_account():
    print("새로운 계좌가 생성되었습니다.")


open_account()


def deposit(balance, money):  # 입금 함수
    print("입금이 완료되었습니다. 잔액은 {0} 원립니다.".format(balance + money))
    return balance + money


def withdraw(balance, money):  # 출금 함수
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
        return balance


def withdraw_night(balance, money):  # 저녁에 출금 함수
    commission = 100
    return commission, balance - money - commission


balance = 0  # 잔액
balance = deposit(balance, 1000)
#balance = withdraw(balance, 200)
commission, balance = withdraw_night(balance, 500)
print("수수료 {0} 원이며, 잔액은 {1} 원입니다.".format(commission, balance))
print(balance)

# 기본값


# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}"
#           .format(name, age, main_lang))


# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")

# 같은 학교 같은 학년 같은 반 같은 수업.


# def profile(name, age=17, main_lang="파이썬"):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}"
#           .format(name, age, main_lang))


# profile("유재석")
# profile("김태호")

# 키워드값


# def profile(name, age, main_lang):
#     print(name, age, main_lang)


# profile(name="유재석", main_lang="파이썬", age=20)
# profile(main_lang="자바", age=25, name="김태호")

# 가변인자
# def profile(name, age, lan1, lan2, lan3, lan4, lan5):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
#     print(lan1, lan2, lan3, lan4, lan5)


def profile(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()


print("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
print("김태호", 25, "kotlin", "Swift")

# 지역변수와 전역변수
# 함수 호출에만 사용가능
# 모든 공간에서 부를 수 있는 변수로 구분함

gun = 10


def checkpoint(soldiers):  # 경계근무
    global gun
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))


print("전체 총 : {0}".format(gun))
checkpoint(2)  # 2명이 근무를 나감
print("남은 총 : {0}".format(gun))

gun = 10


def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun


print("전체 총 : {0}".format(gun))
gun = checkpoint_ret(gun, 2)  # 2명이 근무를 나감
print("남은 총 : {0}".format(gun))


# Quiz) 표준 체중을 구하는 프로그램을 작성하시오
# 표준 체중 : 각 키에 적당한 체중
"""
(성별에 따라)
남자 : 키 * 키 * 22
여자 : 키 * 키 * 21

조건1 : 표준 체중은 별도의 함수 내에서 계산
    * 함수명 : std_weight
    * 전달값 : 키(height), 성별(gender)
조건2 : 표준 체중은 소수점 둘째자리까지 표시

"""


def std_weight(height, gender="남자"):
    Global: gender
    if gender == "남자":
        n_weight = round(height/100 * height/100 * 22, 2)
    else:
        n_weight = round(height/100 * height/100 * 21, 2)
    print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, n_weight))


height = 175
gender = "여자"

std_weight(height, "남자")

####################


# def std_weight(height, gender):      # 키 m 단위, 성별 "남자"/"여자"
#     if gender == "남자":
#         return height * height * 22
#     else:
#         return height * height * 21


# height = 175
# gender = "남자"
# weight = round(std_weight(height / 100, gender), 2)
# print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))


# 표준입출력

print("Python", "Java", "JavaScript", sep=", ", end="?")
print("무엇이 더 재밌을까요?")

# import sys
# print("Python", "Java", file=sys.stdout)   #표준 출력
# print("Python", "Java", file=sys.stderr)   #표준 에러로 출력

scores = {'수학': 0, '영어': 50, '코딩': 100}
for subject, score in scores.items():
    #print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=':')      # 정렬해서 문자 출력!!!

# 은행 대기순번표
# 001, 002, 003, ...
for num in range(1, 21):
    print("대기번호 :" + str(num).zfill(3))

answer = input("아무 값이나 입력하세요 : ")     # input 값은 스트링(문자열) 변수로 받는다
print(type(answer))
print("입력하신 값은 " + answer + "입니다.")

# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, {총 10자리 공간}을 확
print("{0: >10}".format(500))

# 양수일 땐 +로 표시, 음수일 땐 -로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

# 왼쪽 정렬하고, 빈칸으로 _로 채움
print("{0:_<10}".format(500))

# 3자리 마다 콤마를 찍어주기
print("{0:,}".format(1000000000000))

# 3자리 마다 콤마를 찍어주기, +- 부호도 붙이기
print("{0:+,}".format(1000000000000))
print("{0:+,}".format(-1000000000000))

# 3자리 마다 콤마를 찍어주기, 부호도 붙이고, 자릿수 확보하기
# 돈이 많으면 행복하니까 빈 자리는 ^
# print("{0:<+,^10}".format(10000000000))
print("{0:^<+30,}".format(1000000000000))

# 소수점 출력
print("{0:f}".format(5/3))

# 소수점 특정 자리수 까지만 표시
print("{0:.2f}".format(5/3))
