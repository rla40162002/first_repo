from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models  # .은 동일폴더라는 의미
from rooms.models import Room


# class RoomInline(admin.StackedInline):
#     model = Room


# admin.py와 같은 폴더에 있는 models.py를 불러오는 것
@admin.register(models.User)  # 이걸 decorator라고 부름
class CustomUserAdmin(UserAdmin):
    # decorator는 클래스 위에 있어야 작동함  테스트용 코드에서는 매개변수 admin.ModelAdmin
    # CustomUserAdmin으로 user를 컨트롤 한다는 뜻

    """ Custom User Admin """
    # inlines = (RoomInline,)  # 다시 해야 할 부분
    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                    "login_method",
                )  # fields
            },  # Custom Profile
        ),  # fieldsets
    )  # 초기 admin 패널의 파란부분

    # 원래 기본으로 주는 거에 커스텀 붙이기
    list_filter = UserAdmin.list_filter + ("superhost",)

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "language",
        "currency",
        "superhost",
        "is_staff",
        "is_superuser",
        "email_verified",
        "email_secret",
        "login_method",
    )
