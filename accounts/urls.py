from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

# from .views import user_login, register_user, user_logout, MyObtainTokenPairView
from . import views

urlpatterns = [
    path("register/", views.UserRegisterationAPIView.as_view(), name="create-user"),
    path("login/", views.UserLoginAPIView.as_view(), name="login-user"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    path("logout/", views.UserLogoutAPIView.as_view(), name="logout-user"),
    # path("register/", register_user, name="register"),
    # # path("login/", user_login, name="login"),
    # path("login/", MyObtainTokenPairView.as_view(), name="token_obtain_pair"),
    # path("login/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # path("logout/", user_logout, name="logout"),
]
