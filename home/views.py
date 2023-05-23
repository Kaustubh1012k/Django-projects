from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from datetime import datetime
from home.models import Contact,SignUp

def index(request):
    return render(request,'index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout_user(request):
    auth.logout(request)
    return redirect('home')

def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already taken')
                return redirect(signup)
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email is already taken')
                return redirect(signup)
            else:
                user = User.objects.create_user(username=username, password=password, 
                                        email=email, first_name=first_name, last_name=last_name)
                user.save()
                return redirect('login.html')
        else:
            messages.info(request, 'Both passwords are not matching')
            return redirect(signup)
    else:
        return render(request, 'signup.html')
    
    
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
