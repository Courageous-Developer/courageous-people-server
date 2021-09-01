from .models import *
from rest_framework import serializers

# Store CRUD API


class StoreSerializers(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ('store_name', 'address', 'post', 'picture', 'biz_num', 'user_id')

class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('content', 'user_id', 'store_id')

class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('content', 'user_id', 'store_id')

class ReviewImgSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review_Img
        fields = ('review_img', 'review_id')