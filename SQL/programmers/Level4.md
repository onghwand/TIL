## Level4

### 우유와 요거트가 담긴 장바구니

```sql
SELECT CART_ID FROM CART_PRODUCTS
WHERE name IN ('Milk', 'Yogurt')
GROUP BY CART_ID
HAVING COUNT(DISTINCT name) > 1;
```

### 입양 시각 구하기(2)

```sql
WITH RECURSIVE TEMP AS (
    SELECT 0 AS HOUR
    UNION ALL
    SELECT HOUR+1 FROM TEMP
    WHERE HOUR<23
)

SELECT HOUR, COUNT(ANIMAL_OUTS.DATETIME) AS COUNT FROM

TEMP LEFT JOIN ANIMAL_OUTS
ON TEMP.HOUR = HOUR(ANIMAL_OUTS.DATETIME)

GROUP BY HOUR;
```

### 보호소에서 중성화한 동물

```sql
SELECT I.ANIMAL_ID, I.ANIMAL_TYPE, I.NAME
FROM ANIMAL_INS AS I JOIN ANIMAL_OUTS AS O USING (ANIMAL_ID)
WHERE I.SEX_UPON_INTAKE LIKE '%Intact%' 
AND (O.SEX_UPON_OUTCOME LIKE '%Spayed%' or O.SEX_UPON_OUTCOME LIKE '%Neutered%')
```

### 주문량이 많은 아이스크림들 조회하기

```sql
SELECT j.flavor
from first_half as f join 
(select flavor, sum(total_order) as total_order from july group by flavor) as j
on j.flavor = f.flavor
order by (j.total_order+f.total_order) desc
limit 3
```

### 식품분류별 가장 비싼 식품의 정보 조회하기

```sql
SELECT CATEGORY, PRICE AS MAX_PRICE, PRODUCT_NAME
from food_product
where (category, price) in (select category, max(price) 
                            from food_product 
                            group by category
                            having category in ('과자', '국', '김치', '식용유'))
order by price desc
```

### 5월 식품들의 총매출 조회하기

```sql
SELECT p.PRODUCT_ID, p.PRODUCT_NAME, sum(p.price*amount) as TOTAL_SALES
from food_product as p join food_order as o on p.product_id=o.product_id
where date_format(produce_date,'%y-%m') = '22-05'
group by p.product_id
order by TOTAL_SALES desc, p.PRODUCT_ID
```

### 서울에 위치한 식당 목록 출력하기

```sql
SELECT i.rest_id, rest_name, food_type, favorites, address, round(avg(review_score),2) as score
from rest_info as i join rest_review as r on i.rest_id=r.rest_id
where address like '서울%'
group by rest_id
order by score desc, favorites desc
```

### 년, 월, 성별 별 상품 구매 회원 수 구하기

```sql
SELECT date_format(sales_date,'%Y') as YEAR, 
        MONTH(sales_date), 
        GENDER,
        count(distinct u.user_id) as USERS
from user_info as u join online_sale as o on u.user_id=o.user_id
where gender is not null
group by YEAR, MONTH(sales_date), GENDER
order by YEAR, MONTH(sales_date), GENDER
```

### 취소되지 않은 진료 예약 조회하기

```sql
SELECT apnt_no, pt_name, p.pt_no, mcdp_cd, dr_name, apnt_ymd
from patient as p join (select apnt_no, dr_name, apnt_ymd, pt_no, apnt_cncl_yn, d.mcdp_cd
                      from doctor as d join appointment as a on d.dr_id=a.mddr_id) as b
                      on p.pt_no=b.pt_no
where date_format(apnt_ymd,"%y-%m-%d")="22-04-13" and apnt_cncl_yn='N'
order by apnt_ymd
```

### 오프라인/온라인 판매 데이터 통합하기

```sql
SELECT *
from (select date_format(sales_date,'%Y-%m-%d') as sales_date, product_id, user_id, sales_amount 
      from online_sale 
      where year(sales_date) = 2022 and month(sales_date) = 3) as A 
      union all 
      (select date_format(sales_date,'%Y-%m-%d') as sales_date, product_id, null as user_id, sales_amount 
       from offline_sale 
       where year(sales_date) = 2022 and month(sales_date) = 3) 
order by sales_date, product_id, user_id
```

### 그룹별 조건에 맞는 식당 목록 출력하기

> 내 풀이는 뭔가 불필요한 서브쿼리를 많이 쓴 것 같다
>
> [참고](https://velog.io/@sheltonwon/SQL%EC%97%B0%EC%8A%B5-%EA%B7%B8%EB%A3%B9%EB%B3%84-%EC%A1%B0%EA%B1%B4%EC%97%90-%EB%A7%9E%EB%8A%94-%EC%8B%9D%EB%8B%B9-%EB%AA%A9%EB%A1%9D-%EC%B6%9C%EB%A0%A5%ED%95%98%EA%B8%B0) => 지금까지는 순위 함수 없이도 간단하게 풀려서 생각을 못했다. 근데 순위 함수 써도 join을 두번이나 써야하는 복잡한 문제긴 하다.

```sql
select F.member_name, review_text, date_format(review_date, '%Y-%m-%d') as review_date
from (select member_name
    from (select max(count) as max_count
        from (SELECT member_name, count(*) as count
            from rest_review as r join member_profile as m on r.member_id=m.member_id
            group by member_name) as A) as B
        join
        (SELECT member_name, count(*) as count
            from rest_review as r join member_profile as m on r.member_id=m.member_id
            group by member_name) as C
        on C.count = B.max_count) as G
    join
    (select member_name, review_text, review_date
    from member_profile as D join rest_review as E on D.member_id = E.member_id) as F
    on F.member_name = G.member_name
order by review_date, review_text
```

- rank() 로 개선

```sql
select member_name, review_text, date_format(review_date,'%Y-%m-%d') as review_date
from rest_review A
    join 
    (select member_name, r.member_id, rank() over (order by cnt desc) as ranking
    from (select *, count(*) as cnt
        from rest_review
        group by member_id) as r
        join
        member_profile as m 
        on r.member_id=m.member_id) B
    on A.member_id = B.member_id
where B.ranking=1
order by review_date
```

