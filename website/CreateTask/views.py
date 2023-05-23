from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from CreateTask.models import Tasks, Users, Boards
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
import ast

# http://127.0.0.1:8000/tasks/createtask/?name=kek

@csrf_exempt
def task_creator(request):
    try:
        if request.POST:
            request.POST = ast.literal_eval(request.POST['json'])
            author = Users.objects.get(login=request.user)
            executor = Users.objects.get(login=request.POST['executor_login'])
            board = Boards.objects.get(board_name=request.POST['board_name'])
            temp_task = Tasks(task_name=request.POST['task_name'],
                              author=author,
                              executor=executor,
                              board=board,
                              task_create_date=str(datetime.now().date()),
                              status=int(request.POST['status']),
                              task_description=str(request.POST['task_description']))

            temp_task.save()
            print('kek', request.POST)
    except Exception as e:
        print(f"vse upalo, oshibka {e}")
        return HttpResponse(f"vse upalo, oshibka {e}")
    return HttpResponse("<h1>Create task</h1>")
"""
var payload = {
    "executor_login": "valentina94",
    "board_name": "Доска 1",
    "task_name": "Навалить фонка",
    "status": "3",
    "task_description":"надо очень жоска навалить фонка"
    
};

var data = new FormData();
data.append( "json", JSON.stringify( payload ) );

fetch("http://127.0.0.1:8000/tasks/createtask/",
{
    method: "POST",
    body: data
})
"""


@csrf_exempt
def task_editor(request):
    try:
        if request.POST: #curl -d "task_idx=3&executor_login=kek2&board_name=asdascva&task_name=blya&status=1" -X POST http://127.0.0.1:8000/tasks/edittask/

            request.POST = ast.literal_eval(request.POST['json'])
            author = Users.objects.get(login=request.POST['get_post']['author'])
            executor = Users.objects.get(login=request.POST['get_post']['executor_login'])
            task = Tasks.objects.filter(author=author,
                                        task_name=request.POST['get_post']['task_name'],
                                        executor=executor)
            task = task[0]
            request.POST = request.POST['change_post']
            if 'author_login' in request.POST:
                author = Users.objects.get(login=request.POST['author_login'])
                task.author = author
            if 'executor_login' in request.POST:
                executor = Users.objects.get(login=request.POST['executor_login'])
                task.executor = executor
            if 'board_name' in request.POST:
                board = Boards.objects.get(board_name=request.POST['board_name'])
                task.board = board
            if 'task_name' in request.POST:
                task.task_name = request.POST['task_name']
            if 'status' in request.POST:
                task.status = int(request.POST['status'])
            if 'task_description' in request.POST:
                task.status = request.POST['status']
            task.save()
    except Exception as e:
        print(f"vse upalo, oshibka {e}")
        return HttpResponse(f"vse upalo, oshibka {e}")
    return HttpResponse("<h1>Edit task</h1>")

"""
var payload = {
    "get_post":{"executor_login":"valentina94",
               "task_name":"Навалить фонка",
               "author":"lribakov"},
    "change_post":{"executor_login": "valentina94",
                    "board_name": "Доска 1",
                    "task_name": "не Навалить фонка",
                    "status": "3",
                    "task_description":"не надо очень жоска навалить фонка"}
    
};

var data = new FormData();
data.append( "json", JSON.stringify( payload ) );

fetch("http://127.0.0.1:8000/tasks/edittask/",
{
    method: "POST",
    body: data
})
"""
