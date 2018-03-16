from django.shortcuts import render

def home_page(request):
    return render(request, 'home.html')
    
def our_team_page(request):
    return render(request, 'our_team.html')