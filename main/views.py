from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def RenderHomePage(request):

    posts = Post.objects.all()


    context = {'posts':posts}
    return render(request, 'main/home.html', context)

def viewPost(request, uid):
    post = Post.objects.get(uid = uid)

    context = {'singlePost':post}
    return render(request, 'main/home.html', context)

# def Posts(request, uid):
#     posts = Post.objects.all()
#     print('Posts: ', posts, '\n')

