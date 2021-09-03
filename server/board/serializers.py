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
        fields = ('content', 'user_id', 'store_id')


class ReviewImgSerializers(serializers.ModelSerializer):
    class Meta:
        model = ReviewImg
        fields = ('review_img', 'review_id')

class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('tag_content', 'review_id', 'type')


class MenuSerializers(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('menu', 'store_id')