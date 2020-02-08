from datetime import datetime
from math import ceil
from django.shortcuts import render
from . import models


def all_rooms(request):
    page = int(request.GET.get("page", str(1)))  # default 값이 두번쨰 인자
    page_size = 10
    limit = page_size * page
    offset = limit - page_size
    all_rooms = models.Room.objects.all()[offset:limit]
    page_count = ceil(models.Room.objects.count() / page_size)

    return render(
        request,
        "rooms/home.html",
        context={
            "rooms": all_rooms,
            "page": page,
            "page_count": page_count,
            "page_range": range(1, page_count),
        },
    )
