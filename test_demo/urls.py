"""test_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from django.urls import path
from django.views.static import serve
from django.conf import settings
from rest_framework_jwt.views import obtain_jwt_token
desc = """

# 登陆相关
```bash
# 普通登陆认证
curl -X 'GET'  'http://127.0.0.1:8000/order/DishManagement/'   -H 'accept: application/json'  -u admin:qq

# jwt认证
curl -X 'GET' 'http://127.0.0.1:8000/order/DishManagement/' -H 'accept: application/json'  -H "Authorization: jwt  $token"  
 


```


"""
schema_view = get_schema_view(
    openapi.Info(
        title="点餐系统 API",  # 名称
        default_version="版本 v1.0.0",  # 版本
        description=desc,  # 项目描述
    ),
    public=True,
)
urlpatterns = [
    path('admin/', admin.site.urls),
        path("order/", include(("order.urls", "order"))),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
            path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),
    path("api-jwt-auth/", obtain_jwt_token),

]
