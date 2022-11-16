from django.urls import path, include
from .views import EnvsViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'envs', EnvsViewSet, basename='envs')

urlpatterns = [
    path('', include(router.urls)),
]
