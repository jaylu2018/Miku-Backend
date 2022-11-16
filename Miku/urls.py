from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.documentation import include_docs_urls

from drf_yasg2.views import get_schema_view
from drf_yasg2 import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="API接口文档平台",  # 必传
        default_version='v1',  # 必传
        description="这是一个美轮美奂的接口文档",
        terms_of_service="http://lianlianpay.com",
        contact=openapi.Contact(email="luyh@lainlianpay.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    # permission_classes=(permissions.AllowAny,),   # 权限类
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # 添加接口文档平台的路由条目
    path('docs/', include_docs_urls(title='接口文档', description='')),
    # re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # path('api/', include('rest_framework.urls')),
    path('user/', include('apps.users.urls')),
    # path('', include('apps.projects.urls')),
    path('', include('apps.menus.urls')),
    path('', include('apps.envs.urls')),
    # path('', include('testsuits.urls')),
    # path('', include('interfaces.urls')),
    # path('', include('debugtalks.urls')),
    # path('', include('reports.urls')),
    # path('', include('testcases.urls')),
    # path('', include('summary.urls')),
    # path('', include('configures.urls')),
]
