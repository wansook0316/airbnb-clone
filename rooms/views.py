from datetime import datetime
from math import ceil
from django.shortcuts import render
from django.core.paginator import Paginator
from . import models


def all_rooms(request):
    page = request.GET.get("page")  # default 값이 두번쨰 인자
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 10)  # 두번쨰 인지 페이지 수)
    rooms = paginator.get_page(page)
    print(vars(rooms.paginator))
    return render(request, "rooms/home.html", {"rooms": rooms})
