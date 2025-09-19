from django.urls import path
from . import views

urlpatterns = [
    # READ
    path("", views.post_list, name="post-list"),
    path("<slug:slug>/", views.post_detail, name="post-detail"),

    # CREATE
    path("post/new/", views.post_create, name="post-create"),

    # UPDATE
    path("<slug:slug>/update/", views.post_update, name="post-update"),

    # DELETE
    path("<slug:slug>/delete/", views.post_delete, name="post-delete"),
    
    # CATEGORY
    path("category/<slug:category_slug>/", views.posts_by_category, name="posts-by-category"),

    # LIKE
    path('<slug:slug>/like/', views.like_post, name='like-post'),

    # SEARCH
    path('search/', views.search, name='search'),
]
