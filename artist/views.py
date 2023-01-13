from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404 , redirect

from .forms import *
from .models import *

menu = [
    {'title':"О нас", 'url_name':'about'},
    {'title':"Додати статтю", 'url_name':'add_page'}
]

def index(request):
    posts = artist.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Головна сторінка'
    }
    return render(request, 'artist/index.html',context=context)

def about(request):
    return render(request, 'artist/about.html',{'menu' : menu,'title':'О нас'})

def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            try:
                artist.objects.create(**form.cleaned_data)
                return redirect('home')
            except:
                form.add_error(None,'Помилка додавання статті ')
    else:
        form = AddPostForm()
    return render(request,'artist/addpage.html',{'form':form,'menu' : menu,'title':'Додавання статті'})

def show_post(request,post_slug):
    post = get_object_or_404(artist, slug=post_slug)

    context = {
        'post':post,
        'menu':menu,
        'title':post.title
    }

    return render(request, 'artist/post.html', context=context)