from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Store(models.Model):  # 가게
    id = models.BigAutoField(db_column='id', primary_key=True)
    store_name = models.CharField(db_column='store_name', max_length=45)
    address = models.CharField(db_column='address', max_length=200)
    post = models.CharField(db_column='post', max_length=500, blank=True, null=True)
    picture = models.CharField(db_column='picture', max_length=200, blank=True, null=True)
    biz_num = models.CharField(db_column='biz_num', max_length=45)
    user_id = models.ForeignKey(User, related_name='+', on_delete=models.CASCADE)
    updt_dt = models.DateTimeField(db_column='updt_dt', auto_now=True)
    insrt_dt = models.DateTimeField(db_column='insrt_dt', auto_now_add=True)
    usage_fg = models.CharField(db_column='usage_fg', max_length=1, blank=True, null=True, default='Y')

    class Meta:
        managed = True
        db_table = 'store'
        app_label = 'board'
