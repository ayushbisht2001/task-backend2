from django.urls import path, include
from .views import *

urlpatterns = [

    path('get-restaurant/', RestaurantView.as_view(), name="get_res"),
    path('add-restaurant/', RestaurantView.as_view(), name="post_res"),
    path('search-restaurant/<str:query>/', search_restaurant, name="search_res"),

]