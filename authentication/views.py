from django.shortcuts import render


def authentication_page(request):
    return render(request, 'account_login.html')


def employee_zone_page(request):
    return render(request, 'employee_zone.html')