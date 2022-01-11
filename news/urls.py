from django.urls import path
from news import views

urlpatterns = [
    path("", views.index, name="index"),
    path("author/", views.author, name="author"),
    path("politics/", views.politics, name="politics"),
    path("post/", views.post, name="post"),
    path("business/", views.business, name="business"),
    path("sports/", views.sports, name="sports"),
    path("art/", views.art, name="art"),
    path("world/", views.world, name="world"),
    # path("post/<int:pk>", views.PostDetailView.as_view(), name="post"),
    # path("post/create", views.PostCreate.as_view(), name="post_create"),
]