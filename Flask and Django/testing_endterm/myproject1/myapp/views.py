from django.shortcuts import render
from .forms import contactform

# Create your views here.
def test(request):
    return render(request, 'test.html')


def home(request):
    data= {
        'test1':'test'
    }
    return render(request,'home.html',data)

def contact(request):
    form = contactform()
    return render(request , 'form.html', {'form':form})


