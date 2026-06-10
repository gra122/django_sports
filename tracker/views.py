from django.shortcuts import render
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def teams(request):
    teams = [
        "Team A",
        "Team B",
        "Team C",
    ]
    return render(request, 'teams.html', {'teams': teams})

def matches(request):
    matches = [
        "Team A vs Team B",
        "Team B vs Team C",
    ]
    return render(request, 'matches.html', {'matches': matches})
