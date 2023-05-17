from django import forms
from .models import *

class AddPostForm(forms.Form):
    task_name = forms.CharField(max_length=255, label="Task name", widget=forms.TextInput(attrs={'class': 'form-input'}))
    author = forms.IntegerField()
    executor = forms.IntegerField()
    board = forms.IntegerField()
    task_create_date = forms.DateField()
    status = forms.IntegerField()


