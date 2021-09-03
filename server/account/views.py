from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from .models import *
from rest_framework.parsers import JSONParser
from rest_framework import exceptions
from django.views.decorators.csrf import csrf_exempt