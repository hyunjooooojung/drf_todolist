from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .models import Todo
from .serializers import TodoSerializer, TodoDetailSerializer, TodoCreateSerializer

class TodoAPIView(APIView):
    def get(self, request):
        todos = Todo.objects.filter(complete=False)
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        # 입력한 데이터(request.data)를 serializer에 넣어준다.
        serializer = TodoCreateSerializer(data=request.data)
        if serializer.is_valid():
            # serializer에 들어온 데이터가 올바른 데이터이면 저장.
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class TodoDetailAPIView(APIView):
    def get(self, request, todo_id):
        todo = get_object_or_404(Todo, id=todo_id)
        serializer = TodoDetailSerializer(todo)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # todo list 수정하기
    def put(self, request, todo_id):
        todo = get_object_or_404(Todo, id=todo_id)
        serializer = TodoCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    # todo list 삭제하기
    def delete(self, request, todo_id):
        todo = get_object_or_404(Todo, id=todo_id)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
        
# 전체 완료 todo 조회
class DoneTodoAPIView(APIView):
    def get(self, request):
        dones = Todo.objects.filter(complete=True)
        serializer = TodoSerializer(dones, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
  
# 완료 todo 상세 목록
class DoneDetailTodoAPIView(APIView):
    def get(self, request, todo_id):
        done = get_object_or_404(Todo, id=todo_id)
        done.complete = True
        done.save()
        serializer = TodoDetailAPIView(done)
        return Response(status=status.HTTP_200_OK)