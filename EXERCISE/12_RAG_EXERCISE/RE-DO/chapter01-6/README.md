# chapter01-6: 메타데이터 (practice_metadata.ipynb)

## 리스트 컴프리헨션 vs 일반 for문

메타데이터 필터링 코드에 `for`가 두 번 나오지만, 둘은 서로 다른 문법이다.

```python
# ① 리스트 컴프리헨션
filtered_documents = [
    doc for doc in documents
    if doc.metadata.get('dept') == target_dept and doc.metadata.get('year') == target_year
]

# ② 일반 for문
for doc in filtered_documents:
    print(f"내용: {doc.page_content}")
    print(f"속성: {doc.metadata}")
```

### ① 리스트 컴프리헨션: 리스트를 **만드는** 문법

```python
[ doc   for doc in documents   if 조건 ]
#  ↑          ↑                   ↑
# 담을 값   어디서 꺼낼지        어떤 것만 남길지
```

- 결과로 **새 리스트**가 만들어진다. 그래서 `for` 앞에 **리스트에 담을 값**을 반드시 적는다.
- `doc for doc in documents`는 "꺼낸 doc을 **그대로** 리스트에 담아라"라는 뜻이다.
- 앞의 값을 바꾸면 담기는 값도 바뀐다.

```python
[doc.page_content for doc in documents]       # 본문 문자열만 담김
[doc.metadata['year'] for doc in documents]   # 연도만 담김 → [2024, 2026, 2026]
```

일반 for문으로 풀어 쓰면 다음과 같다.

```python
filtered_documents = []
for doc in documents:
    if doc.metadata.get('dept') == target_dept and doc.metadata.get('year') == target_year:
        filtered_documents.append(doc)   # ← 맨 앞의 doc이 이 append(doc) 역할
```

### ② 일반 for문: 하나씩 **실행만** 하는 문법

- 리스트를 만들지 않고, 각 요소마다 들여쓴 블록(`print` 등)을 실행한다.
- 담을 값이 없으므로 `for` 앞에 아무것도 오지 않는다.

### 정리

| | 리스트 컴프리헨션 | 일반 for문 |
|---|---|---|
| 형태 | `[값 for x in 리스트 if 조건]` | `for x in 리스트:` + 들여쓴 블록 |
| 목적 | 새 리스트를 **만들기** | 각 요소로 **동작 실행** |
| `for` 앞 | 담을 값 (필수) | 없음 |
