from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
    path("", include("core.urls", namespace="core")),
    path("rooms/", include("rooms.urls", namespace="rooms")),
    path("users/", include("users.urls", namespace="users")),
    path("reservations/", include("reservations.urls", namespace="reservations")),
    path("reviews/", include("reviews.urls", namespace="reviews")),
    path("lists/", include("lists.urls", namespace="lists")),
    path("conversations/", include("conversations.urls", namespace="conversations")),
    path("admin/", admin.site.urls),
    path("sentry-debug/", trigger_error),
]  # 이부분 변경하면 접속할때의 주소가 바뀜.

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # url 은 settings.MEDIA_URL, 폴더는 settings.MEDIA_ROOT
