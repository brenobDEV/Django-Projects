from django.shortcuts import render


def home_view(request):
    return render(request,'home.html')

def produtos_view(request):
    return render(request,'produtos.html')
