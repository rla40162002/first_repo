from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage
from . import models


def all_rooms(request):
    page = request.GET.get("page", 1)
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 10, orphans=5)
    try:
        rooms = paginator.page(int(page))  # page list중에서 요청된 페이지를 가져옴
        return render(request, "rooms/home.html", context={"page": rooms},)
        # all_rooms.html 과 all_rooms 메소드, all_rooms 변수가 같은 이름일 필요 없다.
    except EmptyPage:  # 어떤 예외를 핸들링 할 건지
        return redirect("/")
