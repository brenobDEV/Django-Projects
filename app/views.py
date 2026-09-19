from django.shortcuts import render


def home_view(request):
    return render(request,'home.html')

def produtos_view(request):
    context = {'nome': "Monitor", "preco": 700.00, "estoque": 3}
    
    return render(request,'produtos.html', context)