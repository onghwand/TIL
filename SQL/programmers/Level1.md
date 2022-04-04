## Level1

https://programmers.co.kr/learn/challenges

### 모든 레코드 조회하기

```sql
-- 코드를 입력하세요
SELECT ANIMAL_ID, ANIMAL_TYPE, DATETIME, INTAKE_CONDITION, NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
ORDER BY ANIMAL_ID
```

### 최댓값 구하기

```sql
-- 코드를 입력하세요
SELECT DATETIME
FROM ANIMAL_INS
ORDER BY DATETIME DESC LIMIT 1
```

### 이름이 없는 동물의 아이디

```sql
-- 코드를 입력하세요
SELECT ANIMAL_ID
FROM ANIMAL_INS
WHERE NAME IS NULL
```

### 역순 정렬하기

```sql
-- 코드를 입력하세요
SELECT NAME, DATETIME
FROM ANIMAL_INS
ORDER BY ANIMAL_ID DESC
```

### 이름이 있는 동물의 아이디

```sql
-- 코드를 입력하세요
SELECT ANIMAL_ID
FROM ANIMAL_INS
WHERE NAME IS NOT NULL
```

### 아픈 동물 찾기

```sql
-- 코드를 입력하세요
SELECT ANIMAL_ID , NAME
FROM ANIMAL_INS
WHERE INTAKE_CONDITION = 'Sick'
```

### 어린 동물 찾기

```sql
-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE INTAKE_CONDITION !='Aged'
```

### 동물의 아이디와 이름

```sql
-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
ORDER BY ANIMAL_ID
```

### 여러 기준으로 정렬하기

```sql
-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME, DATETIME
FROM ANIMAL_INS
ORDER BY NAME, DATETIME DESC
```

### 상위 n개 레코드

```sql
-- 코드를 입력하세요
SELECT NAME
FROM ANIMAL_INS
ORDER BY DATETIME LIMIT 1
```

