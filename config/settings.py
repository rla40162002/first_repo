"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("DJANGO_SECRET", "m9zAC;M.rP")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(os.environ.get("DEBUG"))
ALLOWED_HOSTS = [".elasticbeanstalk.com", "localhost"]


# Application definition

# INSTALLED_APPS 에 있던 것들 가져옴
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = ["django_countires", "django_seed"]
# 나중에 다른 개발자가 만든 app을 import 하기 위해 넣는 곳

# 만든 앱들을 여기에 설치
PROJECT_APPS = [
    "core.apps.CoreConfig",
    "users.apps.UsersConfig",
    "rooms.apps.RoomsConfig",
    "reviews.apps.ReviewsConfig",
    "reservations.apps.ReservationsConfig",
    "lists.apps.ListsConfig",
    "conversations.apps.ConversationsConfig",
]

# INSTALLED_APPS 처음부터 설치된 앱 적혀있던 곳
# INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + PROJECT_APPS
INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.locale.LocaleMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases


# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
#     }
# }
if DEBUG:

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "HOST": os.environ.get("RDS_HOST"),
            "NAME": os.environ.get("RDS_NAME"),
            "USER": os.environ.get("RDS_USER"),
            "PASSWORD": os.environ.get("RDS_PASSWORD"),
            "PORT": "5432",
        }
    }


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {  # 사용자 패스워드 강도 확인하는 데 사용되는 유효성 검사기들
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },  # 유사성 검사기. 사용자 정보와 유사한 것이 있는지 체크
    # {"NAME":"django.contrib.auth.password_validation.MinimumLengthValidator"},
    # 패스워드 최소 길이 검사기 (이 파일에 없었던 것.)
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    # 흔한 패스워드 검사기 : 2만개의 흔한 패스워드와 동일한지 체크
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"
    },  # 패스워드가 숫자로만 되어있는지 체크하는 검사기
    # 세줄 }전에 있는 컴마 하나씩 지움
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Seoul"  # 표준시간대 설정 가능

USE_I18N = True  # internationaliztion

USE_L10N = True  # localization

USE_TZ = True
# True로 설정 시, DB엔 UTC(세계표준시)로 저장, UI엔 TIME_ZONE에 설정한 시간대를 반영하여 처리
# 아시아/서울 시간대만 사용한다면 false로 설정하는 게 더 편리할 수 있음
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = "/static/"
# not dir, just Server url
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
# 변수명이 꼭 STATIC 안 들어가도 됨.

AUTH_USER_MODEL = "users.User"
# 만든 User를 쓰기 위해 바꿔줌

MEDIA_ROOT = os.path.join(BASE_DIR, "uploads")
MEDIA_URL = "/media/"


# Email Configration(환경설정)

EMAIL_HOST = "smtp.mailgun.org"
EMAIL_PORT = "587"
EMAIL_HOST_USER = os.environ.get("MAILGUN_USERNAME")
EMAIL_HOST_PASSWORD = os.environ.get("MAILGUN_PASSWORD")
EMAIL_FROM = "yw@sandbox33587d05071d405aaec887e0f9c6af92.mailgun.org"

# Auth

LOGIN_URL = "/users/login/"


# Locale

LOCALE_PATHS = (os.path.join(BASE_DIR, "locale"),)

# Sentry

if not DEBUG:
    sentry_sdk.init(
        dsn=os.environ.get("SENTRY_URL"),
        integrations=[DjangoIntegration()],
        send_default_pii=True,
    )