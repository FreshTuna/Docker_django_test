from django.db import models
from django.conf import settings
# Create your models here.

class ID(models.Model):
    anonymousID = models.CharField(max_length=100, verbose_name="Token", primary_key=True)
    name = models.CharField(max_length=100, verbose_name='이름')
    phonenumber = models.CharField(max_length=11,verbose_name='전화번호', null=True)
    registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')
    address = models.CharField(max_length=30, verbose_name='주소', null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'fakeid_user' # 테이블명 지정
        verbose_name = 'IDs'
        verbose_name_plural='IDs'