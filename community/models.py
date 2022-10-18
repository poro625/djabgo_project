from turtle import title, update
from venv import create
from django.db import models
from users.models import User

# 모델을 맨처음에 만들고 어드민에 연결시키고 마이그레이트하고 admin url에 들어와서 확인해볼것

class Article(models.Model): # 타이틀 컨텐트 생성날짜 수정날짜 유저
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE) # null 이란 빈값을 허용하냐 안하냐지만 아이디값이 존재 하지 않으면 다 지워져야하기 때문에 null값을 지운다

    def __str__(self):
        return str(self.user)