# 5-1 함수 정의와 매개변수

# 1
# def rent_book(user_name, book_title):
#     print(f"회원명:{user_name}"
#           ,"\n",f"책 제목: {book_title}",
#           "\n","[대여 완료]되었습니다.") #출력 값을 줄바꿈 하고 싶을때 어떻게 하나요?

# rent_book("홍길동", "파이썬 안내서")
# rent_book(book_title="데이터 구조", user_name= "이영희")

# 2
# def calculate_total(price, delivery_fee = 3000):
#     total_fee = price + delivery_fee
#     return f"{total_fee}", "결제가 완료되었습니다."

# price, message = calculate_total(25000,)
# print(price, message)

# 3 (심화)
# def get_total_and_average(*args):
#     if len(args) == 0:
#         return 0

#     total = sum(args)
#     mean = total / len(args)
#     return print(f"합계:{total}, 평균: {mean}")

# get_total_and_average(90, 85, 95)
# get_total_and_average(70, 80, 90, 100, 65)