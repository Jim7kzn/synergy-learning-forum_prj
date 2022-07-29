from django.urls import path
from service import views

urlpatterns = [
    path('', views.PostsView.as_view(), name='index'),
    path('post/<int:pk>', views.DetailPostView.as_view(), name='post_detail'),
    path('create_post', views.CreatePostView.as_view(), name='post_create'),
    path('post_update/<int:pk>', views.UpdatePostView.as_view(), name='post_update'),
    path('post_delete/<int:pk>', views.DeletePostView.as_view(), name='post_delete'),
    path('post/<int:pk>/add_comment', views.AddCommentView.as_view(), name='comment_add'),
    path('about', views.about, name='about'),
]

