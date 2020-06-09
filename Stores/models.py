from django.db import models
from django.conf import settings
# Create your models here.

class Store(models.Model):
    code = models.CharField(max_length=30, verbose_name="가게 code",primary_key=True)
    store_name = models.CharField(max_length=100, verbose_name='가게 이름')
    geolat = models.DecimalField(max_digits=20, decimal_places=14, verbose_name='위도')
    geolon = models.DecimalField(max_digits=20, decimal_places=14, verbose_name='경도')

    def __str__(self):
        return self.store_name

    class Meta:
        db_table = 'Store' # 테이블명 지정
        verbose_name = 'store'
        verbose_name_plural='store'
