----passo a passo para criação do projeto-----

1. Configurar dependências:

---cmd---

python -m venv venv

venv\scripts\activate

pip install django
*OU (se ja tiver o requirements)* pip install -r requirements.txt 

pip freeze > requirements.txt

-----------

criar o arquivo .gitignore na raiz do projeto e colocar o seguinte texto:

venv/

2. Iniciar o Django

---cmd---

django-admin startproject config .

python manage.py startapp app

-------

em settings, adicionar o 'app' nos INSTALLED_APPS

dentro de app/ , crie o arquivo 'urls.py' e coloque o código a seguir(configurando ENDPOINTS):

------app/urls.py---------

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
]

------------------


agora, no config/urls:

------config/urls.py---------


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
]

-----------------


por fim, na views:

-------app/views.py ------------

from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
	return HttpResponse("<h1>Olá, Mundo!</h1>")

---------------------


















