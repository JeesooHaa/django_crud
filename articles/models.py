from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
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
