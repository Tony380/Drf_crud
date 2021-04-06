from django.shortcuts import render
from .serializers import TaskSerializer
from .models import Task
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/task-list',
        'Detail': '/task-detail/<int:pk>',
        'Create': '/task-create',
        'Update': '/task-update/<int:pk>',
        'Delete': '/task-delete/<int:pk>',
    }

    return Response(api_urls)


@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def taskDetail(request, pk):
    tasks = Task.objects.get(pk=pk)
    serializer = TaskSerializer(tasks, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def taskUpdate(request, pk):
    task = Task.objects.get(pk=pk)
    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return Response('Item successfully deleted!')