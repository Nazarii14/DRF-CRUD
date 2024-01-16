from . import views

from django.urls import path

urlpatterns = [
    path('homepage/', views.homepage, name='home-page'),
    path('', views.list_posts, name='list-posts'),
    path("<int:post_id>", views.post_detail, name='post-detail'),
    path("<int:post_id>/update", views.update_post, name='update-post'),
    path("<int:post_id>/delete", views.delete_post, name='delete-post'),
]
