from django.shortcuts import render, redirect
from .models import Player, Team, Tournament

def home(request):
    db_players = Player.objects.all()

    context = {
        'db_players': db_players
    }
    return render(request, 'home.html', context)   

def about(request):
    db_players = Player.objects.all()

    context = {
        'db_players': db_players
    }
    
    return render(request, 'about.html', context)

def createPlayer(request):
    if request.method == "POST":
        PlayerName = request.POST['name']
        PlayerRank = request.POST['rank']
        PlayerCost = request.POST['cost']
        PlayerAbout = request.POST['about']
        Player.objects.create(name=PlayerName, rank=PlayerRank, cost=PlayerCost, about=PlayerAbout)
        
    return redirect('/about')

def createPlayer(request):
    if request.method == "POST":
        TournamentName = request.POST['name']
        TournamentBudget = request.POST['budget']
        Tournament.objects.create(name=TournamentName, budget=TournamentBudget)
        
    return redirect('/about')

def deleteButton(request):
    if request.method == "POST":
        player_name = request.POST.get('name')
        try:
            delButtonPlayer = Player.objects.get(name=player_name)
            delButtonPlayer.delete()
        except Player.DoesNotExist:
            pass  # Handle the case where player does not exist

    return redirect('/about')
