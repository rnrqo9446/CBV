from django.urls import path
from .views import home, create_post, edit_post, delete_post, detail_post

urlpatterns = [
    path('home/',home,name='home'),
    path('create_post/',create_post,name='create_post'),
    path('edit_post/<int:post_pk>',edit_post,name='edit_post'),
    path('delete_post/<int:post_pk>',delete_post,name='delete_post'),
    path('detail_post/<int:post_pk>',detail_post,name='detail_post'),
]