
from rest_framework import serializers

from app_todo.models import Task_Todo

class  TaskTodoSerializer( serializers.ModelSerializer):
  class Meta:
    model = Task_Todo
    fields=('id','title','completed')

    # fields=('__all__')