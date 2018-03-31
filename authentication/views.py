from django.shortcuts import render

from authentication.forms import MyLoginForm

def authentication_page(request):
    return render(request, 'account_login.html')

def employee_zone_page(request):
    #Tried to override the default allauth form. Didn't work.
    context = {
        'login_form':MyLoginForm()
    }
    return render(request, 'employee_zone.html', context)