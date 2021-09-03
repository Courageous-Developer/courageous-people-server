from django.urls import path
from . import views

urlpatterns = [
    path('store', views.StoreList.as_view(), name='store_list'),
    path('store/<int:pk>', views.StoreDetail.as_view(), name='store_detail'),

    path('review', views.ReviewList.as_view(), name='review_list'),
    path('review/<int:pk>', views.ReviewDetail.as_view(), name='review_detail'),

    path('tag', views.TagList.as_view(), name='tag_list'),
    path('tag/<int:pk>', views.TagDetail.as_view(), name='tag_detail'),

    path('menu', views.MenuList.as_view(), name='menu_list'),
    path('menu/<int:pk>', views.MenuDetail.as_view(), name='menu_detail'),

]