from django.contrib import admin
from .models import Post, Comment, Like, Zim

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Zim)
