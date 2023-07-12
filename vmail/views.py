from re import template
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from flask import request
from .models import Post
from django.views.generic import ListView,DetailView,CreateView
from django.contrib.auth.models import User


def home(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request, 'vmail/home.html',context)

class PostListView(LoginRequiredMixin,ListView):
    model=Post
    template_name='vmail/home.html'
    context_object_name='posts'
    ordering=['-date_posted']
    

    

class UserPostListView(ListView):
    model = Post
    template_name = 'vmail/user_post.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


def sent(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request, 'vmail/sent.html',context)


class PostDetailView(LoginRequiredMixin,DetailView):
    model=Post
    
    
   
class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post 
    fields=['email','subject', 'content']
    
    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)

def about(request):#About=Inbox
    return render(request, 'vmail/about.html', {'title':'About'})

