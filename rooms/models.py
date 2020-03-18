from django.db import models
from django_countries.fields import CountryField
from core import models as core_models


class AbstractItem(core_models.TimeStampedModel):

    """ Abstract Item """

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):
    # roomtype ex 호텔, 개인, 집전체, 공유실 등
    """ RoomType Model Definition """

    class Meta:
        verbose_name = "Room Type"
        ordering = ["name"]


class Amenity(AbstractItem):
    # 예의
    """ Amenity Model Definition """

    class Meta:
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):
    # 시설
    """ Facility Model Definition """

    class Meta:
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):
    # 숙소 규칙
    """ HouseRule Model Definition """

    class Meta:
        verbose_name = "House Rule"


class Photo(core_models.TimeStampedModel):

    """ Photo Model Definition """

    caption = models.CharField(max_length=80)
    file = models.ImageField()
    room = models.ForeignKey("Room", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


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
    host = models.ForeignKey("users.User", on_delete=models.CASCADE)
    # 집주인, foreignkey 를 사용해서 user와 room을 연결해줌.
    room_type = models.ForeignKey("RoomType", on_delete=models.SET_NULL, null=True)
    # 방은 하나의 타입만 선택해야함
    amenities = models.ManyToManyField("Amenity", blank=True)
    facilities = models.ManyToManyField("Facility", blank=True)
    house_rules = models.ManyToManyField("HouseRule", blank=True)

    def __str__(self):
        return self.name
