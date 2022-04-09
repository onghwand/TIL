## Level2

### 고양이와 개는 몇 마리 있을까

```sql
-- 코드를 입력하세요
SELECT ANIMAL_TYPE, COUNT(*)
FROM ANIMAL_INS
GROUP BY ANIMAL_TYPE
ORDER BY ANIMAL_TYPE
```

### 루시와 엘라 찾기

```sql
-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
WHERE NAME IN ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')
```

### 최솟값 구하기

```sql
-- 코드를 입력하세요
SELECT DATETIME
FROM ANIMAL_INS
ORDER BY DATETIME LIMIT 1
```

### 동명 동물 수 찾기

```sql
-- 코드를 입력하세요
SELECT NAME, COUNT(NAME) 
FROM ANIMAL_INS
GROUP BY NAME HAVING COUNT(NAME) > 1
ORDER BY NAME
```

### 이름에 el이 들어가는 동물 찾기

```sql
-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE NAME LIKE '%el%' AND ANIMAL_TYPE = 'DOG'
ORDER BY NAME
```

### 동물 수 구하기

```sql
-- 코드를 입력하세요
SELECT COUNT(*)
FROM ANIMAL_INS
```

### 입양 시각 구하기(1)

```sql
-- 코드를 입력하세요
SELECT HOUR(DATETIME) AS HOUR, COUNT(*)
FROM ANIMAL_OUTS
GROUP BY HOUR(DATETIME) HAVING HOUR>=9 AND HOUR<20
ORDER BY HOUR
```

### NULL 처리하기

```sql
-- 코드를 입력하세요
SELECT ANIMAL_TYPE, IF(NAME IS NULL, "No name", NAME), SEX_UPON_INTAKE
FROM ANIMAL_INS
ORDER BY ANIMAL_ID
```

### 중성화 여부 파악하기

```sql
-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME, IF(SEX_UPON_INTAKE LIKE '%Neutered%' OR SEX_UPON_INTAKE LIKE '%Spayed%', 'O','X')
FROM ANIMAL_INS
```

### 중복 제거하기

```sql
-- 코드를 입력하세요
SELECT COUNT(DISTINCT NAME)
FROM ANIMAL_INS
WHERE NAME IS NOT NULL
```

### DATETIME에서 DATE로 형 변환

```sql
-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME, DATE_FORMAT(DATETIME,'%Y-%m-%d')
FROM ANIMAL_INS
ORDER BY ANIMAL_ID
```

### 