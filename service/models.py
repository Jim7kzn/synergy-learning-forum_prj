from django.db import models

# Create your models here.


class Post(models.Model):
    objects = models.Manager

    title = models.CharField(verbose_name='название', max_length=100)
    description = models.TextField(verbose_name='описание', null=True, blank=True)
    image = models.ImageField(verbose_name='картинка')
    created_at = models.DateTimeField(verbose_name='дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='дата изменения', auto_now=True)

    def __str__(self):
        return f'{self.title}'


class Comment(models.Model):
    objects = models.Manager

    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    description = models.TextField(verbose_name='описание', null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='дата создания', auto_now_add=True)

    def __str__(self):
        return f'{self.description}'
