
# 예외처리
import byme
import datetime
import time
import os
import glob
from travel import *
from theater_module import price_soldier as price_s
from theater_module import price, price_morning
from theater_module import *
import theater_module as mv
import theater_module

try:
    print("나누기 전용 계산기이다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두번째 숫자를 입력하세요 : ")))
    nums.append(int(nums[0] / nums[1]))
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print("알 수 없는 에러가 발생하였습니다")
    print(err)


# 에러 발생시키기

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise ValueError
    print("{0} / {i} = {2}".format(num1, num2, int(num1/num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")


# 사용자 정의 예외처리
class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
    print("{0} / {i} = {2}".format(num1, num2, int(num1/num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
except BigNumberError as err:
    print("에러가 발생했습니다. 한 자리 숫자만 입력하세요.")
    print(err)
finally:
    print("계산기를 이용해 주셔서 감사합니다")    # 무조건 출력

# finally
# 프로그램 강조 종료를 막음 (완성도)

# Quiz) 치킨 자동 주문 시스템에 시스템 코드를 확인하고 적절한 예외처리 구문을 넣으시오
#
# 조건1 : 1보다 작거나 숫자가 아닌 입력값이 들엉올 때는 ValueError 로 처리
#         출력 메시지 : "잘못된 값을 입력하였습니다."
# 조건2 : 대기 손님이 주문할 수 있는 총 치킨량은 10마리로 한정
#         치킨 소진 시 사용자 정의 에러[SoldOutError]를 발생시키고 프로그램 종료
#         출력 메시지 : "재고가 소진되어 더 이상 주문을 받지 않습니다."

# [코드]


class SoldOutError(Exception):
    def __init__(self):
        pass


chicken = 10
waiting = 1

while(1):
    try:
        print("남은 치킨 : {0}".format(chicken))
        order = int(input("치킨 몇마리 주문하시겠습니까?"))

        if order > chicken:
            print("재료가 부족합니다.")
        elif order < 1:
            raise ValueError
        else:
            print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다."
                  .format(waiting, order))
            waiting += 1
            chicken -= order
            if chicken == 0:
                raise SoldOutError

    except ValueError:
        print("잘못된 값을 입력하였습니다.")

    except SoldOutError:
        print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
        break                                 # 무한루프 탈출하기


# 모듈
# : 확장자 .py 필요한 것들끼리(함수 정의 클래스 정의) 담은 라이브러리


theater_module.price(3)
theater_module.price_morning(4)
theater_module.price_soldier(5)


mv.price(2)
mv.price_morning(4)
mv.price_soldier(3)

price(4)
price_morning(2)
price_soldier(4)


price(5)
price_morning(6)
# price_soldier(7) import 가 되지 않아 사용할 수 없음

price_s(3)


# 패키지

# import travel.thailand
# # 클래스는 import 할 수 없다
# trip_to = travel.thailand.ThailandPackpage()
# trip_to.detail()
#
# from travel.thailand import  ThailandPackpage
# # 클래스, 함수까지 import 할 수 있다
# trip_to = ThailandPackpage()
# trip_to.detail()
#
# from travel.vietnam import Vietnamepackage
# trip_to = Vietnamepackage()
# trip_to.detail()
#
# #from random import *
# trip_to = vietnam.Vietnamepackage()
# #trip_to = thailand.ThailandPackage()
# trip_to.detail()


# 패키지, 모듈 위치 확인

# from travel import *
# import inspect
# import random
# print(inspect.getfile(random))
# print(inspect.getfile(thailand))


# pip install

# 내장함수
print(dir(list))

# 외장함수

# glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
print(glob.glob("*.py"))     # 확장자가 py인 모든 파일 경로 알려줘

# os : 운영체제에서 제공하는 기본 기능
print(os.getcwd())  # 현재 디렉토리

#
# folder = "sample_dir"
#
# if os.path.exists(folder):
#     print("이미 존재하는 폴더 입니다.")
#     os.rmdir(folder)
#     print(folder, "폴더를 삭제하였습니다.")
# else:
#     os.makedirs(folder)
#     print(folder, "폴더를 생성하였습니다.")
# print(os.listdir())

# time : 시간 관련 함수
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S"))

# datetime
print("오늘 날짜는 ", datetime.date.today())

# timedelta : 두 날짜 사이의 간격
today = datetime.date.today()    # 오늘 날짜 저장
td = datetime.timedelta(days=100)    # 오늘 날짜로부터 100일 뒤

print("우리가 만난지 100일은", today + td)


# Quiz) 프로젝트 내에 나만의 시그니처를 남기는 모듈을 만드시오

# 조건 : 모듈 파일명은 byme.py 로 작성

byme.sign()
