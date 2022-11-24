## Level3

### 없어진 기록 찾기

```sql
-- 코드를 입력하세요
SELECT ANIMAL_OUTS.ANIMAL_ID, ANIMAL_OUTS.NAME
FROM ANIMAL_OUTS LEFT OUTER JOIN ANIMAL_INS ON ANIMAL_INS.ANIMAL_ID = ANIMAL_OUTS.ANIMAL_ID 
WHERE ANIMAL_INS.ANIMAL_ID IS NULL
```

### 있었는데요 없었습니다

```sql
-- 코드를 입력하세요
SELECT A.ANIMAL_ID, A.NAME
FROM ANIMAL_INS AS A JOIN ANIMAL_OUTS AS B ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE A.DATETIME > B.DATETIME
ORDER BY A.DATETIME
```

### 오랜 기간 보호한 동물(1)

```sql
-- 코드를 입력하세요
SELECT I.NAME, I.DATETIME
FROM ANIMAL_INS AS I LEFT OUTER JOIN ANIMAL_OUTS AS O ON I.ANIMAL_ID = O.ANIMAL_ID
WHERE O.DATETIME IS NULL
ORDER BY I.DATETIME LIMIT 3
```

### 헤비 유저가 소유한 장소

```sql
-- 코드를 입력하세요
SELECT *
FROM PLACES
WHERE HOST_ID IN (SELECT HOST_ID FROM PLACES GROUP BY HOST_ID HAVING COUNT(*) >=2)
```

### 오랜 기간 보호한 동물(2)

```sql
-- 코드를 입력하세요
SELECT I.ANIMAL_ID, I.NAME 
FROM ANIMAL_INS AS I JOIN ANIMAL_OUTS AS O USING (ANIMAL_ID)
ORDER BY O.DATETIME - I.DATETIME DESC 
LIMIT 2
```

### 즐겨찾기가 가장 많은 식당 정보 출력하기

```sql
SELECT FOOD_TYPE, REST_ID, REST_NAME, FAVORITES 
from REST_INFO
where (FOOD_TYPE, FAVORITES) in (select FOOD_TYPE, max(FAVORITES) 
                                  from rest_info
                                  group by FOOD_TYPE)
order by FOOD_TYPE DESC
```

### 조건별로 분류하여 주문상태 출력하기

> 풀이1

```sql
SELECT order_id, product_id, date_format(out_date, '%Y-%m-%d') as out_date,
if(out_date <= '2022-05-01', '출고완료', if(out_date is null, '출고미정', '출고대기')) as 출고여부
from food_order
order by order_id
```

> 풀이2

```sql
SELECT order_id, product_id, date_format(out_date, '%Y-%m-%d') as out_date,
case when datediff(out_date, '2022-05-01') <= 0 then '출고완료'
when datediff(out_date, '2022-05-01') > 0 then '출고대기'
else '출고미정' end as 출고여부
from food_order
order by order_id
```

