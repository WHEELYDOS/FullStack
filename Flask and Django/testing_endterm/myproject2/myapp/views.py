from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import product
from .forms import contact
from django.contrib.auth import login , logout, authenticate
from django.contrib.auth.decorators import login_required

def testing(request):
    return HttpResponse("this app of yours is running dhashu mwah <3 ")

def home(request):
    return render(request,'home.html')    
# Create your views here.

def products_view(request):
    products = product.objects.all()
    data = {'products':products}
    return render(request,'products.html',data)

def form(request):
    forms = contact()
    data = {'forms':forms}
    return render(request,'form.html',data)

@login_required
def dashboard(request):
    return render(request , 'dashboard.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {
                'error': 'Invalid Username or Password'
            })
    return render(request, 'login.html')
        

def logout_user(request):
    logout(request)
    return render(request,'login.html')