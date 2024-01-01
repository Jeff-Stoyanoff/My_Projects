from django.urls import path
from . import views

urlpatterns = [
    path('', views.start),
    path('playerForm', views.playerForm),
    path('register', views.register),
    path('login', views.login),
    path('gamePage', views.gamePage),
    path('createQuestion', views.createQuestion),
    path('questionPage', views.questionPage),
    path('question_list', views.question_list, name='question_list'),
]