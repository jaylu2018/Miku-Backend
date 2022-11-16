from django.urls import path
from .views import RegisterView, LoginView, UserView

urlpatterns = [
    path(r'login', LoginView.as_view()),
    path(r'register', RegisterView.as_view()),
    path(r'person/<int:pk>', UserView.as_view()),
]
