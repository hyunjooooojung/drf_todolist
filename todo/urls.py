from django.urls import path
from .views import TodoAPIView,TodoDetailAPIView, DoneTodoAPIView, DoneDetailTodoAPIView

urlpatterns = [
    path('todo/', TodoAPIView.as_view()),
    path('todo/<int:todo_id>/',TodoDetailAPIView.as_view()),
    path('done/', DoneTodoAPIView.as_view()),
    path('done/<int:todo_id>/', DoneDetailTodoAPIView.as_view()),
]