from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Task
from .serializers import TaskSerializer


class ApiRootView(APIView):
    def get(self, request):
        return Response({"message": "Task Manager API is running."}, status=status.HTTP_200_OK)


class TaskListCreateView(APIView):
    def get(self, request):
        completed = request.query_params.get('completed')
        tasks = Task.objects.all()
        if completed is not None:
            if completed.lower() in ['true', '1']:
                tasks = tasks.filter(completed=True)
            elif completed.lower() in ['false', '0']:
                tasks = tasks.filter(completed=False)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetailView(APIView):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        serializer = TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return Response({'message': 'Task deleted'}, status=status.HTTP_204_NO_CONTENT)
