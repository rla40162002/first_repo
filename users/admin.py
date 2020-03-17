from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models  # .은 동일폴더라는 의미


# admin.py와 같은 폴더에 있는 models.py를 불러오는 것
@admin.register(models.User)  # 이걸 decorator라고 부름
class CustomUserAdmin(UserAdmin):
    # decorator는 클래스 위에 있어야 작동함  테스트용 코드에서는 매개변수 admin.ModelAdmin
    # CustomUserAdmin으로 user를 컨트롤 한다는 뜻

    """ Custom User Admin """
    # list_display =("username", "email", "gender", "language", "currency", "superhost")
    # # user 목록 보여줄 때 속성들
    # list_filter = ("language", "currency", "superhost")
    # 테스트용 코드. 커스텀 전 Django가 갖고 있는 admin 패널 사용할 예정
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
                )  # fields
            },  # Custom Profile
        ),  # fieldsets
    )  # 초기 admin 패널의 파란부분


# admin.site.register(models.User, CustomUserAdmin)
# CustomUserAdmin 은 admin 패널에서 컨트롤 할 수 있는 user 클래스
# 위 코드와 decorator 부분의 코드는 같은 기능을 함
