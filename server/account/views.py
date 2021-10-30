# Create your views here.

from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import *
from .serializers import *
from rest_framework.parsers import JSONParser
from rest_framework import exceptions
from django.views.decorators.csrf import csrf_exempt
from django.core.validators import validate_email
from django.shortcuts import render
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from.token import account_activation_token


class RegisterView(APIView):
    permission_classes = [AllowAny]

    @csrf_exempt
    def post(self, request, format=None):

        data = JSONParser().parse(request)

        if User.objects.filter(email=data['email'], is_active=1).exists():
            raise exceptions.ParseError("Duplicate email")

        data['is_active'] = 0

        serializer = RegisterSerializer(data=data)



        if serializer.is_valid():
            serializer.save()
            current_site = get_current_site(request)
            domain = current_site.domain
            #uidb64 = urlsafe_base64_encode(force_bytes(serializer.data['id']))
            #tokens = account_activation_token.make_token(serializer.data)

            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)



#class Activate(APIView):
    #@csrf_exempt
    #def get(self, request, uidb64, token):

class LogoutView(APIView):

    @csrf_exempt
    def post(self, request):
        try:
            data = JSONParser().parse(request)
            refresh_token = data['refresh']
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class CustomTokenObtainPairView(TokenObtainPairView):
    # Replace the serializer with your custom
    serializer_class = CustomTokenObtainPairSerializer


class NameVerifyView(APIView):
    permission_classes = [AllowAny]

    @csrf_exempt
    def post(self, request):
        data = JSONParser().parse(request)

        if User.objects.filter(nickname=data['nickname'], is_active=1).exists():
            return HttpResponse("Duplicate nickname", status=400)
        else:
            return HttpResponse(status=200)


class UserView(APIView):

    @csrf_exempt
    def get(self, request):
        try:
            email = request.GET['email']

            try:
                obj = User.objects.get(email=email)
            except Exception:
                return HttpResponse("Does Not Exist", status=400)

            serializer = RegisterSerializer(obj)
            return JsonResponse(serializer.data, status=200)

        except Exception:
            return HttpResponse("Null Parameter", status=400)
