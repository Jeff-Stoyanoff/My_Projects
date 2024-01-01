from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin', admin.site.urls),
    path('', views.home, name='site-home'),
    path('about', views.about, name='site-about'),
    path('createPlayer', views.createPlayer, name='site-createPlayer'),
    path('createTournament', views.createPlayer, name='site-createTournament'),
    path('deleteButton', views.deleteButton, name='site-deleteButton')
]
