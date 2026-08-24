# 5-2 변수 스코프와 람다 함수(1)

#1
# game_money = 7000

# def item_shop():
#     game_money = 300
#     print(f"게임머니_local: {game_money}")

# item_shop()
# print(f"게임머니_global: {game_money}")

# 2
# total_score = 0

# def add_score():
#     global total_score
#     total_score += 10

# add_score()
# add_score()

# print(total_score)

# 3
# base_numbers = [1,2,3,4,5,6]

# muliplied_nums = list(map(lambda x : x * 3, base_numbers))
# print(muliplied_nums)

# filtered_nums = list(filter(lambda x : x > 10, muliplied_nums))
# print(filtered_nums)

#----------------------------------------

# 5-3: 클로저와 데코레이터 (1)
# 1
# def message_store():
#     storage = str([])
#     def add_message(*message):
#         nonlocal storage

#         storage.append(" " + message)

#         return add_message

#     return message_store

# my_storage = ["새로운 알림이 도착했습니다.", "출석 체크가 완료되었습니다."]

# print (message_store(my_storage(0,1)))
# print (message_store(my_storage))

# def message_store():
#     storage = ""

#     def add_message(message):
#         nonlocal storage

#         try:
#             storage += message + "\n"
#         except ValueError:
#             print("문장으로 입력하세요.")

#         return storage

#     return add_message

# my_storage = message_store()
# print(my_storage("메세지1"))
# print(my_storage("메세지2"))

# 2
#  # 안내문구를 구분선 테두리로 감싸는 데코레이터
# def deco_border(feat_func):
#     def wrapper():
#         print("====================")
#         feat_func()
#         print("====================")
#     return wrapper

# @deco_border
# feat_func : 원본 함수
# def show_welcome():
#     print("환영합니다. 스파르타님")

#     return

# show_welcome()


# 3

# def auto_tracker(target_func):
#     def wrapper(*args,**kwargs):
#         print(f"{__name__} 함수가 실행되었습니다.")

#     return wrapper

# print(f"{args}, {kwargs}")

# auto_tracker()

#5-4

# 1
# plylst = ['song1','song2','song3']

# plylst.__iter__

# it = iter(plylst)

# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

# 2
# def positive ():
#     yield "대박"
#     yield "사건"
#     yield "성공"

# cheer = positive()
# print(next(cheer))
# print(next(cheer))
# print(next(cheer))

# 3
# import sys
# list_com = [ x ** 2 for x in range(0,500001)]
# gen = (x ** 2 for x in range(0,500001))

# print(sys.getsizeof(list_com))
# print(sys.getsizeof(gen))

def auto_tracker(callback):
    def wrapper(*args, **kwargs):
        print("함수 이름:" + callback.__name__)
        print(args)
        print(kwargs)
        result = callback(*args, **kwargs)

        print("종료!")

        return result


@auto_tracker
def add(num1, num2):
    return num1 + num2

result = add(10, 20)
print(f"반환된 결과: {result}")