from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.menus.views import MenusView, Department, Role, User,MenusView2

router = DefaultRouter()
router.register(r'menu', MenusView, basename='menus')
router.register(r'getAllMenuByRoleId', MenusView2, basename='menus')
router.register(r'getDepartmentList', Department, basename='getDepartmentList')
router.register(r'getRoleList', Role, basename='getRoleList')
router.register(r'getUserList', User, basename='getUserList')

urlpatterns = [
    path('', include(router.urls)),
]
