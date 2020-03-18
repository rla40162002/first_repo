from django.contrib.auth.models import AbstractUser
from django.db import models  # 이건 안 씀


class User(AbstractUser):  # models.Model을 상속

    """ Custom User Model """  # docstring

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = {
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    }

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "kr"

    LANGUAGE_CHOICES = {
        (LANGUAGE_ENGLISH, "English"),
        # LANGUAGE_ENGLISH 값은 DB로, English는 form에서 보여질 값
        (LANGUAGE_KOREAN, "Korean"),
    }

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"

    CURRENCY_CHOICES = {
        (CURRENCY_USD, "USD"),
        (CURRENCY_KRW, "KRW"),
    }

    avatar = models.ImageField(blank=True)  # 사용자 사진
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
    # 성별, null 허용. 한 줄 텍스트 글자수 제한 있음
    bio = models.TextField(blank=True)  # 비어있는 string 값, 여러 줄 가능, 글자수제한없음
    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2, blank=True)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=3, blank=True)
    superhost = models.BooleanField(default=False)
