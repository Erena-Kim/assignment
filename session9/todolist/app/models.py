from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, null=True)
    content = models.TextField(null=True)
    duedate = models.DateField(null=True)

    def __str__(self):
        return self.title