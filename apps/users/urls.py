from django.urls import path
from . import views

urlpatterns = [
    path('users/login/', views.LoginView.as_view(), name='login'),
    path('users/token/refresh/', views.MyTokenRefreshView.as_view(), name='refresh')
]
