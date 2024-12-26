from django.urls import path
from . import views

urlpatterns = [
    path('user_detail/', views.user_detail, name='user_detail'),  # Handle no user_id
    path("", views.index),
    # path('new_user/', views.new_user),
    # path('index/', views.index),
    # path('user_detail/<int:user_id>/', views.user_detail, name='user_detail'),  # Handle with user_id
    path("", views.index, name="index"),
    path("new_user", views.new_user, name="new_user"),
    path("user_detail/<int:user_id>/", views.user_detail, name="user_detail"),

]
