from django.contrib import admin

# Register your models here.
from .models import Post, Comment, Message

# @admin.register(Post)
# class HomeAdmin(admin.ModelAdmin):
#     list_display = [
#         'title',
#         'description',
#         'image',
#         'created_at',
#         'updated_at',
#     ]

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Message)
