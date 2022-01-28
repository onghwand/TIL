# PJT01

> Python을 활용한 데이터 수집 I (22.01.21)

## 1. 배운 점

- 반복적인걸 할 때는 확장성을 고려해서 최대한 반복문을 이용하자

  ```python
  # 내 코드
  def movie_info(movie):
      # 여기에 코드를 작성합니다.
      movie_data = {}
  
      movie_id = movie.get('id')
      title = movie.get('title')
      poster_path = movie.get('poster_path')
      vote_average = movie.get('vote_average')
      overview = movie.get('overview')
      genre_ids = movie.get('genre_ids')
  
      movie_data['id'] = movie_id
      movie_data['title'] = title
      movie_data['poster_path'] = poster_path
      movie_data['vote_average'] = vote_average
      movie_data['overview'] = overview
      movie_data['genre_ids'] = genre_ids
  
      return movie_data
  
  # 개선안
  def movie_info(movie):
      datas= ["id", "title", "poster_path", "vote_average",  "overview", "genre_ids"]
        
      movie_data = dict()
      
      for data in datas :
          movie_data[data] = movie[data]
          
      return movie_data
  ```

  

- 변수이름은 짧고 깔끔하고 의미를 담을 수 있게. '어렵지만' 노력하자

  ``` python
  # 오늘 직접 지은 변수명들
  # 한 프로젝트 내의 변수명이고 비슷한 의미를 가지는데 통일성이 떨어지고 변수명의 길이가 길다
  
  # movie_data
  # id_to_genre_list
  # movie_data_genre
  # max_revenue_movie
  # movies_id_json
  # movies_id_list
  # December_movies
  # release_month
  ```

  

- 항상 자료형 잘 확인하자 

  ```python
  # list <-> dictionary
  genres => list
  get을 쓸 수 없었음
  
  # int <-> str
  # 오류를 보고 바로 깨달았지만 항상 잘 확인하자
  release_month = movies_id_list['release_date'].split('-')[1]
  >>>
  release_month = int(movies_id_list['release_date'].split('-')[1])
  ```



- dict[key] 와 dict.get(key) 차이

  ```python
  alpahbet = {'a':1, 'b':2}
  
  # dict[key] (key가 없으면 error가 뜸)
  print(alpahbet['c'])
  >>> KeyError: 'c'
      
  # dict.get(key) (key가 없으면 None을 반환)
  print(alpahbet.get('c'))
  >>> None
  
  ```
  
  

## 2. 트러블 슈팅

> 트러블 슈팅이란?

- 시스템에서 발생하는 복잡한 문제들을 종합적으로 진단해 해결하는 것

1.  파일 가져오는 걸 처음 해봐서 조금 난감했지만 f문을 이용함

   ``` python
   #1. open(위치(파일명), encoding='UTF8') 할당한다
   #2. json.load를 이용하여 데이터 할당
   
   for movie in movies:
       movie_id = movie.get('id')
       movies_id_json = open(f'data/movies/{movie_id}.json', encoding='UTF8')
       movies_id_list = json.load(movies_id_json)   
   ```

   

## 3. 느낀점

- 데이터가 깔끔하고 모두 할당이 되어있다는 걸 알고있었기 때문에 굳이 예외처리를 하지 않았다.
- 예외처리문을 배운 후에는 결측치에 대한 예외처리를 생각해 봐야 할 것 같다.
