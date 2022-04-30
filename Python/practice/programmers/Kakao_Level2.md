## LEVEL2

> [프로그래머스-카카오](https://programmers.co.kr/learn/challenges)

### 주차 요금 계산

> import 하기 싫었는데 결국 math.ceil 써버림
>
> 다 풀고 다른사람 풀이들 보는데 변수명이 너무 비슷해서 사람 생각하는게 다 똑같구나 느낌

```python
import math
def solution(fees, records):
    answer = []
    inout = {}
    status = {}
    charges = {}
    for record in records:
        time, car, mode = record.split()
        if mode == 'IN':
            status[car] = time
        else:
            hour_pre, minute_pre = map(int, status[car].split(':'))
            hour_post, minute_post = map(int,time.split(':'))
            elapsed = (hour_post-hour_pre)*60 + (minute_post-minute_pre)
            charges[car] = charges.get(car, 0) + elapsed
        inout[car] = mode
            
    for car in status.keys():
        if inout[car] == 'IN':
            hour_pre, minute_pre = map(int, status[car].split(':'))
            elapsed = (23-hour_pre)*60 + (59-minute_pre)
            charges[car] = charges.get(car, 0) + elapsed
            
    
    for key in charges.keys():
        if charges[key] <= fees[0]:
            charges[key] = fees[1]
        else:
            charges[key] = fees[1] + math.ceil((charges[key] - fees[0]) / fees[2]) * fees[3]
    
    
    for car in sorted(charges):
        answer.append(charges[car])
            
    return answer
```

<br>



