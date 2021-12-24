from django.urls import path
from . import views

urlpatterns = [
    path('', views.RenderHomePage),
    # path('login', views.Login),
    # path('register', views.Register),
    path('posts/<str:uid>', views.viewPost),
    # path('posts/create'),
    # path('profile'),
    # path('profile/collection'),

] 