## PJT09

> 알고리즘을 적용한 서버 구성
>

<br>

### 1. 어려웠던 점 & 배운 점

- 처음으로 유저 팔로우 기능 만드는데 preventDefault를 했음에도 자꾸 form submit하면 url이 넘어가서 많이 헤멨다. 다지우고 새로 짜서 되긴 했는데 아직도 뭐가 문제였는지는 모르겠다. 
- M:N 관계에서 movie에는 genre 번호가 기입되어있고 Genre 모델에 번호랑 genre명이 매칭되어 있었는데 번호에서 => 장르명으로 바꿔서 html에 출력하는 것도 시간이 오래걸렸다.
  - 결과적으로 아래 처럼 넘겼는데 이러면 코드가 지저분해질 가능성이 있어서
    [register.filter](https://docs.djangoproject.com/ko/4.0/howto/custom-template-tags/) 장고에서 filter를 직접만들어서 쓴다고 한다.


```python
@require_safe
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    genres = []
    for movi in movie.genres.all():
        #print(movie.pk)
        genres.append(Genre.objects.get(id=movi.pk).name)     
        
    context = {
        'movie':movie, 
        'genres' : genres,
    }
    return render(request, 'movies/detail.html', context)
```

