from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from datetime import datetime
from home.models import SignUp

def index(request):
    return render(request,'index.html')

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('index.html')
        else:
            messages.error(request, 'Invalid Username or Password')
            return redirect('login')
    else:
        return render(request, 'login.html')


def Logout_user(request):
    logout(request)
    messages.success(request,"Logged Out Successfully")
    return redirect('home')

def signup(request):
    if request.method == "POST":
        username=request.POST.get('username')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        myuser=User.objects.create_user(username,email,password)
        myuser.first_name=first_name
        myuser.last_name=last_name
        myuser.save()
        messages.success(request,"Your account has been successsfully created.")
        #signup=SignUp(username=username,first_name=first_name,last_name=last_name, email=email,date=datetime.today())
        #signup.save()
        return redirect('login')
    return render(request,'signup.html')

    
def contact(request):
    return render(request,'contact.html')    


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

def List6 (request):
     return render(request,'List6.html')
 
def COEP(request):
     return render(request,'coep.html') 

def PICT(request):
     return render(request,'pict.html')

def AISSMS(request):
     return render(request,'aissms.html')

def PVG(request):
     return render(request,'pvg.html')
 
def Sinhgad(request):
     return render(request,'sinhagad.html') 
 

  
def about(request):
    return render(request,'about.html')
