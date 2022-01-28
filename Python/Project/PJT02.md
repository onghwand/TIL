# PJT02

> Python을 활용한 데이터 수집 II (22.01.28)

## 1. 어려웠던 부분 / 느낀점 / 배운점

> 1-1. C번에서, 딕셔너리에서 value 기준으로 정렬하는 것을 잘 몰라서 구글을 통해 찾았다

- sorted() 두번째 인자에 key=lambda x: x[1]라고 입력하면 value 기준으로 정렬이 된다.
- sorted() 세번째 인자에 reverse=True라고 입력하면 내림차순 정렬이 가능하다.

```python
# 2-1. vote_average를 기준으로 영화 내림차순 정렬
    sorted_popular_movies = sorted(title_vote_average_dict.items(),
                                   key=lambda x: x[1], reverse=True)
```



> 1-2. D번에서, 예외처리문 try except 이용

- 아직까지 알고리즘 문제 풀 때 예외처리문을 요긴하게 써본적이 없어서 쓸 생각을 잘 못했다. 앞으로도 알고리즘 보다는 프로그램 만들 때, 자주 이용할 듯
- 예외 처리를 하지않으면 index out of range error가 뜨기 때문에 try except 문을 이용했다.

```python
# 1-1.title을 받아서 movie_id라는 변수에 해당 영화 id 저장 (movie 이름이 검색할 수 없는 경우 None 반환)
    try:
        movie_id = data.get('results')[0].get('id')
    except:
        return None
```



> 1-3.  D번에서, params가 두 개 필요해서 딕셔너리 이용

- params가 2개 필요해서 묶어서 딕셔너리를 만들었는데, 그냥 변수 2개 설정하는 것이랑 별다른 차이가 없을 것 같다.

```python
# version1
params = {'search': {'api_key': '1c495200bf8a0c1956a9c60b7877da9c',
                     'language': 'ko',
                     'query': title,
                     'region': 'KR'},
          'recommendations': {'api_key': '1c495200bf8a0c1956a9c60b7877da9c',
                              'language': 'ko'}
         }

# version2
params_search = {'api_key': '1c495200bf8a0c1956a9c60b7877da9c',
                 'language': 'ko',
                 'query': title,
                 'region': 'KR'}
params_reco = {'api_key': '1c495200bf8a0c1956a9c60b7877da9c',
               'language': 'ko'}
```



> 1-4.  웹 크롤링 

- 웹 크롤링 기초를 배웠다.
  1. import requests
  2. 앞부분에 들어가는 공통적인 BASE_URL 설정
  3. 세부 path 설정
  4. 정보 요청에 필요한 params 설정(웹페이지에 들어가서 살펴볼 것)
  5.  requests.get(URL, params)로 요청
  6.  데이터 형태(html, json 등) 확인 및 변환해서 이용하기

```python
import requests

# 0. 기본 URL, path, params 설정
BASE_URL = 'https://api.themoviedb.org/3'
path = '/search/movie'
params = {'api_key': '1c495200bf8a0c1956a9c60b7877da9c',
          'language': 'ko',
          'query': title,
          'region': 'KR'}

# 1. Search Movies에 정보 요청
response = requests.get(BASE_URL+path, params=params)
```



> 1-5. Json 구조 크롬에서 보기

- response.url을 통해 url을 받아서 크롬으로 json을 보면 좀 더 json 구조를 파악하기 용이하다. + JSON VIEWER(크롬 확장 프로그램)

```python
print(response.url)
# => https://api.themoviedb.org/3/movie/popular?api_key=1c495200bf8a0c1956a9c60b7877da9c&language=ko&region=KR
```



## 2. 코드 작성

> A. 인기 영화 조회

- 인기 영화의 개수를 출력합니다

```python
import requests

def popular_count():
    # 0. 기본 URL, path, params 설정
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {'api_key': '1c495200bf8a0c1956a9c60b7877da9c',
              'language': 'ko',
              'region': 'KR'}

    # 1. Get Plpular에 정보 요청
    response = requests.get(BASE_URL+path, params=params)
    data = response.json()

    # 2. popular 영화목록의 개수 출력.
    return len(data.get('results'))


if __name__ == '__main__':
    """
    popular 영화목록의 개수 출력.
    """
    print(popular_count())
    # => 20
```

> B. 특정 조건에 맞는 인기 영화 조회 I 

- popular를 기준으로 가져온 영화 목록 중 평점이 8 이상인 영화들의 목록을 출력합니다. 

```python
import requests
from pprint import pprint


def vote_average_movies():
    # 0. 기본 URL, path, params 설정
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {'api_key': '1c495200bf8a0c1956a9c60b7877da9c',
              'language': 'ko',
              'region': 'KR'}

    # 1. Get Plpular에 정보 요청
    response = requests.get(BASE_URL+path, params=params)
    data = response.json()
    popular_movies = data.get('results')

    # 2. 평점 8이상인 영화들 list 생성
    vote_average_movies_list = []
    for movie in popular_movies:
        if movie.get('vote_average', 0) >= 8:
            vote_average_movies_list.append(movie.get('title'))

    return vote_average_movies_list


if __name__ == '__main__':
    """
    popular 영화목록중 vote_average가 8 이상인 영화목록 출력.
    """
    pprint(vote_average_movies())
    # => 영화정보 순서대로 출력
```

> C. 특정 조건에 맞는 인기 영화 조회 II 

- 영화목록을 평점순으로 출력하는 함수를 완성합니다. 해당 기능은 향후 커뮤니티 서비스에서 기본으로 제공되는 영화 정보로 사용됩니다.

