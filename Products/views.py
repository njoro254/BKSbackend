from django.shortcuts import render
from .models import Product
from .serializer import ProductSerializer
from rest_framework import viewsets
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView
from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser,FormParser,JSONParser)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer