# menu_name = 'Americano'
# menu_price = 4500

# message = "상품: %s | 가격: %d원" % (menu_name, menu_price)
# print(message)
# print(f"f-string => 상품: {menu_name}| 가격: {menu_price}원")

# price = 15000
# price_memo = f"금액: {price:8,}원"
# print(price_memo)

# current_status = '정산 진행중'
# price = 6500

# print(f"디버깅 로그 -> {current_status=} ; {price=}")


# --------------------------------------------------
# <추가 설명>
#  
# f-string의 디버깅 조절자(=) 설명
# f-string 중괄호 안에서 변수명 뒤에 등호(=)를 붙이면, 변수의 이름과 값을 동시에 출력하는 기능입니다.
# 코드를 디버깅할 때 변수 이름을 일일이 적지 않아도 어떤 변수가 어떤 값을 가지는지 한눈에 알 수 있어요.

# current_status = '정산 진행중'
# price = 6500

# # = 없이 일반 출력
# print(f"디버깅 로그 -> {current_status} ; {price}")
# # 결과: 디버깅 로그 -> 정산 진행중 ; 6500

# # = 있는 디버깅 조절자 (여러분 코드)
# print(f"디버깅 로그 -> {current_status=} ; {price=}")
# # 결과: 디버깅 로그 -> current_status='정산 진행중' ; price=6500
