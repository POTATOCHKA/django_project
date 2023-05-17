# django_project
1) чтобы поднять у себя сервер, надо настроить базу в settings
2) сделать миграцию (хз)
3) поднять сервак python manage.py runserver
создать таск: 
%%bash
curl -d "author_login=kek1&executor_login=kek2&board_name=asdascva&task_name=aaa&status=1" -X POST http://127.0.0.1:8000/tasks/createtask/
