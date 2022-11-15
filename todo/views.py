from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .models import Todo
from .serializers import TodoSerializer

class TodoAPIView(APIView):
    def get(self, request):
        todos = Todo.objects.filter(complete=False)
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)