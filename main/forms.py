from django import forms
from .models import Task

class CreateNewTask(forms.ModelForm):
    identified = forms.CharField(label='Идентификатор', widget=forms.TextInput(attrs={'placeholder': 'Идентификатор'}))
    in_wait_status = forms.BooleanField(initial=False, required=False)
    manager = forms.CharField(label='Менеджер', widget=forms.TextInput(attrs={'placeholder': 'Менеджер'}))
    short_description = forms.CharField(label='Короткое описание', widget=forms.Textarea(attrs={'placeholder': 'Короткое описание'}))
    full_description = forms.CharField(label='Полное описание', widget=forms.Textarea(attrs={'placeholder': 'Полное описание'}))
    deadline = forms.DateField(label='Дедлайн', widget=forms.DateInput(attrs={'placeholder': 'Дедлайн'}))
    payment = forms.IntegerField(label='Цена', widget=forms.NumberInput(attrs={'placeholder': 'Цена'}))
    status = forms.CharField(label='Статус', widget=forms.TextInput(attrs={'placeholder': 'Статус'}))
    documentation_link = forms.CharField(label='Ссылка на методички', widget=forms.Textarea(attrs={'placeholder': 'Ссылка на методички'}))
    project_link = forms.CharField(label='Ссылка на проект', widget=forms.Textarea(attrs={'placeholder': 'Ссылка на проект'}))

    class Meta:
        model = Task
        fields = ['user',
                 'identified',
                 'in_wait_status',
                 'manager',
                 'short_description',
                 'full_description',
                 'deadline',
                 'payment',
                 'status',
                 'documentation_link',
                 'project_link',
                 'payment_parts',
                 'part1',
                 'part2',
                 'part3',
                 'part4']