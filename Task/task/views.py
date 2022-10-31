from django.shortcuts import render
from rest_framework import viewsets
from yaml import serialize
from .serializers import UserSerializer, IncomeSerializer
from .models import User_data
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view


class UserViewSet(viewsets.ModelViewSet):
    queryset = User_data.objects.all().order_by("Age")
    serializer_class = UserSerializer


@api_view(["PUT"])
def update(request, pk):
    if request.method == "PUT":
        print(request)
        serializer = IncomeSerializer(User_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
