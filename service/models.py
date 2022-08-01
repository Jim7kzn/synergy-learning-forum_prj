from django.db import models
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    objects = models.Manager

    title = models.CharField(verbose_name='название', max_length=100)
    description = models.TextField(verbose_name='описание', null=True, blank=True)
    image = models.ImageField(verbose_name='картинка', null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='дата изменения', auto_now=True)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('index')


class Comment(models.Model):
    objects = models.Manager

    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    description = models.TextField(verbose_name='описание', null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='дата создания', auto_now_add=True)

    def __str__(self):
        return f'{self.description}'

    def get_absolute_url(self):
        return reverse('index')


class Message(models.Model):
    objects = models.Manager

    subject = models.CharField(verbose_name='тема сообщения', max_length=255, null=True, blank=True)
    body = models.TextField(verbose_name='текст сообщения')
    created_at = models.DateTimeField(verbose_name='дата создания', auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

    # def get_absolute_url(self):
    #     return reverse('index')
