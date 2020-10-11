from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . serializers import MessageSerializer
from . models import Message

# Create your views here.

def home(request):

	return render(request, 'base/home.html')

# @api_view(['GET'])
# def taskList(request):
# 	tasks = Task.objects.all().order_by('-id')
# 	serializer = TaskSerializer(tasks, many=True)
# 	return Response(serializer.data)

@api_view(['POST'])
def createMessage(request):

	serializer = MessageSerializer(data=request.data)
	
	if serializer.is_valid():
		serializer.save()
	else:
		print('createMessage ERROR')

	return Response(serializer.data)
