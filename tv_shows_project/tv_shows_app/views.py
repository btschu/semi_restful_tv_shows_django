from django.shortcuts import render, redirect
from .models import Show

def index(request):
    return redirect ('/shows')

def shows(request):
    context = {
        'shows' : Show.objects.all()
    }
    return render (request, 'shows.html', context)

def new_show(request):
    if request.method == 'GET':
        return render (request, 'new_show.html')
    if request.method == 'POST':
        Show.objects.create(
            title = request.POST['title'], 
            network = request.POST['network'], 
            release_date = request.POST['release_date'], 
            description = request.POST['description']
        )
        return redirect ('/shows')

def view_show(request, id):
    context = {
        'show' : Show.objects.get(id=id)
    }
    return render (request, 'view_show.html', context)

def edit_show(request, id):
    context = {
        'edit' : Show.objects.get(id=id)
    }
    if request.method == 'GET':
        return render (request, 'edit_show.html', context)
    if request.method == 'POST':
        edit = Show.objects.get(id=id)
        edit.title = request.POST['title']
        edit.network = request.POST['network']
        edit.release_date = request.POST['release_date']
        edit.description = request.POST['description']
        edit.save()
        return redirect ('/shows')

def delete_show(request, id):
    show = Show.objects.get(id=id)
    show.delete()
    return redirect ('/shows')