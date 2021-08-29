from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.parsers import JSONParser
from rest_framework import exceptions
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

class StoreList(APIView):

    @csrf_exempt
    def get(self, request, format=None):
        query_set = Store.objects.all()
        serializer = StoreSerializers(query_set, many=True)
        return JsonResponse(serializer.data, status=200, safe=False)

    @csrf_exempt
    def post(self, request, format=None):

        permission_classes = (IsAuthenticated,)

        data = JSONParser().parse(request)

        if Store.objects.filter(biz_num=data['biz_num'], usage_fg='Y').exists():
            raise exceptions.ParseError("Duplicate BizNum")

        serializer = StoreSerializers(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)


class StoreDetail(APIView):

    @csrf_exempt
    def get(self, request, pk, format=None):
        obj = Store.objects.get(id=pk)
        serializer = StoreSerializers(obj)
        return JsonResponse(serializer.data, status=200)

    @csrf_exempt
    def put(self, request, pk, format=None):
        permission_classes = (IsAuthenticated,)

        obj = Store.objects.get(id=pk)
        data = JSONParser().parse(request)

        serializer = StoreSerializers(obj, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)

    @csrf_exempt
    def delete(self, request, pk, format=None):
        obj = Store.objects.get(id=pk)
        obj.usage_fg = 'N'
        obj.save()
        return HttpResponse(status=204)
