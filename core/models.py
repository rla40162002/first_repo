from django.db import models
from . import managers


class TimeStampedModel(models.Model):

    """ Time Stamped Model """

    created = models.DateTimeField(auto_now_add=True)
    # 새로운 모델을 만들면 장고가 현재 날짜, 시간을 여기에 입력해줌
    updated = models.DateTimeField(auto_now=True)
    # 모델 저장할때마다 새로운 날짜를 기록해줌.
    objects = managers.CustomModelManager()

    class Meta:  # 이 두줄을 해줘야 DB에 등록되지 않음
        abstract = True  # DB에 나타나지 않는 추상 모델
