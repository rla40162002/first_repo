from django.contrib import admin
from django.utils.html import mark_safe
from . import models


# roomtype add가능하게 해줌
@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.rooms.count()


class PhotoInline(admin.TabularInline):
    model = models.Photo


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room Admin Definition """

    inlines = (PhotoInline,)
    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "city", "address", "price")},
        ),
        ("Time", {"fields": ("check_in", "check_out", "instant_book")},),
        ("Spaces", {"fields": ("guests", "beds", "bedrooms", "baths")},),
        (
            "More About the Space",
            {
                "classes": ("collapse",),
                "fields": ("amenities", "facilities", "house_rules"),
            },
        ),
        ("Last Details", {"fields": ("host",)},),
    )

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        "count_photos",
        "total_rating",
    )  # 리스트에서 보여지는 것

    ordering = ("name", "price", "bedrooms")
    # 정렬 순서대로 우선순위 갖고 있음

    list_filter = (
        "instant_book",
        "host__superhost",
        "room_type",
        "amenities",
        "facilities",
        "house_rules",
        "city",
        "country",
    )
    raw_id_fields = ("host",)
    search_fields = ("=city", "^host__username")  # __ 를 통해서 유저이름을 가져올 수 있음
    # 도시 전체를 입력해야하고, 검색된 단어로 시작하는 유저를 찾음

    filter_horizontal = ("amenities", "facilities", "house_rules")
    # room 정보 입력하는 곳에서의 필터 변화

    def count_amenities(self, obj):
        return obj.amenities.count()

    count_amenities.short_description = "COUNT AMT"
    # 보여주고 싶은 내용

    def count_photos(self, obj):
        return obj.photos.count()

    count_photos.short_description = "Photo Count"

    list_filter = ("instant_book", "city", "country")
    search_fields = ("=city", "^host__username")  # __ 를 통해서 유저이름을 가져올 수 있음
    # 도시 전체를 입력해야하고, 검색된 단어로 시작하는 유저를 찾음


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Photo Admin Definition"""

    list_display = (
        "__str__",
        "get_thumbnail",
    )

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.file.url}" />')

    get_thumbnail.short_description = "Thumbnail"
