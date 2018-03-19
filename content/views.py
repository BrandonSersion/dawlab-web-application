from django.shortcuts import render
from content.models import Employee

def home_page(request):
    return render(request, 'home.html')
    
def team_page(request):
    employees = Employee.objects.all()
    return render(request, 'team.html', {'employees': employees})

def employee_login_page(request):
    return render(request, 'employee_login.html')