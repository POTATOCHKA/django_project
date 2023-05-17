# django_project
чтобы поднять у себя сервер
1) надо настроить базу в settings
2) сделать миграцию (наверное)
3) поднять сервак python manage.py runserver


создать таск (author_login, executor_login, board_name --- уникальные): 
```
curl -d "author_login=kek1&executor_login=kek2&board_name=asdascva&task_name=aaa&status=1" -X POST http://127.0.0.1:8000/tasks/createtask/
```
изменить таск по индексу таска можно передать любые поля для изменения: 
```
curl -d "task_idx=3&executor_login=kek2&board_name=asdascva&task_name=blya&status=1" -X POST http://127.0.0.1:8000/tasks/edittask/```
```
