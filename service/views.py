from django.shortcuts import render, redirect

# Create your views here.
from .models import Post, Comment
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView
from .forms import PostForm, CommentForm, RegisterForm
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


class RegisterForm(CreateView):
    template_name = 'register.html'
    # form_class = UserCreationForm
    form_class = RegisterForm
    success_url = reverse_lazy('login')


class PostsView(ListView):
    model = Post
    template_name = 'index.html'
    ordering = ['-created_at']


class DetailPostView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class CreatePostView(CreateView):
    model = Post
    template_name = 'post_create.html'
    form_class = PostForm


class UpdatePostView(UpdateView):
    model = Post
    # template_name = 'post_update.html'
    template_name = 'post_create.html'
    form_class = PostForm


class DeletePostView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('index')


class AddCommentView(CreateView):
    model = Comment
    template_name = 'comment_add.html'
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
