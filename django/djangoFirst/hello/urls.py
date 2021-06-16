from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('coder/',views.coder, name='greeting'),
    path('<str:name>',views.greet, name='greet'),
    path('<str:name>/',views.greet, name='greet'),
]