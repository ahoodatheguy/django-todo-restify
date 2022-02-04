from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task
from api import serializers

# Create your views here.


@api_view(['GET'])
def index(request):
	urls = {
		'api/': 'route index',
		'/view-tasks/': 'view current tasks',
		'/create-task/': 'create new task',
		'/delete-task/<int:id>': 'delete task',
		'/task-detail/<int:id>': 'view task details'
	}
	return Response(urls)


@api_view(['GET'])
def view_tasks(request):
	tasks = Task.objects.all()
	serializer = TaskSerializer(tasks, many=True)
	return Response(serializer.data)


@api_view(['GET'])
def task_detail(request, id):
	tasks = Task.objects.get(id=id)
	serializer = TaskSerializer(tasks, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def create_task(request):
	serializer = TaskSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def delete_task(request, id):
	task = Task.objects.get(id=id)
	task.delete()

	return Response(f'Successfully deleted task {id}')
