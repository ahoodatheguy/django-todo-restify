from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='api-index'),
	path('view-tasks/', views.view_tasks, name='api-tasks'),
	path('create-task/', views.create_task, name='create-task'),
	path('delete-task/<int:id>', views.delete_task, name='delete-task'),
	path('task-detail/<int:id>', views.task_detail, name='task-detail')
]
