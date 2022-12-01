from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.serializers import MyTokenSerializer, MyTokenRefreshSerializer


class LoginView(TokenObtainPairView):
    """
    登录视图
    """
    serializer_class = MyTokenSerializer


class MyTokenRefreshView(TokenRefreshView):
    """
    token刷新视图
    """
    serializer_class = MyTokenRefreshSerializer
