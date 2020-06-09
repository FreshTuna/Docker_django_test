from django.db import models

# Create your models here.

class EntranceList(models.Model):
    num = models.AutoField(primary_key=True)
    id = models.ForeignKey('FakeID.ID', on_delete=models.CASCADE, verbose_name='사용자')
    code = models.ForeignKey('Stores.Store', on_delete=models.CASCADE, verbose_name='시설')
    visit_dttm = models.DateTimeField(auto_now_add=True, verbose_name='입장 시간')

    def __str__(self):
        return "visitLog"

    class Meta:
        db_table = 'EntranceList'
        verbose_name = '입장 목록'
        verbose_name_plural = '입장 목록'

