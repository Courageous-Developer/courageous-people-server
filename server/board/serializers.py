from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model


# User
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'nickname', 'password', 'date_of_birth', 'user_type')

    # def validate_password(self, value: str) -> str:
    #     """
    #     Hash value passed by user.
    #
    #     :param value: password of a user
    #     :return: a hashed version of the password
    #     """
    #     return make_password(value)


# CRUD API
class MenuImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuImg
        fields = '__all__'


class MenuSerializer(serializers.ModelSerializer):
    menu_img = MenuImgSerializer(many=True, read_only=True)

    class Meta:
        model = Menu
        fields = ('id', 'menu', 'price', 'store', 'menu_img')


class StoreImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreImg
        fields = '__all__'


class StoreSerializer(serializers.ModelSerializer):
    menu = MenuSerializer(many=True, read_only=True)
    store_img = StoreImgSerializer(many=True, read_only=True)

    class Meta:
        model = Store
        fields = ('id', 'store_name', 'address', 'post', 'latitude', 'longitude', 'user', 'menu', 'store_img')


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


class ReviewNestedSerializer(serializers.ModelSerializer):
    tag = TagSerializer(many=True)
    review_img = ReviewImgSerializer(many=True, read_only=True)

    class Meta:
        model = Review
        fields = ('id', 'content', 'insrt_dt', 'updt_dt', 'user', 'store', 'tag', 'review_img')
        # fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['nickname'] = RegisterSerializer(instance.user).data.get('nickname')
        return response

    def create(self, validated_data):
        tag_data = validated_data.pop('tag')
        review = Review.objects.create(**validated_data)

        for tag in tag_data:
            Tag.objects.create(review=review, **tag)
        return review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'content', 'insrt_dt', 'updt_dt', 'user', 'store')


class BizAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = 'biz_num'
