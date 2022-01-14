# 1. 모듈 불러오기
import random

# 2. 숫자 통 (1~45)
num_box = list(range(1, 46))
# print(num_box)

# 3. 숫자 통에서 6개를 sample
result = random.sample(num_box, 6)

# 4. 결과 출력
print(result)
