from .models import *
from rest_framework import serializers

# Store CRUD API


class StoreSerializers(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ('store_name', 'address', 'post', 'picture', 'biz_num', 'user_id')
