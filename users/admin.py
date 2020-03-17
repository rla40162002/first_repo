from django.contrib import admin
from . import models  # .은 동일폴더라는 의미


@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):

    pass
