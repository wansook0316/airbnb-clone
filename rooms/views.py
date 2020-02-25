from django.utils import timezone
from django.views.generic import ListView
from django.shortcuts import render
from . import models


class HomeView(ListView):

    """HomeView Definition"""

    # 해당 클래스의 property와 method는 ListView라고 django docs에 가도 되지만
    # 보기 굉장히 짜증나기 때문에 classy class-Based Views https::/ccbv.co.uk 에 들어가자.

    model = models.Room  # 어떤 모델을 보여줄 지 선택하면 자동으로 template/rooms/room_list.html을 찾는다!
    paginate_by = 10
    # page_kwarg = "potato" page=여기서 page의 이름을 바꿀 수 있음
    paginate_orphans = 5
    ordering = "created"  # model이 갖고 있는 feature 어떤 순으로 나열할 것인지
    context_object_name = "rooms"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = timezone.now()
        context["now"] = now
        return context


def room_detail(request):
    render(request,)

