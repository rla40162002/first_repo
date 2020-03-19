from django.db import models
from core import models as core_models


class Review(core_models.TimeStampedModel):

    """ Review Model Definition """

    review = models.TextField()  # 리뷰

    accuracy = models.IntegerField()  # 정확성
    communication = models.IntegerField()  # 의사소통
    cleanliness = models.IntegerField()  # 청결도
    location = models.IntegerField()  # 위치
    check_in = models.IntegerField()  # 체크인
    value = models.IntegerField()  # 만족도
    # 여러 부분에서의 평점

    # 작성자
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    # 평가되는 숙소
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.review}-{self.room}"
