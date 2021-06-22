from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def login(request):
    return render(request, 'login.html')


@login_required
def home(request):
    return render(request, 'home.html')


@login_required
def add_memory(request):
    return render(request, 'add_memory.html')


@login_required
def delete_memory(request):
    return render(request, 'delete_memory.html')
