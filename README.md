# django_project
чтобы поднять у себя сервер
1) надо настроить базу в settings
2) сделать миграцию (наверное)
3) поднять сервак python manage.py runserver


создать таск (author_login, executor_login, board_name --- уникальные):
```
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
```
изменить таск по индексу таска можно передать любые поля для изменения: 
```
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
})```