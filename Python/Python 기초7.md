# Python 기초7

> 문제풀이

### 1. 솔로 천국 만들기

```python
'''
input : 연속된 숫자가 있는 list
output : 연속된 숫자는 하나만 남기고 제거한 list, 순서는 유지
'''
def lonely(nums):
    lonely_num = []
    # 새롭게 만들 리스트에 기존 리스트의 첫번째 숫자 추가
    lonely_num.append(nums.pop(0))
    
    # 기존 리스트에서 계속해서 숫자를 뽑으면서 그 전 숫자와 다르면 추가
    for i in range(len(nums)-1):
        pop = nums.pop(0)
        if lonely_num[-1] != pop:
            lonely_num.append(pop)
    
    return lonely_num

# 결과
print(lonely([4,4,4,3,3]))
print(lonely([1,1,3,3,0,1,1]))
>>>
[4, 3]
[1, 3, 0, 1]
```



### 2. 과목별 점수 총합 

- unpack * 은 list를 한 번 풀어준다.

```python
students = [
 [100, 80, 100],
 [90, 90, 60],
 [80, 80, 80]
]

# zip 이용
for scores in zip(*students):
    total = 0
    for score in scores:
        total += score   
    print(total)

# for만 이용
for i in range(len(students[0])):
    total = 0
    for scores in students:
        total += scores[i]    
    print(total)

# 결과    
>>>
270
250
240
    
    
```



