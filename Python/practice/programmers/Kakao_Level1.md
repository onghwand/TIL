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

