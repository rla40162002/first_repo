from django.contrib.auth.models import AbstractUser
from django.db import models  # 이건 안 씀


class User(AbstractUser):  # models.Model을 상속

    bio = models.TextField(default="")
