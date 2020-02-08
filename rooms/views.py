from datetime import datetime
from django.shortcuts import render
from . import models


def all_rooms(request):
    page = int(request.GET.get("page", str(1)))  # default 값이 두번쨰 인자
    page_size = 10
    limit = page_size * page
    offset = limit - page_size
    all_rooms = models.Room.objects.all()[offset:limit]

    return render(request, "rooms/home.html", context={"rooms": all_rooms})
