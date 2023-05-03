from django.shortcuts import render, HttpResponse

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



def food(request):
    return render(request,'food.html')

def contact(request):
    return render(request,'contact.html')



def Entertainment(request):
    return render(request,'Entertainment.html')

def Shopping (request):
     return render(request,'Shopping.html')

def about(request):
    return render(request,'about.html')
