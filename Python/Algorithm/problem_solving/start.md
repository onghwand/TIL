## 1242. 암호코드스캔

```python
#import sys
#sys.stdin = open('in1.txt')
nums = {'0001101': 0,
        '0011001': 1,
        '0010011': 2,
        '0111101': 3,
        '0100011': 4,
        '0110001': 5,
        '0101111': 6,
        '0111011': 7,
        '0110111': 8,
        '0001011': 9,
        }
def f():
    for l in range(M*4//56,-1,-1):  # 단위 길이 l, 가능한 큰 배율부터
        cnt = 0
        for k in range(4):  # 뒤에서부터 5개만 테스트, 배율로 잘랐는데 그 안이 다 같은 숫자면 배율일듯
            tmp = lst[i][j - l * (k + 1) + 1:j - l * k + 1]
            if tmp == ['0'] * l or tmp == ['1'] * l:
                cnt += 1
        if cnt == 4:
            return l
 
T = int(input())
for tc in range(1, T+1):
    N, M =map(int, input().split())
    arr = [input() for _ in range(N)]
    lst = [[] for _ in range(N)] #2진 변환후
 
    # 2진수로 변환해서 새로운 lst행렬 생성(N X 4M)
    for i in range(N):
        for j in range(M):
            lst[i].extend(list(bin(int(arr[i][j],16))[2:].zfill(4)))
 
    # 코드 추출
    codes = set()
    # while 1:
    #     tmp_cnt = len(codes)
    for i in range(N):
        for j in range(4*M-1, -1, -1):
            if lst[i][j] != '0':
                unit = f() # 배율 찾음
                codes.add(''.join(lst[i][j-unit*56+1:j+1:unit])) # 배율 압축해서 담고
                lst[i][j - unit * 56 + 1:j + 1] = ['0'] * 56 * unit
                    #break
        # if tmp_cnt == len(codes): # 다시 돌았는데 추가된게 없으면
        #     break
 
    # 찾은 코드 복호화
    ans=[] # 복호화된 수들
    for code in codes:
        decoded = ''
        for i in range(len(code)//7):
            if code[i*7:(i+1)*7] not in nums.keys():
                break
            decoded += str(nums[code[i*7:(i+1)*7]])
        ans.append(decoded)
 
    # 정상암호코드만 골라서 합
    final = 0
    for n in ans:
        total = 0
        for i in range(len(n)):
            if not i%2:
                total += int(n[i])*3
            else:
                total += int(n[i])
        if not total % 10:
            candi = sum(map(int, list(n)))
            final += candi
 
    print(f'#{tc} {final}')
```

## 5185. 이진수

```python
T = int(input())
for tc in range(1,T+1):
    N, n = input().split()
    s = ''
    for i in range(int(N)):
        s += format(int(n[i],16),'b')
    print(f'#{tc} {s}')
```

## 5186. 이진수2

```python
T = int(input())
for tc in range(1, T+1):
    N = float(input())
    ans = ['0']*13
    i=1
    total = 0
    while i < 13 :
        if abs(N - total) < 1e-13:
            break
        if total + 2**(-i) <= N:
            total += 2**(-i)
            ans[i] = '1'
        i += 1
    # while i < 13 and N > 1e-13:
    #     if N - 2 ** (-i) >= 0:
    #         N -= 2 ** (-i)
    #         ans[i] = '1'
    #     i+=1
    if i == 13 and N-total > 0:
        print(f'#{tc} overflow')
    else:
        print(f'#{tc}', ''.join(ans[1:i]))

```

