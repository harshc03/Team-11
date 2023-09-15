from django.urls import path
from . import views
urlpatterns = [
    # path("",views.blog_list, name='blog_list'),
    # path("posts",views.posts,name="posts-page"),
    # path("posts/<slug:slug>",views.post_detail,name="post-detail-page"), #posts/my-first-post
    path('blogs/', views.blog_list, name='blog_list'),
]
