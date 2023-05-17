from django.urls import path

from .views import *
urlpatterns = [
    path('createtask/', task_creator), # http://127.0.0.1:8000/tasks/createtask/
    path('edittask/', task_editor) # http://127.0.0.1:8000/tasks/edittask/
]