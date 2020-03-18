from django.db import models


class TimeStampedModel(models.Model):

    """ Time Stamped Model """

    created = models.DateTimeField()
    updated = models.DateTimeField()


class Meta:  # 이 두줄을 해줘야 DB에 등록되지 않음
    abstract = True  # DB에 나타나지 않는 추상 모델
