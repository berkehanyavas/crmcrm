from django.shortcuts import render, redirect
from django.contrib import messages
# from .forms import TaskForm
from .models import Task, Team, Checklist, Comment


# Create your views here.

def indexerp(request):
    if not request.user.is_authenticated:
        messages.warning(request,'Giris yapmadan bu sayfayi goremezsiniz.')
        return redirect('index')
    gorevler = Task.objects.filter(atanan=request.user)
    team = Team.objects.filter(team_leader_id=request.user.id)
    print(team)
    context = {
        'sayfaadi': 'ERP Anasayfa',
        'gorevler': gorevler,
        'team': team
    }

    return render(request,'indexerp.html',context)

def taskPage(request,id):
    if not request.user.is_authenticated:
        messages.warning(request,'Giris yapmadan bu sayfayi goremezsiniz.')
        return redirect('index')
    gorev = Task.objects.get(id=id)
    context = {
        'sayfaadi': 'Gorev Sayfasi',
        'gorev': gorev,
    }
    return render(request,'taskpage.html',context)

def teamView(request):
    team = Team.objects.values_list('team_leader_id')
    context = {
        'sayfaadi': 'Takimlar',
        'takimlar': team
    }
    return render(request,'teampage.html',context)