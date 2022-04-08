## HTTP requests & Media files

### 1. HTTP requests

> Handling HTTP requests

- get_object_or_404()
  - 모델 manager인 objects 에서 get()을 호출하지만, 해당 객체가 없을경우 DoesNotExist 예외 대신 Http 404를 raise
  - 코드 실행 단계에서 발생한 예외 및 에러에 대해서는 http status code 500으로 인식함
    - 5로 시작하면 server잘못인데 사실은 클라이언트 잘못이므로 404로 바꿔서 전달

<br>

> Allowed HTTP methods
>
> 요청 메서드에 따라 view함수에 대한 엑세스 제한
>
> 요건이 충족 안되면 405Method Not Allowed return

1. require_http_methods()
2. require_POST()
3. require_safe

```python
from django.views.decorator.http import require_http_methods, require_POST, require_safe

@require_safe
def index(request):
    pass

@require_http_methods(['GET','POST'])
def create(request):
    pass

@require_POST
def delete(request, pk):
    pass
```

<br>

### 2. Media Files

#### 2.1. ImageField 작성

- upload_to = 'images/'	
  - 실제 이미지가 저장되는 경로를 지정
- blank=True
  - 이미지 필드에 빈 값이 허용되도록 설정(이미지를 선택적으로 업로드)

```python
# articles/models.py

class Article(models.Model):
    image = models.ImageField(upload_to='images/', blank=True)
```

#### 2.2. settings.py

```python
MEDIA_ROOT = BASE_DIR / 'media' # 사용자가 업로드 한 파일들을 보관할 디렉토리의 절대 경로
MEDIA_URL = '/media/' # domain/media/~~~ => 사진을 처리하는 URL
```

#### 2.3. 렌더링

- 업로드 된 파일의 경로는 django가 제공하는 `url`속성을 통해 얻을 수 있음

```django
<img src="{{ article.image.url }}" alt="{{article.image}}">
```

#### 2.4. urls.py

- 사용자가 업로드 한 파일이 프로젝트에 업로드 되더라도, 실제로 사용자에게 제공하기 위해서는 업로드 된 파일의 URL이 필요함

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #생략
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

#### 2.5. 마이그레이션 실행

- ImageField를 사용하기 위해서는 Pillow 라이브러리 설치 필요

```bash
$ pip install Pillow
$ python manage.py makemigrations
$ python manage.py migrate
$ pip freeze > requirements.txt
```

#### 2.6. 이미지 업로드

> create.html
>
> `enctype="multipart/form-data"` 속성 지정
>
> 전송되는 데이터의 형식을 지정하므로 이미지 업로드 시에 반드시 설정해야함
>
> <input type="file">을 사용할 경우 사용

```django
<form action="{% url 'movies:create' %}" method="POST" enctype="multipart/form-data">
    {% csrf_token %}
    {{form.as_p}}
    <input type="submit">
</form>  
```

#### 2.7. views.py 수정

- ArticleForm 두번째 인자에 `request.FILES` 추가 POST객체랑 다른 객체로 전달됨
- update에도 똑같이 두번째인자로 작성하면 수정할때 덮어씌워짐

```python
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES) 
        # 생략
```

#### 2.8. DETAIL.html 수정

- img가 없으면 오류발생하므로 이미지가 업로드됐을 때만 보여주는 조건문

```django
{% if article.image %}
	<img src="{{ article.image.url }}" alt="{{ article.image}}">
{% endif %}
```

<br>

### 3. 이미지 Resizing

- 실제 원본 이미지를 서버에 그대로 업로드 하는 것은 서버의 부담이 큰 작업
- img 태그에서 직접 사이즈를 조정할 수도 있지만 업로드 될 때 이미지 자체를 resizing 할 수 있음
  - django-imagekit 라이브러리 활용

#### 3.1. 원본 X, 썸네일 O

```bash
$ pip install django-imagekit
$ pip freeze > requirments.txt
```

> settings.py

```python
INSTALLED_APP = [
    ...
    'imagekit',
    ...
]
```

> models.py

```python
from imagekit.processors import Thumbnail
from imagekit.models import ProcessedImageField

class Article(models.Model):
    image = ProcessedImageField(
    	blank=True,
    	upload_to='thumbnail/',
    	processors=[Thumbnail(200,300)],
    	format='JPEG',
    	options={'quality':90},
    )
```

- 모델 변경했으므로

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```



