from . import views

from django.urls import path

urlpatterns = [
    path('homepage/', views.homepage, name='home-page'),
    path('', views.PostListCreateView.as_view(), name='list_posts'),
    path("<int:pk>", views.PostRetrieveUpdateDeleteView.as_view(), name="post-detail"),
    path("current_user/", views.get_posts_for_current_user, name="current_user"),
    path("posts_for/", views.ListPostsForAuthor.as_view(), name="posts_for_current_user"),
]
