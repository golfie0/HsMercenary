from django.urls import path
from . import views

urlpatterns = [
    path('', views.RenderHomePage),
    # path('posts',views.),
    # path('posts/<str:uid>', views.),
]
