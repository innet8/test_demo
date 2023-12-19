from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render
 
def hello(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)

class DishManagementViewSet(ModelViewSet):
    queryset = DishManagement.objects.all()
    serializer_class = DishManagementSerializer
    # 过滤
    filter_fields = ("Id", "name")
    # 排序
    ordering_fields = "Id"

    # 自定义方法
    @action(methods=["post"], detail=False, url_path="exec_task")
    def exec_task(self, request, *args, **kwargs):
        print(request.method, args, kwargs, request.data)
        dd = {"w": "ww", "ee": "ttt"}

        return Response(dd)


class TestViewSet(ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    # 过滤
    filter_fields = ("Id", "name")
    # 排序
    ordering_fields = "Id"


    # 自定义方法
    @action(methods=["post"], detail=False, url_path="qq")
    def exec_task(self, request, *args, **kwargs):
        print(request.method, args, kwargs, request.data)
        dd = {"w": "ww", "ee": "ttt"}

        return Response(dd)
    

class DishCategoryViewSet(ModelViewSet):
    queryset = DishCategory.objects.all()
    serializer_class = DishManagementSerializer
    # 过滤
    filter_fields = ("Id", "name")
    # 排序
    ordering_fields = "Id"





