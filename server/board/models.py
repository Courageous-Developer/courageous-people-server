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
    user = models.ForeignKey(User, related_name='+', on_delete=models.CASCADE)
    updt_dt = models.DateTimeField(db_column='updt_dt', auto_now=True)
    insrt_dt = models.DateTimeField(db_column='insrt_dt', auto_now_add=True)
    usage_fg = models.CharField(db_column='usage_fg', max_length=1, blank=True, null=True, default='Y')

    class Meta:
        managed = True
        db_table = 'store'
        app_label = 'board'


class Menu(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True)
    menu = models.CharField(db_column='menu', max_length=45)
    store = models.ForeignKey(Store, related_name='+', on_delete=models.CASCADE, blank=True, null=True)
    updt_dt = models.DateTimeField(db_column='updt_dt', auto_now=True)
    insrt_dt = models.DateTimeField(db_column='insrt_dt', auto_now_add=True)
    usage_fg = models.CharField(db_column='usage_fg', max_length=1, blank=True, null=True, default='Y')

    class Meta:
        managed = True
        db_table = 'menu'
        app_label = 'board'


class Review(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True)
    content = models.CharField(db_column='content', max_length=200, blank=True, null=True)
    user = models.ForeignKey(User, related_name='+', on_delete=models.CASCADE, blank=True, null=True)
    store = models.ForeignKey(Store, related_name='+', on_delete=models.CASCADE, blank=True, null=True)
    # 등록, 수정 컬럼 + 데이터 보존 Flag 컬럼
    updt_dt = models.DateTimeField(db_column='updt_dt', auto_now=True)
    insrt_dt = models.DateTimeField(db_column='insrt_dt', auto_now_add=True)
    usage_fg = models.CharField(db_column='usage_fg', max_length=1, blank=True, null=True, default='Y')

    class Meta:
        managed = True
        db_table = 'review'
        app_label = 'board'


class ReviewImg(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True)
    review_img = models.CharField(db_column='review_img', max_length=200, blank=True, null=True)
    review = models.ForeignKey(Review, related_name='+', on_delete=models.CASCADE)
    # 등록, 수정 컬럼 + 데이터 보존 Flag 컬럼
    updt_dt = models.DateTimeField(db_column='updt_dt', auto_now=True)
    insrt_dt = models.DateTimeField(db_column='insrt_dt', auto_now_add=True)
    usage_fg = models.CharField(db_column='usage_fg', max_length=1, blank=True, null=True, default='Y')

    class Meta:
        managed = True
        db_table = 'review_img'
        app_label = 'board'


class Tag(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True)
    tag_content = models.CharField(db_column='tag_content', max_length=200)
    review = models.ForeignKey(Review, related_name='+', on_delete=models.CASCADE)
    TagType = (
        (1, "Product"),
        (2, "Bowl"),
    )
    type = models.IntegerField(db_column='type', choices=TagType, default=1)
    # 등록, 수정 컬럼 + 데이터 보존 Flag 컬럼
    updt_dt = models.DateTimeField(db_column='updt_dt', auto_now=True)
    insrt_dt = models.DateTimeField(db_column='insrt_dt', auto_now_add=True)
    usage_fg = models.CharField(db_column='usage_fg', max_length=1, blank=True, null=True, default='Y')

    class Meta:
        managed = True
        db_table = 'tag'
        app_label = 'board'
