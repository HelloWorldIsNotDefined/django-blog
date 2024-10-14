from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/<int:blog_id>/', views.detail, name='detail'),
    path('blog/list/', views.list, name='list'),
    path('blog/create/', views.create, name='create'),
    path('blog/update/<int:blog_id>/', views.update, name='update'),
    path('blog/delete/<int:blog_id>/', views.delete, name='delete'),
]
