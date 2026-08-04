from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import products
from .forms import contactform
from django.contrib.auth import login ,logout,authenticate
from django.contrib.auth.decorators import login_required

def testing(request):
    return HttpResponse("this is running shashuily")

def home(request):
    return render(request,'home.html')

def product(request):
    product = products.objects.all()
    data = {'products':product}
    return render(request, 'product.html',data)
    #render(request, *args , **kwargs)
# Create your views here.

@login_required
def dashboard(request):
    return render(request,'dashboard.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password= request.POST['password'] 
        user = authenticate(request,username=username,password=password)

        if user is not None:
             login(request,user)
             return redirect('dashboard')
        else :
            return render(request,'login.html')
        
    return render(request,'login.html')

def logout(request):
    logout(request)
    return render(request,'login.html')

def form(request):
    form = contactform()
    return render(request,'forms.html',{'form':form})