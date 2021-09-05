from .models import *
from rest_framework import serializers


# Store CRUD API


class StoreSerializers(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ('store_name', 'address', 'post', 'picture', 'biz_num', 'latitude', 'longitude', 'user')


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('content', 'user', 'store')


class ReviewImgSerializers(serializers.ModelSerializer):
    class Meta:
        model = ReviewImg
        fields = ('review_img', 'review')


class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('tag_content', 'review', 'type')


class MenuSerializers(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('menu', 'store')


class BizAuthSerializers(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = 'biz_num'
