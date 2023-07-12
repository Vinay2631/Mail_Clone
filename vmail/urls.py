from django.urls import path
from .views import PostListView,PostDetailView,PostCreateView,UserPostListView
from . import views

urlpatterns = [
    path('', PostListView.as_view(),name="VMail-Home"),
    path('user/<str:username>', UserPostListView.as_view(),name="user-post"),
    path('sent', views.sent,name="sent"),
    path('post/<int:pk>/', PostDetailView.as_view(),name='post-detail'),
    path('post/new/', PostCreateView.as_view(),name='post-create'),
    path('about/', views.about,name="VMail-About"),
]
