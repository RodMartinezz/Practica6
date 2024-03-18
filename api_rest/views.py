from django.shortcuts import render

# Create your views here.
from .serializer import CervezaSerializer
from .models import Cerveza
from rest_framework import viewsets

class CervezaViewset(viewsets.ModelViewSet):
    queryset=Cerveza.objects.all()
    serializer_class=CervezaSerializer
