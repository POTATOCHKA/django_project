from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
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
        if request.POST:
            request.POST = ast.literal_eval(request.POST['json'])
            task = Tasks.objects.filter(pk=request.POST['get_post']['task_id'])
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


def parse_user_fieds(user):
    output_dict = {'user_id': user.pk,
                   'surname': user.surname,
                   'user_name': user.user_name,
                   'patronymic': user.patronymic,
                   'login': user.login,
                   'email': user.email}
    return output_dict


def parser_board_tasks(tasks):
    tasks = list(tasks)
    output_dict = {}
    for task in tasks:
        try:
            print(task.author)
            # author = Users.objects.get(login=task.author)
            # executor = Users.objects.get(login=task.executor)
            output_dict.update({task.pk: {'task_id': task.pk,
                                          'task_name': task.task_name,
                                          'author': parse_user_fieds(task.author),
                                          'executor': parse_user_fieds(task.executor),
                                          'task_create_date': str(task.task_create_date),
                                          'status': task.status,
                                          'task_description': task.task_description}})
        except Exception as e:
            print(e)
    return output_dict


@csrf_exempt
def boards_getter(request):
    if request.GET:
        print(request.user)
        #print(list(Users.objects.all())[0].login)
        if request.GET['name']:
            author = Users.objects.get(login=request.GET['name'])
        else:
            author = Users.objects.get(login=request.user)
        print(author)
        getted_tasks = Tasks.objects.filter(author=author)
        getted_tasks = list(getted_tasks)
        boards = []
        for task in getted_tasks:
            boards.append(task.board)
        board_to_task = {}
        for board in boards:
            board_tasks = Tasks.objects.filter(board=board)
            board_to_task.update({board.pk: {'board_name': board.board_name,
                                             'board_tasks': parser_board_tasks(board_tasks)}})

        print(board_to_task)
        return JsonResponse(board_to_task)
    return HttpResponse("pass GET request")
