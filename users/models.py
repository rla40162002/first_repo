from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):  # models.Model을 상속

    """ Custom User Model """  # docstring

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "kr"

    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, "English"),
        # LANGUAGE_ENGLISH 값은 DB로, English는 form에서 보여질 값
        (LANGUAGE_KOREAN, "Korean"),
    )

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"

    CURRENCY_CHOICES = (
        (CURRENCY_USD, "USD"),
        (CURRENCY_KRW, "KRW"),
    )
    LOGIN_EMAIL = "email"
    LOGIN_GITHUB = "github"
    LOGIN_KAKAO = "kakao"

    LOGIN_CHOICES = (
        (LOGIN_EMAIL, "Email"),
        (LOGIN_GITHUB, "Github"),
        (LOGIN_KAKAO, "Kakao"),
    )

    avatar = models.ImageField(upload_to="avatars", blank=True)  # 사용자 사진
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
    # 성별, null 허용. 한 줄 텍스트 글자수 제한 있음
    bio = models.TextField(blank=True)  # 비어있는 string 값, 여러 줄 가능, 글자수제한없음
    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, max_length=2, blank=True, default=LANGUAGE_KOREAN
    )
    currency = models.CharField(
        choices=CURRENCY_CHOICES, max_length=3, blank=True, default=CURRENCY_KRW
    )
    superhost = models.BooleanField(default=False)

    login_method = models.CharField(
        max_length=50, choices=LOGIN_CHOICES, default=LOGIN_EMAIL
    )
