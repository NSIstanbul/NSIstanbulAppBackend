from django.urls import path
from .views import UserLoginAPIView, UserLogoutAPIView

app_name = 'accounts_api'

urlpatterns = [
    path('login/', UserLoginAPIView.as_view(), name='login'),
    path('logout/', UserLogoutAPIView.as_view(), name='logout')
]