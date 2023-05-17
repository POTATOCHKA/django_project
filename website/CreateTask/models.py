# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Boards(models.Model):
    board_id = models.AutoField(primary_key=True)
    board_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'boards'


class Comments(models.Model):
    comment_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    task = models.ForeignKey('Tasks', models.DO_NOTHING)
    comment_create_date = models.DateField()
    text = models.TextField()

    class Meta:
        managed = False
        db_table = 'comments'


class Companies(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'companies'


class Histories(models.Model):
    history_id = models.AutoField(primary_key=True)
    task = models.ForeignKey('Tasks', models.DO_NOTHING)
    entry = models.TextField()
    entry_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'histories'


class Tasks(models.Model):
    task_id = models.AutoField(primary_key=True)
    task_name = models.CharField(max_length=100)
    author = models.ForeignKey('Users', models.DO_NOTHING)
    executor = models.ForeignKey('Users', models.DO_NOTHING, related_name='tasks_executor_set')
    board = models.ForeignKey(Boards, models.DO_NOTHING)
    task_create_date = models.DateField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tasks'


class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    surname = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100)
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'users'


class UsersBoards(models.Model):
    user_board_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, models.DO_NOTHING)
    board = models.ForeignKey(Boards, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_boards'


class UsersCompanies(models.Model):
    user_company_id = models.AutoField(primary_key=True)
    company = models.ForeignKey(Companies, models.DO_NOTHING)
    user = models.ForeignKey(Users, models.DO_NOTHING)
    rights = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'users_companies'
