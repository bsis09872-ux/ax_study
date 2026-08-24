# 4-1 조건문 (1)

#1
# current_temp = 22
# if current_temp >= 30:
#     print("폭염 주의보가 발령되었습니다.")
# else:
#     print("쾌적한 날씨입니다.")

#2
# weight = 10
# if weight >= 23:
#     print("대형 수하물 대상입니다. 추가 요금이 부과됩니다.")
# elif weight >= 15:
#     print("일반 위탁 수하물 대상입니다.")
# else:
#     print("무료 수하물 대상입니다.")

#3
# age = 7
# height = 160

# if age >= 12 and height >= 130:
#     print("탑승 가능합니다. 관리자 확인을 진행하십시오.")
# else:
#     print("탑승 요건을 만족하지 못했습니다.")


#---------------------
# 4-2 반복문 (1)

#1
# for i in range(1,5):
#     print(f"{i}번째 고객님입니다.")

#2
# battery = 80

# while battery <= 100:
#     print(f"현재 베터리: {battery}")

#     battery += 5

# 3 
# for floor in range(1,3):
#     for room in range(1,4):
#         print(f"{floor}층 {room}호")
        
# 4-3 종합 제어 실습 (1)
# order_database = [
#     {"name": "김철수", "completed": True, "price": 60000},
#     {"name": "이영희", "completed": False, "price": 35000},
#     {"name": "박민수", "completed": True, "price": 25000},
#     {"name": "최지영", "completed": True, "price": 85000},
#     {"name": "정성민", "completed": False, "price": 90000}
# ]

# highest_price = 0
# highest_number = 0

# for item in order_database:
#     if item["completed"] == True:
#         if item["price"] >= 50000:
#             highest_price += item["price"]
#             highest_number += 1
# print(f"우수 고객 주문 건수: {highest_number}건") 
# print(f"우수 고객 총 결제 금액: {highest_price}원")

#--------------------------- (2026-08-12 이어서)

# fruit_sweetness = [12.5, 14.2, 11.8, 10.5, 15.0, 13.6, 11.2, 14.8, 12.0, 13.1]

# highest_sweetness = fruit_sweetness[0]
# lowest_sweetness = fruit_sweetness[0]
# cumulated_sweetness =0

# for sweetness in fruit_sweetness:
#     if sweetness > highest_sweetness:
#         highest_sweetness = sweetness
#     else:
#         lowest_sweetness = sweetness

#     cumulated_sweetness += sweetness
#     total_count = len(fruit_sweetness)
#     avg_sweetness = cumulated_sweetness / total_count

# print(f"""최고 과일 당도: {highest_sweetness}
#         최저 과일 당도: {lowest_sweetness}
#         과일 평균 당도: {avg_sweetness}""")

# # 3

import random
numbers = random.randint(1,50)
try = 0

while True:
    if int(input()) < numbers:
        print("보물은 더 큰 숫자의 방에 있습니다.")
    int(input())
    try += 1