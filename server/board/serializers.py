from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model


# User
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'nickname', 'password', 'date_of_birth', 'user_type')

    def validate_password(self, value: str) -> str:
        """
        Hash value passed by user.

        :param value: password of a user
        :return: a hashed version of the password
        """
        return make_password(value)
# Store CRUD API


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'
        # fields = ('store_name', 'address', 'post', 'picture', 'biz_num', 'latitude', 'longitude', 'user')


class ReviewSerializer(serializers.ModelSerializer):

    nickname = RegisterSerializer(many=True, read_only=True)

    class Meta:
        model = Review
        fields = ('content', 'user', 'store', 'nickname')


class ReviewImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewImg
        fields = '__all__'
        # fields = ('review_img', 'review')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
        # fields = ('tag_content', 'review', 'type')


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'
        # fields = ('menu', 'store')


class BizAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = 'biz_num'
