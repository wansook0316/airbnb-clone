from datetime import datetime
from math import ceil
from django.shortcuts import render
from django.core.paginator import Paginator
from . import models


def all_rooms(request):
    page = request.GET.get("page", 1)  # default 값이 두번쨰 인자
    room_list = models.Room.objects.all()
    paginator = Paginator(
        room_list, 10, orphans=5
    )  # 두번쨰 인지 페이지 안의 행 개수, orphan은 마지막에 고아로 남는 행들을 마지막에 몇개가 생기면 보여줄 것인지
    # rooms = paginator.get_page(page)
    rooms = paginator.page(int(page))
    return render(request, "rooms/home.html", {"page": rooms})
