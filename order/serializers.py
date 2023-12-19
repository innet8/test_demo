from rest_framework.serializers import ModelSerializer
from .models import *
from rest_framework import serializers
from .serializers import *

from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.decorators import action


class DishManagementSerializer(ModelSerializer):
    class Meta:
        model = DishManagement
        fields = "__all__"


class  TestSerializer(ModelSerializer):
    class Meta:
        model = Test
        fields = "__all__"





class sharedVariableSerializer(serializers.Serializer):
    Id = serializers.IntegerField()

    class Meta:
        fields = "__all__"


class sharedVariable(GenericAPIView):
    serializer_class = sharedVariableSerializer

    def get(self, request, *args, **krgs):
        data = {"message": "GET 请求成功"}

        return Response(data, status=status.HTTP_200_OK)



class HCWSerializer(serializers.Serializer):
    Id = serializers.IntegerField()
 
    class Meta:
        fields = "__all__"


class HCWVariable(GenericAPIView):
    serializer_class = HCWSerializer

    def get(self, request, *args, **krgs):
        data = {"message": "GET 请求成功"}

        return Response(data, status=status.HTTP_200_OK)







class DishCategorySerializer(ModelSerializer):
    class Meta:
        model = DishCategory
        fields = "__all__"
