# 11장 2강 coroutine & async/await(1)

# 1 비동기 라면 조리 타이머 제작하기

# import asyncio

# async def cook_ramen(time):
#     print("라면 조리를 시작합니다.")
#     await asyncio.sleep(time)
#     print("라면 조리가 완료되었습니다.")


# asyncio.run(cook_ramen(3))

# 2 스마트폰 멀티미디어 파일 동시 다운로드 시스템

# import asyncio

# async def download_music(music_name, wait_seconds):
#     print(f"{music_name} 음원 다운로드를 시작합니다.")
#     await asyncio.sleep(wait_seconds)
#     print(f"{music_name} 음원 다운로드가 완료되었습니다.")

# async def main():
#     await asyncio.gather(
#         download_music("음악1", 2),
#         download_music("음악2", 4)
#     )


# asyncio.run(main())

# 3 온라인 쇼핑몰 비동기 배송 알림 문자 발송 서비스

# import asyncio, time

# async def send_notification(customer, seconds):
#     print(f"{customer}님께 문자를 발송합니다.")
#     await asyncio.sleep(seconds)
#     print(f"{customer}님께 문자가 전송되었습니다.")

# async def main():

#     start = time.time()

#     await asyncio.gather(
#         send_notification("고객A", 1),
#         send_notification("고객B", 3),
#         send_notification("고객C", 2)
#     )

#     end = time.time()

#     print(f"총 소요 시간: {end - start:.2f}초")

# asyncio.run(main())

# 11장 3강 비동기 태스크 동시 처리 및 실무 실습(1)

# 1 비동기  클라이언트를 활용한 단일 데이터 수집

# import httpx
# import asyncio

# async def fetch_todo():
#     async with httpx.AsyncClient() as client:
#         url = 'https://jsonplaceholder.typicode.com/todos/1'

#         res = await client.get(url)
#         result = res.json()

#         print (result['id'], result['title'])

# asyncio.run(fetch_todo())

# 2 asyncio.gather를 이용한 다중 데이터 동시 수집
# import asyncio

# todos = ['work01','work02', 'work03', 'work04', 'work05']

# async def fetch_todo_by_id(i):
#     todo = todos[i]
#     return todo

# async def main():
#     works = [fetch_todo_by_id(i) for i in range(5)]

#     results = await asyncio.gather(*works)

#     print(results)

# asyncio.run(main())

# 3 !!! 11장 3강 실습은 1번부터 이어지는거였음 !!!
import asyncio
import httpx

async def fetch_todo_by_id(i):
    async with httpx.AsyncClient() as client:
        try:
            url = f'https://jsonplaceholder.typicode.com/todos/{i}'

            res = await client.get(url)
            res.raise_for_status() 
        except httpx.HTTPError:
            return 999, "수집 에러 대체 데이터"
        
        result = res.json()
        
        return result['id'], result['title']

async def main():
    works = [fetch_todo_by_id(i) for i in range(1, 5)]
    works.append(fetch_todo_by_id(999))
    results = await asyncio.gather(*works)
    print(results)

asyncio.run(main())




