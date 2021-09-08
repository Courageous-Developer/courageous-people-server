

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


class RegisterView(APIView):
    permission_classes = [AllowAny]

    @csrf_exempt
    def post(self, request, format=None):

        data = JSONParser().parse(request)

        if User.objects.filter(email=data['email'], is_active=1).exists():
            raise exceptions.ParseError("Duplicate email")

        serializer = RegisterSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)


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
