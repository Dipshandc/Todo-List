from django.shortcuts import render
from rest_framework import generics
from .serializers import TaskSerializer
from .models import *

class Tasklist(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer