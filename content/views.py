from django.shortcuts import render
from content.models import Employee

def home_page(request):
    return render(request, 'home.html')
    
def our_team_page(request):
    employees = Employee.objects.all()
    return render(request, 'our_team.html', {'employees': employees})

def employee_zone_page(request):
    return render(request, 'employee_zone.html')