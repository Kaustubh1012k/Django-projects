from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

def index(request):
    return render(request,'index.html')



def List(request):
    return render(request,'List.html')

def Historical(request):
    return render(request,'Historical.html')

def Shinde(request):
    return render(request,'Shinde Chhatri.html')

def RajaDinkar(request):
    return render(request,'Raja Dinkar Kelkar Museum.html')

def Parvati(request):
    return render(request,'Parvati.html')

def LalMahal(request):
    return render(request,'Lal_Mahal.html')

def Pataleshwar(request):
    return render(request,'Pataleshwar.html')




def List2(request):
    return render(request,'List2.html')

def Ravi(request):
    return render(request,'ravivarp.html')

def MG(request):
    return render(request,'mgroad.html')

def Tulshibaug(request):
    return render(request,'tulshibaug.html')

def ABC(request):
    return render(request,'abc.html')




def List3(request):
    return render(request,'List3.html')

def wetnjoy(request):
    return render(request,'wetnjoy.html')

def amanora(request):
    return render(request,'amanora.html')

def katraj(request):
    return render(request,'katrajzoo.html')

def tramp(request):
    return render(request,'tramp.html')




def List4(request):
    return render(request,'List4.html')

def food(request):
    return render(request,'food.html')

def Durvankur(request):
    return render(request,'Durvankur.html')

def Bipin(request):
    return render(request,'Bipin.html')

def Sainath(request):
    return render(request,'Sainath_khanawal.html')

def Badshahi(request):
    return render(request,'Badshahi.html')

def Sukanta(request):
    return render(request,'Sukanta.html')

def SP(request):
    return render(request,'SP Biryani.html')




def List5(request):
    return render(request,'List5.html')

def Dagdusheth(request):
    return render(request,'Dagdusheth.html')

def Mahalaxmi(request):
    return render(request,'Mahalaxmi.html')

def Chintamani(request):
    return render(request,'Chintamani.html')

def Sainath(request):
    return render(request,'Sainath_khanawal.html')

def Omkareshwar(request):
    return render(request,'Omkareshwar.html')

def Balaji(request):
    return render(request,'Prati_Balaji.html')

def Ram(request):
    return render(request,'Ram_Mandir.html')



def contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        place=request.POST.get('place')
        address=request.POST.get('address')
        enquiry=request.POST.get('enquiry')
        contact=Contact(name=name, email=email, place=place,address=address,enquiry=enquiry, date=datetime.today())
        contact.save()
    return render(request,'contact.html')

def Shopping (request):
     return render(request,'Shopping.html')

def about(request):
    return render(request,'about.html')
