"""
URL configuration for web_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from home import views
from django.contrib.auth import views as auth_views

urlpatterns = [
     path('', views.index, name='home'),
    path('index.html', views.index, name='index'),
    path('login.html', views.Login, name='login'),

    path('signup.html', views.signup, name='signup'),
    path('contact.html', views.contact, name='contact'),
    
    path('List.html', views.List,name='List'),
    path('Historical.html', views.Historical,name='Historical'),
    path('Shinde Chhatri.html', views.Shinde,name='Shinde Chhatri'),
    path('Raja Dinkar Kelkar Museum.html', views.RajaDinkar,name='Raja Dinkar'),
    path('Parvati.html', views.Parvati,name='Parvati'),
    path('Lal_Mahal.html', views.LalMahal,name='LalMahal'),
    path('Pataleshwar.html', views.Pataleshwar,name='Pataleshwar'),
    
    path('List2.html', views.List2,name='List2'),
    path('ravivarp.html', views.Ravi,name='Ravi'),
    path('mgroad.html', views.MG,name='MG'),
    path('tulshibaug.html', views.Tulshibaug,name='Tulshibaug'),
    path('abc.html', views.ABC,name='ABC'),
    
    path('List3.html', views.List3,name='List3'),
    path('wetnjoy.html', views.wetnjoy,name='wetnjoy'),
    path('amanora.html', views.amanora,name='amanora'),
    path('katrajzoo.html', views.katraj,name='katraj'),
    path('tramp.html', views.tramp,name='tramp'),
    
    path('List4.html', views.List4,name='List4'),
    path('food.html', views.food,name='food'),
    path('Durvankur.html', views.Durvankur,name='Durvankur'),
    path('Bipin.html', views.Bipin,name='Bipin'),
    path('Sainath_khanawal.html', views.Sainath,name='Sainath'),
    path('Sukanta.html', views.Sukanta,name='Sukanta'),
    path('SP Biryani.html', views.SP,name='SP'),
    
    path('List5.html', views.List5,name='List5'),
    path('Dagdusheth.html', views.Dagdusheth,name='Dagdusheth'),
    path('Mahalaxmi.html', views.Mahalaxmi,name='Mahalaxmi'), 
    path('Chintamani.html', views.Chintamani,name='Chintamani'),
    path('Omkareshwar.html', views.Omkareshwar,name='Omkareshwar'),
    path('Prati_Balaji.html', views.Balaji,name='Balaji'),
    path('Ram_Mandir.html', views.Ram,name='Ram'),
    
    path('List6.html', views.List6,name='List6'),
    path('coep.html', views.COEP,name='COEP'),
    path('pict.html', views.PICT,name='PICT'),
    path('aissms.html', views.AISSMS,name='AISSMS'),
    path('pvg.html', views.PVG,name='PVG'),
    path('sinhgad.html', views.Sinhgad,name='Sinhgad'),
    
    path('about', views.about,name='about'),
      
]
