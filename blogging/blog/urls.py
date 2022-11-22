from django.contrib import admin
from django.urls import path, include
from .views import *
from .import views
from members.views import SignUpPage
urlpatterns = [
    path('', SignUpPage.as_view(), name='register' ),
    path('',HomePage.as_view(),name='home'),
    path('addPost',AddPost.as_view(),name='add_post'),
    path('addCategory',AddCategory.as_view(),name='add_category'),
    path('detail/<int:pk>',PostDetails.as_view(),name='post_detail'),
    path('detail/update/<int:pk>', UpdateDetails.as_view(), name='update_blog'),
    path('category/<str:cats>/', CategoryPosts, name='category_posts'),
    path('detail/update/delete/<int:pk>', DeleteBlog.as_view(), name='delete_blog'),
    path('like/<int:pk>', LikeView, name='like_post'),

]