```python
import requests
from pprint import pprint


def ranking():
    # 0. 기본 URL, path, params 설정
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {'api_key': '1c495200bf8a0c1956a9c60b7877da9c',
              'language': 'ko',
              'region': 'KR'}

    # 1. Get Plpular에 정보 요청
    response = requests.get(BASE_URL+path, params=params)
    data = response.json()
    popular_movies = data.get('results')

    # 2. 영화이름과 평점으로만 이루어진 딕셔너리 생성, key: title, value: vote_average
    title_vote_average_dict = {}
    for movie in popular_movies:
        title_vote_average_dict[movie.get('title')] = movie.get('vote_average')

    # 2-1. vote_average를 기준으로 영화 내림차순 정렬
    sorted_popular_movies = sorted(title_vote_average_dict.items(),
                                   key=lambda x: x[1], reverse=True)

    # 3. 상위 5개 영화 이름 list(top5_movies)
    top5_movies = []
    for movie in sorted_popular_movies[:5]:
        top5_movies.append(movie[0])

    # 3-1. 상위 5개 영화 이름을 이용하여 상위 5개 영화 정보 list(top5_movies_info)
    top5_movies_info = []
    for movie in top5_movies:
        for movie_info in popular_movies:
            if movie == movie_info.get('title'):
                top5_movies_info.append(movie_info)

    return top5_movies_info


if __name__ == '__main__':
    """
    popular 영화목록을 정렬하여 평점순으로 5개 영화.
    """
    pprint(ranking())
    # => 영화정보 순서대로 출력
```

> D. 특정 영화 추천 영화 조회 

- 제공된 영화 제목을 기준으로 추천영화 목록을 출력합니다. 

```python
import requests
from pprint import pprint


def recommendation(title):
    # 0. 기본 URL, path, params 설정
    BASE_URL = 'https://api.themoviedb.org/3'
    path_search = '/search/movie'
    params = {'search': {'api_key': '1c495200bf8a0c1956a9c60b7877da9c',
                         'language': 'ko',
                         'query': title,
                         'region': 'KR'},
              'recommendations': {'api_key': '1c495200bf8a0c1956a9c60b7877da9c',
                                  'language': 'ko'}
              }

    # 1. Search Movies에 정보 요청
    response = requests.get(BASE_URL+path_search,
                            params=params.get('search'))
    data = response.json()

    # 1-1.title을 받아서 movie_id라는 변수에 해당 영화 id 저장 (movie 이름이 검색할 수 없는 경우 None 반환)
    try:
        movie_id = data.get('results')[0].get('id')
    except:
        return None

    # 2. 위에서 얻은 id를 이용하여 Get Recommendations에 정보 요청
    path_reco = f'/movie/{movie_id}/recommendations'
    response_reco = requests.get(BASE_URL+path_reco,
                                 params=params.get('recommendations'))
    data_reco = response_reco.json()
    movie_reco = data_reco.get('results')

    # 2-1. 추천 영화들 이름을 movie_reco_titles에 저장
    movie_reco_titles = []
    for movie in movie_reco:
        movie_reco_titles.append(movie.get('title'))

    return movie_reco_titles


if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면
    해당 영화의 id를 기반으로 추천 영화 목록 구성.
    추천 영화가 없을 경우 [].
    영화 id검색에 실패할 경우 None.
    """
    pprint(recommendation('기생충'))
    # ['조커', '조조 래빗', '1917', ..., '토이 스토리 4', '스파이더맨: 파 프롬 홈']
    pprint(recommendation('그래비티'))
    # []  => 추천 영화 없음
    pprint(recommendation('검색할 수 없는 영화'))
    # => None
```

> E. 배우, 감독 리스트 출력

- 영화에 출연한 배우들과 감독의 정보가 저장된 딕셔너리를 출력합니다. 

```python
import requests
from pprint import pprint


def credits(title):
    # 0. 기본 URL, path, params 설정
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {'api_key': '1c495200bf8a0c1956a9c60b7877da9c',
              'language': 'ko',
              'query': title,
              'region': 'KR'}

    # 1. Search Movies에 정보 요청
    response = requests.get(BASE_URL+path, params=params)
    data = response.json()
    # title을 받아서 movie_id라는 변수에 해당 영화 id 저장 (movie 이름이 검색할 수 없는 경우 None 반환)
    try:
        movie_id = data.get('results')[0].get('id')
    except:
        return None

    # 2. 위에서 얻은 id를 이용하여 Get Credits에 정보 요청
    path_credits = f'/movie/{movie_id}/credits'
    params_credits = {'api_key': '1c495200bf8a0c1956a9c60b7877da9c'}
    response_credits = requests.get(BASE_URL+path_credits,
                                    params=params_credits)
    data_credits = response_credits.json()

    # 3. cast_id < 10인 배우들 리스트 생성, actors
    # 3. department:Directing인 감독 리스트 생성, directors
    actors = []
    directors = []
    castings = data_credits.get('cast')
    crews = data_credits.get('crew')

    for casting in castings:
        if casting.get('cast_id') < 10:
            actors.append(casting.get('name'))

    for crew in crews:
        if crew.get('department') == 'Directing':
            directors.append(crew.get('name'))

    # 3-1. 위에서 만들어진 배우, 감독 list 합쳐서 딕셔너리 생성
    actors_directors_list = {'cast': actors,
                             'crew': directors}

    return actors_directors_list


if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면
    해당 영화 id를 통해 영화 상세정보를 검색하여
    주연배우 목록(cast)과 제작진(crew).
    영화 id검색에 실패할 경우 None.
    """
    pprint(credits('기생충'))
    # => {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # => None
```

