from django.db import models
from imagekit.processors import Thumbnail
from imagekit.models import ImageSpecField


class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    # blank vs null 
    # blank: 데이터 유효성과 관련되어 있다. (비어있어도 상관없어)
    # null: DB와 관련되어 있다. (DB 에 Null 로 저장할건지에 대한 여부 확인)
    # django 에서 textfiled 는 '' 
    image = models.ImageField(blank=True)  # chr 형식으로 들어감 그래서 null True 삭제 / 비어있는 str 이 들어가 있는 상태 
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[Thumbnail(50, 50)],
        format='JPEG',
        options={'quality': 90},
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

class Comment(models.Model):
    # on_delete=models.CASCADE == 'Article 이 삭제되면 Comment 도 함께 삭제'
    # article.comments 는 어떻게... related_name='comments' / default = comment_set
    # article.comments.all()
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 역순으로 가져올 수 있도록 
    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return self.content
