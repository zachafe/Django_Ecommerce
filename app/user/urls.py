from django.urls import path
from app.user.views import *

app_name = 'user'

urlpatterns = [
    # user
    path('list/', UserListView.as_view(), name='user_list'),
    path('add/', UserCreateView.as_view(), name='user_create'),
    path('update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    # path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),
]