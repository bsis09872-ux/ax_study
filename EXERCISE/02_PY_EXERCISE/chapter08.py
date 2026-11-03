# 8장 1강 클래스(1)
# 1
# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author

#     def info(self):
#         print(f"책 제목: {self.title}, 저자: {self.author}")

# book1 = Book("시간을 달리네", "한로로")
# book2 = Book("안녕이라 그랬어", "김애란")

# book1.info()
# book2.info()

# print(f"book 1 메모리 주소: {id(book1)}")
# print(f"book 1 메모리 주소: {id(book2)}")

# 2
# class SmartLamp:
#     def __init__(self):
#         is_on = False

#     def turn_on(self, model):
#         is_on = True
#         print(f"{model} 조명이 켜졌습니다.")

#     def turn_off(self, model):
#         is_on = False
#         print(f"{model} 조명이 꺼졌습니다.")

# light = SmartLamp()

# light.turn_on('model001')
# light.turn_off('model001')

# 3
# class Hero:
#     def __init__(self, name):
#         self.name = name
#         self.hp = 100

#     def take_damage(self, name, damage):
                 
#                 print(f"데미지:{damage}hp")
#                 self.hp -= damage

#                 if self.hp > 0:
#                     print(f"HP:{self.hp}")

#                 else:
#                     print(f"{name} 캐릭터가 쓰러졌습니다.")

# hero1 = Hero('히어로')

# import random

# while hero1.hp > 0:
#     hero1.take_damage('히어로', random.randint(1,100))

# 8장 2강 상속과 캡슐화(1)

# 1
# class Phone:
#     def call(self):
#         print("통화를 시작합니다.")

# class SmartPhone(Phone):
#     def call(self):
#         print("영상 통화를 시작합니다.")

#     def search_web(self):
#         print("인터넷 검색을 시작합니다.")

# smartphone1= SmartPhone()

# smartphone1.call()
# smartphone1.search_web()

# 2
class DoorLock:
    def __init__(self, password = '0000'):
        password = str(password)
        self.validate_password(password)

        self.__password = password

    def get_password(self):
        return self.__password

    def set_password(self,new_pass):
        new_pass = str(new_pass)
        self.validate_password(new_pass)


        self.__password = new_pass
        print("정상 변경되었습니다.")

    def validate_password(self, new_pass):
        if len(new_pass) < 4:
            raise ValueError("경고: 비말번호는 4자리 이상이어야 합니다.")

           

dl = DoorLock(12)

print(dl.get_password())
dl.set_password('1')
print(dl.get_password())
dl.set_password('2')
print(dl.get_password())
dl.set_password('45678')
print(dl.get_password())

# 3
# class User:
#     def __init__(self,name):
#         self.name = name


# class VIPUser(User):
#     def __init__(self, name, point):
#         super().__init__(name)
#         self.point = point

# vip = VIPUser('이브이', 1000)

# print(vip.name)
# print(vip.point)


# 🔑 핵심
# 자식 클래스가 부모의 속성(name)을 초기화해야 하려면:

# 자식의 __init__에서 name을 매개변수로 받고
# super().__init__(name)으로 부모에게 전달해야 해요!

