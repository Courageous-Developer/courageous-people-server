from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.


class Store(models.Model):  # 가게
    id = models.BigAutoField(db_column='id', primary_key=True)
    store_name = models.CharField(db_column='store_name', max_length=45)
    address = models.CharField(db_column='address', max_length=200)
    post = models.CharField(db_column='post', max_length=500, blank=True, null=True)
    biz_num = models.CharField(db_column='biz_num', max_length=45, blank=True, null=True)
    latitude = models.DecimalField(db_column='latitude', max_digits=18, decimal_places=15, blank=True, null=True)
    longitude = models.DecimalField(db_column='longitude', max_digits=18, decimal_places=15, blank=True, null=True)
    user = models.ForeignKey(get_user_model(), related_name='store', on_delete=models.CASCADE, blank=True, null=True)
    updt_dt = models.DateTimeField(db_column='updt_dt', auto_now=True)
    insrt_dt = models.DateTimeField(db_column='insrt_dt', auto_now_add=True)
    usage_fg = models.CharField(db_column='usage_fg', max_length=1, blank=True, null=True, default='Y')

    class Meta:
        managed = True
        db_table = 'store'
        app_label = 'board'


class StoreImg(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True)
    store_img = models.CharField(db_column='store_img', max_length=200, blank=True, null=True)
    store = models.ForeignKey(Store, related_name='store_img', on_delete=models.CASCADE)
    # 등록, 수정 컬럼 + 데이터 보존 Flag 컬럼
    updt_dt = models.DateTimeField(db_column='updt_dt', auto_now=True)
    insrt_dt = models.DateTimeField(db_column='insrt_dt', auto_now_add=True)
    usage_fg = models.CharField(db_column='usage_fg', max_length=1, blank=True, null=True, default='Y')

    class Meta:
        managed = True
        db_table = 'store_img'
        app_label = 'board'


class Menu(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True)
    menu = models.CharField(db_column='menu', max_length=45, blank=True, null=True)
    price = models.CharField(db_column='price', max_length=45, blank=True, null=True)
    store = models.ForeignKey(Store, related_name='menu', on_delete=models.CASCADE, blank=True, null=True)
    updt_dt = models.DateTimeField(db_column='updt_dt', auto_now=True)
    insrt_dt = models.DateTimeField(db_column='insrt_dt', auto_now_add=True)
    usage_fg = models.CharField(db_column='usage_fg', max_length=1, blank=True, null=True, default='Y')

    class Meta:
        managed = True
        db_table = 'menu'
        app_label = 'board'


class MenuImg(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True)
    menu_img = models.CharField(db_column='menu_img', max_length=200, blank=True, null=True)
    menu = models.ForeignKey(Menu, related_name='menu_img', on_delete=models.CASCADE)
    # 등록, 수정 컬럼 + 데이터 보존 Flag 컬럼
    updt_dt = models.DateTimeField(db_column='updt_dt', auto_now=True)
    insrt_dt = models.DateTimeField(db_column='insrt_dt', auto_now_add=True)
    usage_fg = models.CharField(db_column='usage_fg', max_length=1, blank=True, null=True, default='Y')

    class Meta:
        managed = True
        db_table = 'menu_img'
        app_label = 'board'


class Review(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True)
    content = models.CharField(db_column='content', max_length=200, blank=True, null=True)
    user = models.ForeignKey(get_user_model(), related_name='review', on_delete=models.CASCADE)
    store = models.ForeignKey(Store, related_name='store', on_delete=models.CASCADE)
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
    review = models.ForeignKey(Review, related_name='review_img', on_delete=models.CASCADE)
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
    review = models.ForeignKey(Review, related_name='tag', on_delete=models.CASCADE, blank=True, null=True)
    TagType = (
        (1, "Product"),
        (2, "Bowl"),
    )
    type = models.IntegerField(db_column='type', choices=TagType, default=1)
    color_index = models.IntegerField(db_column='color_index', blank=True, null=True)
    # 등록, 수정 컬럼 + 데이터 보존 Flag 컬럼
    updt_dt = models.DateTimeField(db_column='updt_dt', auto_now=True)
    insrt_dt = models.DateTimeField(db_column='insrt_dt', auto_now_add=True)
    usage_fg = models.CharField(db_column='usage_fg', max_length=1, blank=True, null=True, default='Y')

    class Meta:
        managed = True
        db_table = 'tag'
        app_label = 'board'
