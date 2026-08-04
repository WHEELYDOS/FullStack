from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm 

# Create your views here.
def test(request):
    return HttpResponse("django hello first project")
    #return render()

def home(request):
    return render(request,'home.html')

def data(request):
    data = {
        'parleg':'10',
        'khattametha':'100'
    }
    return render(request,'data.html',data)

def formss(request):
    form = ContactForm()
    return render(request,'contact.html',{'form':form})