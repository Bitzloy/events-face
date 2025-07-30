from django.urls import path

from .views import CustomTokenRefreshView, LoginAPIView, LogoutAPIView, RegisterAPIView

urlpatterns = [
    path("register", RegisterAPIView.as_view(), name="register"),
    path("login", LoginAPIView.as_view(), name="login"),
    path("logout", LogoutAPIView.as_view(), name="logout"),
    path("token/refresh", CustomTokenRefreshView.as_view(), name="token_refresh"),
]
