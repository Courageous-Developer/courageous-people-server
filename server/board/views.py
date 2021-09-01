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


# review API
# (1) 리뷰 보여주기
# (2) 리뷰 쓰기
# (2-2) 리뷰 수정하기
# (3) 리뷰 삭제하기
class ReviewList(APIView):

    # 리뷰 보여주기

    # pk로 store_id 를 받고 store_id에 따른 review를 보여준다

    @csrf_exempt
    def get(self, request, pk, format=None):
        obj = Store.objects.get(store_id=pk)
        serializer = ReviewSerializers(obj, many=True)
        return JsonResponse(serializer.data, status=200, safe=False)

    # 리뷰 쓰기
    @csrf_exempt
    def post(self, request, format=None):

        permission_classes = (IsAuthenticated,)

        data = JSONParser().parse(request)

        if Review.objects.filter(store_id=data['store_id'], usage_fg='Y').exists():
            raise exceptions.ParseError("Duplicate Store")

        serializer = ReviewSerializers(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)

    # 리뷰 수정하기
    @csrf_exempt
    def put(self, request, pk, format=None):
        permission_classes = (IsAuthenticated,)

        obj = Review.objects.get(id=pk)
        data = JSONParser().parse(request)

        serializer = StoreSerializers(obj, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)

    # 리뷰 삭제
    @csrf_exempt
    def delete(self, request, pk, format=None):
        obj = Review.objects.get(id=pk)
        obj.usage_fg = 'N'
        obj.save()
        return HttpResponse(status=204)


# review img API
# (1) 이미지 보여주기
# (2) 이미지 넣기
# (2-2) 이미지 수정하기
# (3) 이미지 삭제하기

class ReviewImgList(APIView):
    # 이미지 보여주기
    #
    # 가게 페이지에서 리뷰에 맞는  이미지를 보여줘야한다.
    # 가게id, 리뷰id 에 맞게 보여주기
    @csrf_exempt
    def get(self, request, pk, format=None):
        obj = Review_Img.objects.get(id=pk)
        serializer = ReviewImgSerializers(obj)
        return JsonResponse(serializer.data, status=200)

    # 이미지 올리기
    @csrf_exempt
    def post(self, request, format=None):

        permission_classes = (IsAuthenticated,)

        data = JSONParser().parse(request)

        if Review_Img.objects.filter(review_id=data['review_id'], usage_fg='Y').exists():
            raise exceptions.ParseError("Duplicate review_id")

        serializer = ReviewImgSerializers(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)
    # 이미지 수정하기
    @csrf_exempt
    def put(self, request, pk, format=None):
        permission_classes = (IsAuthenticated,)

        obj = ReviewList.objects.get(id=pk)
        data = JSONParser().parse(request)

        serializer = ReviewImgSerializers(obj, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)

    # 이미지 삭제
    @csrf_exempt
    def delete(self, request, pk, format=None):
        obj = Review_Img.objects.get(id=pk)
        obj.usage_fg = 'N'
        obj.save()
        return HttpResponse(status=204)
