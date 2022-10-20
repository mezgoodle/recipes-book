from django.shortcuts import render

from .models import TelegramUser

def index(request):
    users = TelegramUser.objects.all().order_by('-id')
    return render(request, 'dashboard/index.html', {'users': users})


def recipes(request):
    return render(request, 'dashboard/recipes.html')
