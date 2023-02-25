from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import MusicForm
from .models import Music


# Create your views here.
def index(request):
    music = Music.objects.all()
    context = {
        'music_list': music
    }

    return render(request,"index.html",context)


def detail(request, music_id):
    music = Music.objects.get(id=music_id)

    return render(request, "detail.html", {'music': music})


def add_music(request):
    if request.method == "POST":
        name = request.POST.get('name', )
        desc = request.POST.get('desc', )
        movie_name = request.POST.get('movie_name', )
        img = request.FILES['img']
        music = Music(name=name, desc=desc, movie_name=movie_name, img=img)
        music.save()
        return redirect('/')
    return render(request, 'add.html')


def update(request, id):
    music = Music.objects.get(id=id)
    form = MusicForm(request.POST or None, request.FILES, instance=music)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'music': music})


def delete(request, id):
    if request.method == 'POST':
        music = Music.objects.get(id=id)
        music.delete()
        return redirect('/')
    return render(request, 'delete.html')
