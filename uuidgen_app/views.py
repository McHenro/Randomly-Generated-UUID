from django.shortcuts import render
from .models import Task
from .serializers import TaskSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import  status 


class TaskView(APIView):
    def get(self, request):
        object_collection = dict()
        Task.objects.create()
        task = Task.objects.all()
        serializer = TaskSerializer(task, many=True)
        # collecting all objects and storing in the empty dictionary " object_collection"
        for object in serializer.data:
            object_collection[object['created_at']] = object['uuid']
        return Response(object_collection, status= status.HTTP_200_OK)
