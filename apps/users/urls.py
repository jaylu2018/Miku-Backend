from django.urls import path, include

from rest_framework.routers import DefaultRouter

from apps.users import views

router = DefaultRouter()
router.register('users', views.UserViewSet)

urlpatterns = [
    path('users/login', views.LoginView.as_view(), name='login'),
    path('users/token/refresh/', views.MyTokenRefreshView.as_view(), name='refresh'),
    path('users/register/', views.RegisterView.as_view(), name='register'),
    path('', include(router.urls))
]
