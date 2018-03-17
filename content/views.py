from django.shortcuts import render

def home_page(request):
    return render(request, 'home.html')
    
def our_team_page(request):
    return render(request, 'our_team.html')

def employee_zone_page(request):
    return render(request, 'employee_zone.html')