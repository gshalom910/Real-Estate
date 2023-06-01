from turtle import home, title
from django.shortcuts import redirect, render
from .forms import GalleryForm, HomeForm, Userform
from .models import Gallery, Home, PropertyType
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    properties=Home.objects.all().order_by('-created_at')[:3]
    # print(properties)
    # listproperty=[properties]
    # last_pro=listproperty[-3:]
    # last_pro3={'status':last_pro[0][0]['status'],'price':last_pro[0][0]['price'],'title':last_pro[0][0]['title'],'ptype':last_pro[0][0]['ptype_id'],'geo':last_pro[0][0]['geolocation'],'address':last_pro[0][0]['address'],'subarea':last_pro[0][0]['subarea']}
    # last_pro2=[last_pro[0][1]]
    # print(last_pro3)
        
        # last_pro1=last_pro[0][2][x]
        # print(last_pro2)
    return render(request,'main/index.html',{'properties':properties,'count':3})
@login_required(login_url='login')
def create_p(request):
    forms=HomeForm()
    form1=GalleryForm()
    properties=Home.objects.filter(created_by=request.user)
    if request.method == 'POST':
        forms=HomeForm(request.POST,request.FILES)
        if forms.is_valid():
            pp=forms.save(commit=False)
            pp.created_by=request.user
            pp.save()
            return redirect('index')  
        # return redirect('index')
    return render(request,'main/create_property.html',{'forms':forms,'pro':properties})
@login_required(login_url='login')
def property(request):
    properties=Home.objects.all()
    propertytype=PropertyType.objects.all()
    context={'properties':properties,'pptype':propertytype,'statuss':['Rent','Sell']}
    if request.method == 'POST':
        status_nw=request.POST['status']
        type_nw=request.POST['type']
        price_nw=request.POST['price']
        address_nw=request.POST['address']
        sort=request.POST['s']
        properties=Home.objects.filter(Q(status=status_nw) | Q(ptype=type_nw) | Q(price=price_nw) | Q(address=address_nw) ).order_by(sort)
        context={'properties':properties}
        return render(request,'main/property.html',context)
    return render(request,'main/property.html',context)

def about(request):
    return render(request,'main/about_us.html')


def contact(request):
    return render(request,'main/contact_us.html')
@login_required(login_url='login')
def detail(request,pk):
    property=Home.objects.get(id=pk)
    properties=Home.objects.filter(created_by__id=property.created_by.id)
    return render(request,'main/detail.html',{'property':property,'properties':properties})
@login_required(login_url='login')
def chat(request):
    return render(request,'main/chat.html')


def registration(request):
    # form=UserCreationForm()
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form=Userform()
        if request.method == 'POST':
            # form=UserCreationForm(request.POST).0
            form=Userform(request.POST)
            if form.is_valid():
                form.save()
                return redirect('index')
        return render(request,'main/register.html',{'form' : form})

def loginuser(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            usname=request.POST['username']
            passowrd=request.POST['pass']
            user=authenticate(request,username=usname,password=passowrd)
            if user is not None:
                login(request,user)
                return redirect('index')
        return render(request,'main/login.html')

def logout_user(request):
    logout(request)
    return redirect('login')

def gallery(request):
    if request.method == 'POST':
        img=request.FILES.getlist('images')
        gal=request.POST['gal']
        pro=Home.objects.get(id=gal)
        for i in img:
            g=Gallery.objects.create(prop=pro,images=i)
            g.save()
    return redirect('index') 