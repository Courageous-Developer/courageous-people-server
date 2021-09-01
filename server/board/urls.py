from django.urls import path
from . import views

urlpatterns = [
    path('store', views.StoreList.as_view(), name='store_list'),
    path('store/<int:pk>', views.StoreDetail.as_view(), name='store_detail'),
    path('review/<int:pk>', views.ReviewList.as_view(), name='review_list'),

]