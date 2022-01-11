from django.urls import path
from news import views

urlpatterns = [
    path("", views.index, name="index"),
    path("art/", views.art, name="art"),
    # path("post/<int:pk>", views.PostDetailView.as_view(), name="post"),
    # path("post/create", views.PostCreate.as_view(), name="post_create"),
]