from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)
from . import views

urlpatterns = [
    path('',views.home,name='todo-home'),
    path('post/', PostListView.as_view(), name='todo-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='todo-detail'),
    path('post/new/', PostCreateView.as_view(), name='todo-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='todo-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='todo-delete'),
    path('authors/', views.authors, name='todo-about'),
    ]
