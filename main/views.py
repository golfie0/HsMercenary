from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def RenderHomePage(request):
    return HttpResponse('<h1>dog</h1>')

def viewPost(request, uid):
    return HttpResponse('post uid:', str(uid))

# def Posts(request, uid):
#     posts = Post.objects.all()
#     print('Posts: ', posts, '\n')

