from django.shortcuts import render, redirect

# Create your views here.
from .models import Post, Comment
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView
from .forms import PostForm, CommentForm, UserRegisterForm
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


def index(request):
    return render(request, 'index.html')


@login_required()
# @permission_required('service.view_post')
def about(request):
    return render(request, 'about.html')


class RegisterForm(CreateView):
    template_name = 'register.html'
    # form_class = UserCreationForm
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')


class PostsView(ListView):
    login_url = 'login'
    model = Post
    template_name = 'index.html'
    ordering = ['-created_at']


class DetailPostView(DetailView):
    model = Post
    template_name = 'post_detail.html'


# class CreatePostView(LoginRequiredMixin, CreateView):
class CreatePostView(PermissionRequiredMixin, CreateView):
    permission_required = 'service.add.post'
    model = Post
    template_name = 'post_create.html'
    form_class = PostForm


# class UpdatePostView(LoginRequiredMixin, UpdateView):
class UpdatePostView(PermissionRequiredMixin, UpdateView):
    permission_required = 'service.change.post'
    model = Post
    # template_name = 'post_update.html'
    template_name = 'post_create.html'
    form_class = PostForm


# class DeletePostView(LoginRequiredMixin, DeleteView):
class DeletePostView(PermissionRequiredMixin, DeleteView):
    permission_required = 'service.delete.post'
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('index')


class AddCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'comment_add.html'
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
