from django.urls import path
from .views import TaskListCreateView, TaskDetailView, ApiRootView

urlpatterns = [
    path('', ApiRootView.as_view()),              # GET /api/ => API status
    path('tasks/', TaskListCreateView.as_view()), # GET, POST /api/tasks/
    path('tasks/<int:pk>/', TaskDetailView.as_view()), # GET, PUT, DELETE /api/tasks/<id>/
]
