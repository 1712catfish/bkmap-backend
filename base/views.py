from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Post, Task
from .serializers import PostSerializer, TaskSerializer


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
