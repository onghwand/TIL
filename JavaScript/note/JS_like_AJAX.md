## 좋아요 기능 - 비동기

### 0.  base.html, index.html

- block script 추가 => script 태그 추가
- axios CDN 추가

### 1. form에 class 추가 , 선택

class ='likeForm'

```javascript
const forms = document.querySelectorAll('.likeForm') // form에서 class="likeForm"

forms.forEach(form => {
    form.addEventListener('click', event => {
        event.preventDefault()
        // AJAX 요청
        const articleId = event.target.dataset.articleId 
        // form에서 data-article-id="{{article.pk}}"라고 설정하면 알아서 articleId로 변환
        const URL = `/articles/${articleID}/likes/`
        // 요청 보낼 URL 
        console.log(URL) // 브라우저에서 확인해보고 다음 단계
        
        // post요청이므로 axios.post
        
        // 이러고 요청보내면 csrf 오류 뜸
        axios.post(URL)
    })
})
```

### 2. CSRF 해결

[CSRF, Headers](https://docs.djangoproject.com/en/4.0/ref/csrf/)

```javascript
// 1번째인자 URL, 2번째인자 사용자에게 받은 정보(없으므로 빈칸), 3번째인자 headers
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
axios.post(URL, {}, {
    headers: {
        'X-CSRFToken': csrftoken
    }
})
```

### 3. 좋아요 <=> 좋아요 취소

- redirect가 아닌 JSON을 보내야함

>  views.py

```python
@require_POST
def likes(request, article_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)

        # 이 게시글에 좋아요를 누른 유저 목록에 현재 요청하는 유저가 있다면.. 좋아요 취소
        # if request.user in article.like_users.all(): 
        if article.like_users.filter(pk=request.user.pk).exists():
            article.like_users.remove(request.user)
            is_liked = False # 추가
        else:
            article.like_users.add(request.user)
            is_liked = True # 추가
        from django.http import JsonResponse # 추가
        context = { 
            'is_liked': is_liked, # 추가
        }
        return JsonResponse(context) # 수정
    return redirect('accounts:login')
```

> index.html

```javascript
//생략
axios.post(URL, {}, {
    headers : {
        'X-CSRFToken' : csrftoken
    }
})
	.then(response => {
    const isLiked = response.data.is_liked
    // 좋아요, 좋아요 취소 버튼에 id="like-{{article.pk}}"
    const button = document.querySelector(`#like-${articleId}`)
    button.value = isLiked ? '좋아요 취소' : '좋아요'
})
	.catch(error => console.log(error))
```



