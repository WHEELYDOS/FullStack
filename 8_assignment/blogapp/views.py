from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import Post
from .forms import PostForm, UserregistrationForm
from django.contrib import messages


def home(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            posts = Post.objects.all().order_by('-created_at')
        else:
            posts = Post.objects.filter(author=request.user)
    else:
        posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blogapp/home.html', {'posts': posts})


def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = UserregistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Welcome, {user.username}! Your account has been created.')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserregistrationForm()
    return render(request, 'blogapp/signup.html', {'form': form})


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Your post has been published!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = PostForm()
    return render(request, 'blogapp/create_post.html', {'form': form})


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blogapp/post_detail.html', {'post': post})
