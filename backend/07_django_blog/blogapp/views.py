from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .form import PostForm, UserRegisterForm
from django.contrib import messages

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            posts = Post.objects.all().order_by('created_at')
        else:
            posts = Post.objects.filter(author = request.user).order_by('created_at')
    else :
        posts = Post.objects.all().order_by('created_at')
        
    return render(request, "blogapp/home.html", {'posts':posts})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'blogapp/create_post.html', {'form' : form})

def signup(request):
    pass

def post_details(request):
    pass