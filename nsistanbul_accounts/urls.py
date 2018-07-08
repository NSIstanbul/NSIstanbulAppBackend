from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = 'accounts_api'

urlpatterns = [
    # path('login/', UserLoginAPIView.as_view(), name='login'),
    # path('logout/', UserLogoutAPIView.as_view(), name='logout'),
    path('token/', TokenObtainPairView.as_view(), name='token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]