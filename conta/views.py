from django.shortcuts import render

def conta(request):
    return render(request, 'home/home.html')
