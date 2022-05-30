## 영화 추천 알고리즘 

> 문제설명

당신은 사용자가 영화를 클릭하면 해당 영화와 개봉일이 비슷한 영화리스트를 추천해주는 알고리즘을 구현하려고 한다. 개봉일이 비슷하다는 기준은 해당 영화 개봉일 전후 7일이다. 전후 7일의 기간동안 3개 이상의 영화가 없다면 전후 14일로 설정한 뒤 다시 리스트를 만든다. 만약 전후 14일에도 영화의 개수가 3개가 안된다면 0을 return한다.



만약 영화리스트가 3개 이상이라면 평점순으로 정렬하여 높은순으로 3개만 리스트에 담아 return한다. 만약 평점이 같다면 영화제목 사전순으로 정렬한다.



>  추가 조건

1. 윤년이 아니고 2월은 28일이다.

2. choice에 영화제목이 중복되어 들어가 있을 수 있다. 영화 제목이 중복된다면 더 일찍 개봉한 영화를 선택한다.

   

>  입력값 설명

입력값으로 선택된 영화 choice와 movies가 주어진다.

choice는 사용자가 고른 영화이며 '개봉일 영화제목'으로 주어진다.

movies는 영화들 목록 리스트인데 '개봉일 제목 평점'이 하나의 문자열로 리스트의 원소가 된다.



>  입출력 예 #1

choice= "05/30 Batman"

movies= ["03/23 HarryPotter 3.6", 04/27 Heartstopper 4.7", "06/24 Playlist 1.5", "04/12 Top Gun 3.8", "05/20 Men 2.2", "05/26 HarryPotter 4.5", "05/24 LalaLand 4.3", "06/02 Shrek 4.0"]

- 평점순

| 개봉일 | 영화제목          | 평점 | 날짜차이 | 비고                              |
| ------ | ----------------- | ---- | -------- | --------------------------------- |
| 06/11  | Morbius           | 4.8  | 11       |                                   |
| 04/27  | Heartstopper      | 4.7  |          |                                   |
| 05/26  | <~~HarryPotter~~> | 4.5  | -4       | 03/23에 개봉한 HarryPotter가 있음 |
| 05/24  | LalaLand          | 4.3  | -6       |                                   |
| 06/02  | Shrek             | 4.0  | 2        |                                   |
| 04/12  | Top Gun           | 3.8  |          |                                   |
| 03/23  | HarryPotter       | 3.6  |          |                                   |
| 05/20  | Men               | 2.2  | -10      |                                   |
| 06/24  | Playlist          | 1.5  |          |                                   |
| 05/21  | The Northman      | 1.3  | -9       |                                   |

HarryPotter는 중복되었으므로 더 일찍 개봉한 03/23 HarryPotter를 선택한다. 평점 순으로 주어진 movie_list를 정렬해보았을 때, target_movie의 개봉일 전후 7일에 개봉한 영화의 수가 3개가 되지 않으므로 전후14일로 설정하여 다시 검색한다. 그러면 Morbius, LalaLand, Shrek, Men, The Northman 4개의 영화가 만족하는데 그 중 평점 순으로 상위 3개인 Morbius,LalaLand, Shrek을 리스트 형태도 return 한다. 단, 리스트 안의 영화 순서 역시 평점순이어야 한다.



>  입력

| choice         | movies                                                       | result                           |
| -------------- | ------------------------------------------------------------ | -------------------------------- |
| "05/30 Batman" | ["03/23 HarryPotter 3.6", "04/27 Heartstopper 4.7", "06/24 Playlist 1.5", "04/12 Top Gun 3.8", "05/20 Men 2.2", "05/26 HarryPotter 4.5", "05/24 LalaLand 4.3", "06/02 Shrek 4.0", "06/11 Morbius 4.8"] | ['Morbius', 'LalaLand', 'Shrek'] |
|                |                                                              |                                  |
|                |                                                              |                                  |



> solution.py
>
> 문제푸는 사람에게 기본적으로 주어지는 함수 세팅

```python
def solution(choice, movies):
    answer = []
    return answer
```



> solution
>
> 풀이(미완성)

```python
from datetime import date

# 입력값
choice = "05/30 Batman"
movies =["03/23 HarryPotter 3.6", "04/27 Heartstopper 4.7", "06/24 Playlist 1.5", "04/12 TopGun 3.8", "05/20 Men 2.2", "05/26 HarryPotter 4.5", "05/24 LalaLand 4.3", "06/02 Shrek 4.0", "06/11 Morbius 4.8"]

# 풀이
def solution(choice, movies):
    answer = []
    # 1. 중복 영화이름 지우고, 평점순으로 sort
    titles = set()
    filtered = []
    for movie in movies:
        rel, title, score = movie.split()
        if title in titles: # 영화가 중복되었다면 찾아서 바꿔
            for i in range(len(filtered)):
                rel1, title1, score1 = filtered[i].split()
                if title == title1:
                    month, day = map(int,rel.split('/'))
                    month1, day1 = map(int,rel1.split('/'))
                    rel=date(2022,month,day)
                    rel1=date(2022,month1,day1)
                    if rel1 > rel:
                        filtered[i] = movie
        else:
            titles.add(title)
            filtered.append(movie)
    #print(filtered)
    
    # 1-1. 평점순으로 sort하고 평점이 같은 영화가 있다면 영화제목 사전순으로
    #filtered = sorted(filtered, key=lambda x: date(2022,int(x[:5].split('/')[0]), int(x[:5].split('/')[1])))
    filtered = sorted(filtered, key=lambda x: float(x[-3:]), reverse=True)
    
    # 1-2 평점이 같은 영화에 대해서 영화제목 사전순으로 해야함 
    #print(filtered)
    
    # 2. choice영화 개봉일 datetime형태로 만들기
    release, title = choice.split()
    month, day = map(int, release.split('/'))
    #print(month, day)
    release=date(2022, month, day)
    #print(release)

    # 3. 조건에 맞게 반복문 돌면서 return
    limits = [7, 14] # 제한 기간
    for limit in limits:
        for movie in filtered:
            rel, title, score = movie.split()
            month, day = map(int, rel.split('/'))
            rel = date(2022, month, day)
            diff = (release-rel).days
            if abs(diff) <= limit:
                answer.append(title)

        if len(answer) >= 3:
            return answer[:3]
        else:
            answer = []
    if len(answer) >= 3:
        return answer[:3]
    else:
        return []
    
# 함수 실행(결과값)
print(solution(choice,movies))
```





