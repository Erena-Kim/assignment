from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=10)

    #admin page에서 self.title로 확인하기 위한 조치
    def __str__(self):
        return self.title