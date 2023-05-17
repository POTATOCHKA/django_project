from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from CreateTask.models import Tasks, Users, Boards
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *

# Create your views here.
"""def task_creator(request):
    form = AddPostForm()
    if request.POST:
        print('kek', request.POST)
        print(request.POST['task_name'])
        author = Users.objects.get(pk=int(request.POST['author']))
        executor = Users.objects.get(pk=int(request.POST['executor']))
        board = Boards.objects.get(pk=int(request.POST['board']))
        temp_task = Tasks(task_name=request.POST['task_name'],
                          author=author,
                          executor=executor,
                          board=board,
                          task_create_date=request.POST['task_create_date'],
                          status=request.POST['status'])
        temp_task.save()

    if request.GET:
        print(request.GET)
        idx = request.GET['id']
        print(idx)
        print(Tasks.objects.get(pk=int(idx)))  # http://127.0.0.1:8000/tasks/createtask/?name=kek
        task = Tasks.objects.get(pk=int(idx))
    return render(request, 'CreateTask/add_task.html', {'form': form, 'title': 'Добавление статьи'})"""

@csrf_exempt
def task_creator(request):
    try:
        if request.POST:
            author = Users.objects.get(login=request.POST['author_login'])
            executor = Users.objects.get(login=request.POST['executor_login'])
            board = Boards.objects.get(board_name=request.POST['board_name'])
            temp_task = Tasks(task_name=request.POST['task_name'],
                              author=author,
                              executor=executor,
                              board=board,
                              task_create_date=str(datetime.now().date()),
                              status=int(request.POST['status']))
            temp_task.save()
            print('kek', request.POST) #curl -d "author_login=kek1&executor_login=kek2&board_name=asdascva&task_name=blya&status=1" -X POST http://127.0.0.1:8000/tasks/createtask/
    except Exception as e:
        print(f"vse upalo, oshibka {e}")
        return HttpResponse(f"vse upalo, oshibka {e}")
    return HttpResponse("<h1>Create task</h1>")


@csrf_exempt
def task_editor(request):
    try:
        if request.POST: #curl -d "task_idx=3&executor_login=kek2&board_name=asdascva&task_name=blya&status=1" -X POST http://127.0.0.1:8000/tasks/edittask/
            print('kek', request.POST)
            task = Tasks.objects.get(pk=int(request.POST['task_idx']))
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
            task.save()
    except Exception as e:
        print(f"vse upalo, oshibka {e}")
        return HttpResponse(f"vse upalo, oshibka {e}")
    return HttpResponse("<h1>Edit task</h1>")
