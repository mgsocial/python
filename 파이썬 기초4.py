# 파일입출력
# score_file = open("score.txt", "w", encoding="utf8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8")
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

# 파일 읽기
from random import *
import pickle
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read())
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline(), end="")   # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline())
score_file.close()

# 읽어와야 하는 파일이 몇 줄인지 모를 때
score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end="")

score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines()   # list 형태로 저장
for line in lines:
    print(line, end="")

score_file.close()


# 피클
# pickle

profile_file = open("profile.pickle", "wb")
profile = {'이름': "박명수", "나이": 30, "취미": ["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile, profile_file)  # profile 에 있는 정보를 file 에 저장
profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file)   # file 에 있는 정보를 profile 에 불러오기
print(profile)
profile_file.close()

# with


with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))

with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())


# Quiz  매주 1회 보고서 작성

"""
- X 주차 주간보고 -
부서 :
이름 :
업무 요약 :
"""

# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램 작성
# 조건 : 파일명은 '1주차.txt', '2주차.txt', ... 와 같이 만든다

# for i in range(1,51):
#     with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
#         report_file.write("- {0} 주차 주간보고 -".format(i))
#         report_file.write("\n부서 :")
#         report_file.write("\n이름 :")
#         report_file.write("\n업무 요약 :")


# 클래스

# 마린
name = "마린"
hp = 40
damage = 5

print("{} 유닛이 생성되었습니다".format(name))
print("체력 {}, 공격력 {}\n". format(hp, damage))

tank_name = "탱크"
tank_hp = 150
tank_damage = 35

print("{} 유닛이 생성되었습니다".format(tank_name))
print("체력 {}, 공격력 {}\n". format(tank_hp, tank_damage))


def attack(name, location, damage):
    print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}".format(
        name, location, damage))


attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)

# 붕어빵은 틀이 있으면 무한정 만들 수 있음


class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성 되었습니다.".format(self.name))

    def move(self, location):
        print("[유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"
              .format(self.name, location, self.speed))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)

# 생성자 __init__

# 클래스로 만들어지는 변수 객체
# marine3 = Unit("마린", 40, 5)

# 멤버 변수 / 확장

# wraith1 = Unit("레이스", 80, 5)
# print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))
#
# wraith2 = Unit("레이스", 80, 5)
# wraith2.clocking = True

# if wraith2.clocking == True:
#     print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))


# class AttackUnit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage

#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]"
#               .format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))

# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")
#
# firebat1.damaged(25)
# firebat1.damaged(25)

# 상속


class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]"
              .format(self.name, location, self.damage))

# 마린


class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)

    # 스팀팩 : 일정 시간 동안 이동 및 공격 속도 증가
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))

# 탱크


class Tank(AttackUnit):
    # 시즈모드
    seize_developed = False

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return

        if self.seize_mode == False:
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.seize_mode = True

        else:
            print("{0} : 시즈모드로 해제합니다.".format(self.name))
            self.damage /= 2
            self.seize_mode = False


# firebat1 = AttackUnit("파이어뱃", 50, 0, 16)
# firebat1.attack("5시")
#
# firebat1.damaged(25)
# firebat1.damaged(25)


# 다중 상속

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed  # 초기화

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"
              .format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스


class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)  # 지상 speed 0
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[유닛 이동]")
        self.fly(self.name, location)

# 레이스


class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False

    def clocking(self):
        if self.clocked == True:
            print("{0} : 클로킹 모드 해체합니다.".format(self.name))
            self.clocked = False
        else:
            print("{0} : 클로킹 모드 설합니다.".format(self.name))
            self.clocked = True


def game_start():
    print("[알림] 새로운 게임을 시작합니다.")


def game_over():
    print("Player : gg")
    print("[Player] 님이 게임에서 퇴장하셨습니다")

# # 발키리 : 공중 공격 유닛
# valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
# valkyrie.fly(valkyrie.name, "3시")
#
#
# # 메소드 오버라이딩
#
# # 벌쳐 : 지상 유닛, 기동성이 좋음
# vulture = AttackUnit("벌쳐", 80, 10, 20)
#
# # 배틀크루저
# battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)
#
# vulture.move("11시")
# ##battlecruiser.fly(battlecruiser.name, "9시")
#
# # 똑같이 처리하도록
# battlecruiser.move("9시")


# pass

# 건물
# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         pass                                  #일단은 넘어간


# # 서플라이 디폿 : 1개 건물 = 8 유닛
# supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")다
#
# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")
#
# def game_start():
#     pass
#
# game_start()
# game_over()


# super

# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         #Unit.__init__(self, name, hp, 0)
#         super().__init__(name, hp, 0)             #super를 쓸 경우 self를 없이 사용
#         self.location = location

# 두개 이상의 부모클래스를 다중 상속 받을 경우 맨 마지막 클래스만 호출
# 두번을 통해서 초기화하는 방법 (해결)


# 스타크래프트 프로젝트
# 게임 진행
game_start()

m1 = Marine()
m2 = Marine()
m3 = Marine()

t1 = Tank()
t2 = Tank()

w1 = Wraith()

# 유닛 일괄 관리
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

# 전군 이동
for unit in attack_units:
    unit.move("1시")

# 탱크 시즈모드
Tank.seize_developed = True
print("[알림] 시즈 모드 개발 완료")

# 공격 모드 준비
for unit in attack_units:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()

# 전군 공격
for unit in attack_units:
    unit.attack("1시")

# 전군 피해
for unit in attack_units:
    unit.damaged(randint(5, 21))

# 게임 종료
game_over()


# Quiz) 주어진 코드를 활용하여 부동산 프로그램을 작성하시오

# (출력 예제)
# 총 3대의 매물이 있습니다.
# 강남 아파트 매물 10억 2010년
# 마포 오피스텔 전세 5억 2007년
# 송파 빌라 월세 500/50 2000년

# [코드]

class House:
    # 매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year
        #count += 1

    # 매물 정보 표시

    def show_detail(self):
        #print(f'총 {count}대의 매물이 있습니다')
        print(f'{self.location} {self.house_type} {self.deal_type} \
{self.price} {self.completion_year}')


houses = []
h1 = House("강남", "아파트", "매매", "10억", "2010년")
h2 = House("마포", "오피스텔", "전세", "5억", "2007년")
h3 = House("강남", "빌라", "월세", "500/50", "2000년")

houses.append(h1)
houses.append(h2)
houses.append(h3)

print("\n총 {0}대의 매물이 있습니다.".format(len(houses)))
for houses in houses:
    houses.show_detail()
