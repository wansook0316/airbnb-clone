from django.db import models


# Create your models here.

# 얘는 데이터 베이스로 형성되는 것을 원치 않고
# 다른 모델이 생성될 때 반복되는 것을 방지하기 위함임
# 따라서 데이터 베이스가 생성되는 것을 막아야 함
class TimeStampedModel(models.Model):
    """ Time Stamped Model """

    # auto_now_add : 모델이 생성된 날짜를 입력해줌
    # auto_now : 새로운 날짜로 업데이트 해줌
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # 그래서 메타 클래스의 추상을 true로 해준다.
    # 보통 추상적이냐고 물어봤을 때 그렇다고 한 경우,
    # 이후에 확장을 하기 위해서 사용많이한다. AbstractUser 처럼
    # 여튼 이렇게 하면 데이터 베이스 등록이 안된당
    class Meta:
        abstract = True
