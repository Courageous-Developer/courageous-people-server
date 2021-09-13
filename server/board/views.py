from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.parsers import JSONParser
from rest_framework import exceptions
from django.views.decorators.csrf import csrf_exempt
import json
import requests
from django.contrib.auth import get_user_model

# Create your views here.

class StoreList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    @csrf_exempt
    def get(self, request, format=None):
        query_set = Store.objects.filter(usage_fg="Y")
        serializer = StoreSerializer(query_set, many=True)
        return JsonResponse(serializer.data, status=200, safe=False)

    @csrf_exempt
    def post(self, request, format=None):
        data = JSONParser().parse(request)

        serializer = StoreSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)


class StoreDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    @csrf_exempt
    def get(self, request, pk, format=None):
        obj = Store.objects.get(id=pk, usage_fg="Y")
        serializer = StoreSerializer(obj)
        return JsonResponse(serializer.data, status=200)

    @csrf_exempt
    def put(self, request, pk, format=None):
        obj = Store.objects.get(id=pk, usage_fg="Y")
        data = JSONParser().parse(request)

        serializer = StoreSerializer(obj, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)

    @csrf_exempt
    def delete(self, request, pk, format=None):
        obj = Store.objects.get(id=pk, usage_fg="Y")
        obj.usage_fg = 'N'
        obj.save()
        return HttpResponse(status=204)


class StoreImg(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    @csrf_exempt
    def post(self, request, pk, format=None):
        img = request.FILES['store_img']


# review API
# (1) 리뷰 보여주기
# (2) 리뷰 쓰기
# (2-2) 리뷰 수정하기
# (3) 리뷰 삭제하기
class ReviewList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    @csrf_exempt
    def get(self, request, format=None):
        query_set = Review.objects.filter(usage_fg="Y")
        serializer = ReviewSerializer(query_set, many=True)
        return JsonResponse(serializer.data, status=200, safe=False)

    @csrf_exempt
    def post(self, request, format=None):
        data = JSONParser().parse(request)

        serializer = ReviewSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)


class ReviewDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    @csrf_exempt
    def get(self, request, pk, format=None):  # store_id에 해당하는 review들만 반환.
        query_set = Review.objects.filter(store_id=pk, usage_fg="Y")
        serializer = ReviewSerializer(query_set, many=True)
        return JsonResponse(serializer.data, status=200, safe=False)

    # 리뷰 수정하기
    @csrf_exempt
    def put(self, request, pk, format=None):
        obj = Review.objects.get(id=pk, usage_fg="Y")
        data = JSONParser().parse(request)

        serializer = ReviewSerializer(obj, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)

    # 리뷰 삭제
    @csrf_exempt
    def delete(self, request, pk, format=None):
        obj = Review.objects.get(id=pk, usage_fg="Y")
        obj.usage_fg = 'N'
        obj.save()
        return HttpResponse(status=204)


# review img API
# (1) 이미지 보여주기
# (2) 이미지 넣기
# (2-2) 이미지 수정하기
# (3) 이미지 삭제하기

class ReviewImgList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    # 이미지 보여주기
    #
    # 가게 페이지에서 리뷰에 맞는  이미지를 보여줘야한다.
    # 가게id, 리뷰id 에 맞게 보여주기

    @csrf_exempt
    def get(self, request, pk, format=None):
        obj = ReviewImg.objects.get(id=pk, usage_fg="Y")
        serializer = ReviewImgSerializer(obj)
        return JsonResponse(serializer.data, status=200)

    # 이미지 올리기
    @csrf_exempt
    def post(self, request, format=None):

        data = JSONParser().parse(request)

        if ReviewImg.objects.filter(review_id=data['review_id'], usage_fg='Y').exists():
            raise exceptions.ParseError("Duplicate review_id")

        serializer = ReviewImgSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)

    # 이미지 수정하기
    @csrf_exempt
    def put(self, request, pk, format=None):

        obj = ReviewList.objects.get(id=pk, usage_fg="Y")
        data = JSONParser().parse(request)

        serializer = ReviewImgSerializer(obj, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)

    # 이미지 삭제
    @csrf_exempt
    def delete(self, request, pk, format=None):
        obj = ReviewImg.objects.get(id=pk, usage_fg="Y")
        obj.usage_fg = 'N'
        obj.save()
        return HttpResponse(status=204)


# Tag API
# (1) Tag 보여주기
# (2) Tag 입력하기

# (3) Tag 수정하기
# (4) Tag 삭제하기
class TagList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    @csrf_exempt
    def get(self, request, format=None):
        query_set = Tag.objects.filter(usage_fg="Y")
        serializer = TagSerializer(query_set, many=True)
        return JsonResponse(serializer.data, status=200, safe=False)

    @csrf_exempt
    def post(self, request, format=None):
        data = JSONParser().parse(request)

        serializer = TagSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)


class TagDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    @csrf_exempt
    def put(self, request, pk, format=None):
        obj = Tag.objects.get(id=pk, usage_fg="Y")
        data = JSONParser().parse(request)

        serializer = TagSerializer(obj, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)

    @csrf_exempt
    def delete(self, request, pk, format=None):
        obj = Tag.objects.get(id=pk, usage_fg="Y")
        obj.usage_fg = 'N'
        obj.save()
        return HttpResponse(status=204)


# Menu API
# (1) Menu 보여주기
# (2) Menu 입력하기

# (3) Menu 수정하기
# (4) Menu 삭제하기
class MenuList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    # (1) Menu 보여줄 때,
    @csrf_exempt
    def get(self, request, format=None):
        query_set = Menu.objects.filter(usage_fg="Y")
        serializer = MenuSerializer(query_set, many=True)
        return JsonResponse(serializer.data, status=200, safe=False)

    @csrf_exempt
    def post(self, request, format=None):
        data = JSONParser().parse(request)

        serializer = MenuSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)


class MenuDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    @csrf_exempt
    def put(self, request, pk, format=None):
        obj = Menu.objects.get(id=pk, usage_fg="Y")
        data = JSONParser().parse(request)

        serializer = MenuSerializer(obj, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)

    @csrf_exempt
    def delete(self, request, pk, format=None):
        obj = Menu.objects.get(id=pk, usage_fg="Y")
        obj.usage_fg = 'N'
        obj.save()
        return HttpResponse(status=204)


class BizAuth(APIView):  # 사업자 등록번호 검증 API

    @csrf_exempt
    def patch(self, request, pk, format=None):

        try:
            dic = JSONParser().parse(request)

            if Store.objects.filter(biz_num=dic['biz_num'], usage_fg='Y').exists():
                raise exceptions.ParseError("Duplicate BizNum")

            api_key = "d21gTtDAjK7W6WpSvPSCMl6C%2B%2BEzHrSAEPi%2BSYCXSF7gsn9h62IYlVKT397Sx%2BYJOsN9ztH93J9qzNMaMpo9qg%3D%3D"
            headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
            url = "https://api.odcloud.kr/api/nts-businessman/v1/status?serviceKey=" + api_key
            body = {

                "b_no": [
                    dic["biz_num"]
                ]
            }
            res = requests.post(url, data=json.dumps(body), headers=headers)

            if res.status_code == 200:
                obj = Store.objects.get(id=pk, usage_fg="Y")
                serializer = StoreSerializer(obj, data=dic, partial=True)

                if serializer.is_valid():
                    serializer.save()
                return HttpResponse(res, content_type='application/json')
        except:
            return HttpResponse(status=400)
