## PJT05

> 프레임워크 기반 웹 페이지 구현
>
> [장고 태그 템플릿&필터](https://docs.djangoproject.com/en/4.0/ref/templates/builtins/)
>
> [장고 모델 필드 타입](https://docs.djangoproject.com/en/4.0/ref/models/fields/)

<br>

### 1. 어려웠던 점 & 배운 점

-  python과 html 사이에 자료 왔다갔다하면서 표현하는 거에 문제가 많다
  - 똑같은거 반복하기 보단 다양한 연습을 많이 해야 실력이 늘 듯

1. input 태그에는 여러 type이 존재한다 굳이 다 text로 받을 필요없음
   - number, url, date, text,reset ...
2. html 태그에는 여러 옵션이 있다. 파이썬으로 해결안하고 더 쉬운 길이 있을 수도
   - autofocus,required,min,max,step ...

	3. 장고 반복/조건문 잘 활용하면 효율적으로 구현할 수 있다.
    - views에서 genres = ["none", "commedy", "horror", "romance", "SF"] 넘겨주고 반복/조건 활용

```django
<select value="{{movie.genre}}" name="genre" id="genre">
      {% for genre in genres %}
        <option value={{genre}} {% if genre == movie.genre %}selected{% endif %}>{{genre}}</option>
      {% endfor %}
</select>
```

4. edit 페이지 구현할 때, 기존 날짜 받아서 표기하는 법
   - value='{{movie.release_date|date:'Y-d-m'}}' 입력 방법 filter이용해서 맞추기

```django
<p>
    <label for="release_date">RELEASE_DATE</label>
    <input type="date" name="release_date" id="release_date" value='{{movie.release_date|date:'Y-d-m'}}' required>
</p>
```

5. 생각해보니까 html 태그에 required 쓰면 null값이 들어올 일이 없다.

<br>

### 2. 느낀 점

**오류가 안풀리면 오탈자 검사 무조건**!!

- 처음에 `method`를 `mothod`라고 써놓고 발견을 못했다. 그러니 오류가 데이터 속성에 not null 설정이 안되어있다고 떴다. 전에 연습할 때는 설정안해도 한 번도 뜬 적이 없었는데 이상하다고 생각하며 null=True를 입력하고 있는 대참사

> 첫번째 시도 실패
>
> null = True

```python
class Movie(models.Model):
    title = models.CharField(max_length=20, null=True)
    -생략-
```

> 두번째 시도 
>
> 자료형 때문인가 싶어서 자료형 변환
>
> 이건 맞긴한데 html에서 애초에 type="number"로 받는게 낫다

```python
release_date = int(request.POST.get('release_date'))
```

> html에서 받아서 형변환 하지 말고 쓰면됨

```django
<input type="number" min="0" max="10" step="0.1" name="score" id="score" required>
```

