
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.


@api_view(['GET'])
def index(request):
	urls = {
		'api/': 'route index',
		'/view-tasks/': 'view current tasks',
		'/create-task/<str:name>': 'create new task',
		'/delete-task/<int:id>': 'delete task',
		'/task-detail/<int:id>': 'view task details'
	}
	return Response(urls)
