
from rest_framework_swagger.views import get_swagger_view

from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import *

schema_view = get_swagger_view(title="API")

router = DefaultRouter()
router.register(r"DishManagement", DishManagementViewSet)
router.register(r"DishCategory", DishCategoryViewSet)
router.register(r"Test", TestViewSet)





urlpatterns = [
    path("sharedVariable/", sharedVariable.as_view()),
        path("HCWVariable/", HCWVariable.as_view()),


    path('hello/', hello),

]
urlpatterns += router.urls  # 将路由器中的所以路由信息追到到django的路由列表中

