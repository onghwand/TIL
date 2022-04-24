## LEVEL1

> [프로그래머스-카카오](https://programmers.co.kr/learn/challenges)

### 신고 결과 받기

> report 안에 중복되는 원소가 많은 줄 모르고 했다가 시간초과 나서 set으로 원소 줄이고 시작했더니 바로 pass

```python
def solution(id_list, report, k):
    
    N = len(id_list)
    person_id = {}
    for i in range(N):
        person_id[id_list[i]] = i 
        
    pairs = {}
    for pair in set(report):
        reporting, reported=pair.split()
        pairs[reported] = pairs.get(reported, []) + [reporting]
        
    cnt = [0]*N
    for p in pairs:
        if len(set(pairs[p])) >= k:
            for person in pairs[p]:
                cnt[person_id[person]] += 1
                
    return cnt
```

### 신규 아이디 추천

> 정규 표현식 쓰는 법 외워야겠다고 느낀 문제
>
> [정규 표현식](https://wikidocs.net/4308)

```python
def solution(new_id):
    # 1
    new_id = new_id.lower()
    # 2
    answer = ''
    for a in new_id:
        if a.isdigit() or a.isalpha() or a in ['-','_','.']:
            answer += a
    # 3
    new_id = ''
    for a in answer:
        if len(new_id)>=1 and new_id[-1] == '.' and a == '.':
            continue
        else:
            new_id += a
    # 4
    new_id = new_id.strip('.')
    # 5
    if len(new_id) == 0:
        new_id = 'a'
    # 6
    elif len(new_id) >= 16:
        new_id = new_id[:15]
        new_id = new_id.rstrip('.')
    # 7  
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[-1]

    return new_id
```

> 다른 사람 풀이

```python
import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st
```

