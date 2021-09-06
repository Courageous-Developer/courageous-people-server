from .models import *
from rest_framework import serializers


# Store CRUD API


class StoreSerializers(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'
        #fields = ('store_name', 'address', 'post', 'picture', 'biz_num', 'latitude', 'longitude', 'user')


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        #fields = ('content', 'user', 'store')


class ReviewImgSerializers(serializers.ModelSerializer):
    class Meta:
        model = ReviewImg
        fields = '__all__'
        #fields = ('review_img', 'review')


class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
        #fields = ('tag_content', 'review', 'type')


class MenuSerializers(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'
        #fields = ('menu', 'store')


class BizAuthSerializers(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = 'biz_num'
