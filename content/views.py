from django.shortcuts import render
from .models import Employee


def home_page(request):
    return render(request, 'home.html')


def team_page(request):
    employees = Employee.objects.all()
    return render(request, 'team.html', {'employees': employees})


def team_profile_pages(request, **kwargs):
    employee = Employee.objects.get(pk=kwargs['pk'])
    return render(request, 'team_profile.html', {'employee': employee})
