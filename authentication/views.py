from django.shortcuts import render

def authentication_page(request):
    return render(request, 'account_login.html')
