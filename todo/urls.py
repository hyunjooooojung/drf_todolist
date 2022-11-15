from django.urls import path
from .views import TodoAPIView,TodoDetailAPIView

urlpatterns = [
    path('todo/', TodoAPIView.as_view()),
    path('todo/<int:todo_id>/',TodoDetailAPIView.as_view()),
]