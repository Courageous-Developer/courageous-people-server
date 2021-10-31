import os

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.parsers import JSONParser
from rest_framework import exceptions
from django.views.decorators.csrf import csrf_exempt
import json
import requests
from django.contrib.auth import get_user_model
from .custom_storage import MediaStorage


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
    def post(self, request, format=None):
        img = request.FILES['store_img']
        store = request.POST['store']

        file_directory_within_bucket = 'store_upload_files/{store_id}'.format(store_id=store)

        # synthesize a full file path; note that we included the filename
        file_path_within_bucket = os.path.join(
            file_directory_within_bucket,
            img.name
        )

        media_storage = MediaStorage()

        if not media_storage.exists(file_path_within_bucket):  # avoid overwriting existing file
            media_storage.save(file_path_within_bucket, img)
            file_url = media_storage.url(file_path_within_bucket)

            data = {
                'store_img': file_url,
                'store': store
            }
            serializer = StoreImgSerializer(data=data)

            if serializer.is_valid():
                serializer.save()

            return JsonResponse({
                'message': 'OK',
                'fileUrl': file_url,
            })
        else:
            return JsonResponse({
                'message': 'Error: file {filename} already exists at {file_directory} in bucket {bucket_name}'.format(
                    filename=img.name,
                    file_directory=file_directory_within_bucket,
                    bucket_name=media_storage.bucket_name
                ),
            }, status=400)


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

class ReviewImg(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    @csrf_exempt
    def post(self, request, format=None):
        img = request.FILES['review_img']
        review = request.POST['review']

        file_directory_within_bucket = 'review_upload_files/{review_id}'.format(review_id=review)

        # synthesize a full file path; note that we included the filename
        file_path_within_bucket = os.path.join(
            file_directory_within_bucket,
            img.name
        )

        media_storage = MediaStorage()

        if not media_storage.exists(file_path_within_bucket):  # avoid overwriting existing file
            media_storage.save(file_path_within_bucket, img)
            file_url = media_storage.url(file_path_within_bucket)

            data = {
                'review_img': file_url,
                'review': review
            }
            serializer = ReviewImgSerializer(data=data)

            if serializer.is_valid():
                serializer.save()

            return JsonResponse({
                'message': 'OK',
                'fileUrl': file_url,
            })
        else:
            return JsonResponse({
                'message': 'Error: file {filename} already exists at {file_directory} in bucket {bucket_name}'.format(
                    filename=img.name,
                    file_directory=file_directory_within_bucket,
                    bucket_name=media_storage.bucket_name
                ),
            }, status=400)


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
class Menu(APIView):
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


class MenuList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    @csrf_exempt
    def post(self, request, format=None):  # 여러 Row 한번에 생성.
        data = JSONParser().parse(request)

        try:
            for obj in data['menu_list']:
                serializer = MenuSerializer(data=obj)
                if serializer.is_valid():
                    serializer.save()

            return JsonResponse(data, status=201)

        except:
            return JsonResponse(status=400)


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


class MenuImg(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    @csrf_exempt
    def post(self, request, format=None):
        img = request.FILES['menu_img']
        menu = request.POST['menu']

        file_directory_within_bucket = 'menu_upload_files/{menu_id}'.format(menu_id=menu)

        # synthesize a full file path; note that we included the filename
        file_path_within_bucket = os.path.join(
            file_directory_within_bucket,
            img.name
        )

        media_storage = MediaStorage()

        if not media_storage.exists(file_path_within_bucket):  # avoid overwriting existing file
            media_storage.save(file_path_within_bucket, img)
            file_url = media_storage.url(file_path_within_bucket)

            data = {
                'menu_img': file_url,
                'menu': menu
            }
            serializer = MenuImgSerializer(data=data)

            if serializer.is_valid():
                serializer.save()

            return JsonResponse({
                'message': 'OK',
                'fileUrl': file_url,
            })
        else:
            return JsonResponse({
                'message': 'Error: file {filename} already exists at {file_directory} in bucket {bucket_name}'.format(
                    filename=img.name,
                    file_directory=file_directory_within_bucket,
                    bucket_name=media_storage.bucket_name
                ),
            }, status=400)


class BizAuth(APIView):  # 사업자 등록번호 검증 API

    permission_classes = [AllowAny]

    @csrf_exempt
    def post(self, request, format=None):

        try:
            dic = JSONParser().parse(request)

            api_key = "d21gTtDAjK7W6WpSvPSCMl6C%2B%2BEzHrSAEPi%2BSYCXSF7gsn9h62IYlVKT397Sx%2BYJOsN9ztH93J9qzNMaMpo9qg%3D%3D"
            headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
            url = "https://api.odcloud.kr/api/nts-businessman/v1/status?serviceKey=" + api_key
            body = {

                "b_no": [
                    dic["biz_num"]
                ]
            }
            res = requests.post(url, data=json.dumps(body), headers=headers)

            if eval(res.text)['data'][0]['b_stt'] != "":
                return HttpResponse(res, content_type='application/json')
            else:
                return HttpResponse("국세청에 등록되지 않은 사업자등록번호입니다.", status=400)
        except:
            return HttpResponse(status=400)


class StoreVerifyView(APIView):

    @csrf_exempt
    def post(self, request):
        data = JSONParser().parse(request)
        try:
            obj = Store.objects.get(store_name=data['store_name'], address=data['address'], usage_fg="Y")

            if obj:
                serializer = StoreSerializer(obj)
                return JsonResponse(serializer.data, status=200, safe=False)

        except Exception:
            return HttpResponse("Not found", status=404)
