### Media 파일 올리기 위한 작업

1. Aritcle Model 에 `ImageField` 추가

2. Form 에서 파일 타입을 보낼 수 있도록 `ecntype` 속성을 `multipart/form-data` 로 줬음.

3. Form 안에서 File type 의 input 생성, `accept="image/*"` 속성을 줬음

   - `acccept` : 특정 파일 타입만 받을 수 있게 하기 위한 속성

4.  `create` 함수에서 파일을 `request.FILES` 에서 꺼내서 article 에 넣고 저장

5.  media 파일들을 저장하기 위한 폴더 설정

   ```python
   	# settings.py
       MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
   ```

6. Client 가 media 파일들로 접근할 수 있는 URL 이름 설정

   ```python
   	# settings.py
       MEDIA_URL = '/media/'
   ```

7. Client 가 실제 파일들로 접근할 수 있는 URL  생성 

   ```python
   	# crud/urls.py
       from django.conf import settings
   	from django.conf.urls.static import static 
       ...
       
       # MEDIA_URL 로 들어오면 MEDIA_ROOT 에 저장한 파일들로 접근할 수 있습니다. 
       urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   ```

8. Detail 페이지에서 이미지 보여주기

   `detail.html`

   ```django
   	<img src="{{ article.image.url }}" alt="{{ article.image }}">
   ```

   