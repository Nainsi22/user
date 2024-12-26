from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [

    path("", views.index),
    path('admin/', admin.site.urls),
    path('new_user/', views.new_user),
    path('index/', views.index),
    path('user_detail/', views.user_detail, name='user_detail'),  # Optional user_id
    path('user_list/', views.user_list, name='user_list'),
    # path('user_detail/<int:id>/', views.user_detail, name='user_detail'),
    path("user_detail/<int:user_id>/", views.user_detail, name='user_detail'),
    path('search_user/', views.search_user, name='search_user'),
    path('users/', views.list_users, name='list_users'),
    path('hello/', views.hello, name='hello'),
]
