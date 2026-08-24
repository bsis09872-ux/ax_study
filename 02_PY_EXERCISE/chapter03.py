# 3-1 시퀀스 자료구조 (1)
# 문제 1-1: 과일 바구니 수정과 색상 추출

# fruits = ['apple', 'banana', 'cherry']
# fruits[1] = 'blueberry'
# print (fruits)

# colors = ('red', 'green', 'blue')
# print(colors[-1])

# 문제 2-1

# group1 = [1,2]
# group2 = [3,4]

# groups = group1+group2
# print(groups)

# user_roles = ['admin', 'editor', 'member']

# print('admin' in user_roles)

# 문제 3-1

# numbers = [0,1,2,3,4,5]
# print(numbers[1:4])

# numbers_10=[10,20,30,40]
# first, *others = numbers_10
# print(first)
# print(others)

# 3-2 매핑 및 집합 자료구조(1)
# 문제 1-1

# user_info = {'name': 'Sparta', 'age': 20}
# print(user_info)
# user_info['age'] = 21
# print(user_info)
# user_info['role'] = 'admin'
# print(user_info)

# print(user_info.get('phone','010-0000-0000'))

# 문제 2-1
# raw_emails = ["a@sparta.com", "b@sparta.com", "a@sparta.com"] 
# emails = set(raw_emails)
# refined_emails = list(emails)
# print(refined_emails)

# 문제 3-1
# menu = {'coffee':4000, 'tea': 4500}
# menu.keys()

# set_a = {1,2,3}
# set_b = {2,3,4}
# print("교집합:", set_a & set_b)
# print("합집합:", set_a | set_b)
# print("차집합:", set_a - set_b)
