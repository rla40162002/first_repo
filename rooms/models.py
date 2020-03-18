from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models


class Room(core_models.TimeStampedModel):

    """ Room Model Definition """

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()  # 가격이 소수일 필요 없기 때문에 decimal이 아닌 integer
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    # 이용 가능 인원, 침대, 방 개수, 욕실 개수
    check_in = models.TimeField()  # 체크인 시간
    check_out = models.TimeField()  # 체크아웃 시간
    instant_book = models.BooleanField(default=False)  # 바로 예약 가능한지 여부
    host = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    # 집주인, foreignkey 를 사용해서 user와 room을 연결해줌.
