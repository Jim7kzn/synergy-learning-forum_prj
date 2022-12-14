import csv
import io
import datetime

from django.shortcuts import render, redirect
from django.conf import settings

# Create your views here.
from .models import Post, Comment
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView
from .forms import PostForm, CommentForm, UserRegisterForm, MessageForm
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


@login_required()
# @permission_required('service.view_post')
def about(request):
    form = MessageForm()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data.get('subject')
            body = form.cleaned_data.get('body')
            try:
                send_mail(subject, body, settings.EMAIL_HOST_USER, ['it@rfprt.ru'], fail_silently=False)
                form.save()
            except Exception as err:
                print(str(err))
            return redirect('about')
    return render(request, 'about.html', {'form': form})


class RegisterForm(SuccessMessageMixin, CreateView):
    template_name = 'register.html'
    # form_class = UserCreationForm
    success_message = "%(username)s был зарегистрирован."
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


# # class CreatePostView(LoginRequiredMixin, CreateView):
# class CreatePostView(PermissionRequiredMixin, CreateView):
#     permission_required = 'service.add.post'
#     model = Post
#     template_name = 'post_create.html'
#     form_class = PostForm

@login_required()
@permission_required('service.add.post')
def create_post(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            title = form.cleaned_data.get('title')
            # id = form.cleaned_data.get('pk')
            messages.success(request, f'Post {title} был успешно создан.')
            return redirect('index')
    return render(request, 'post_create.html', {'form': form})


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


def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['upl_file']
        file = FileSystemStorage()
        file_link = file.save(uploaded_file.name, uploaded_file)
        context['url'] = file.url(file_link)
    return render(request, 'upload.html', context)


def download(request):
    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    writer.writerow(['Title', 'Description', 'Created_At'])
    for row in Post.objects.all().values_list('title', 'description', 'created_at'):
        writer.writerow(row)
    filename = f'log_posts_{datetime.datetime.now()}'
    response['Content-Disposition'] = f'attachment; filename = "{filename}.csv"'
    return response
