from operator import index
from textwrap import indent
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('index1/', views.index1, name = "index1"),
    # path("travel1/", views.NCategory, name="NCategory"),
    # path("home/", views.NSummarization, name="NSummarization"),
    path("author/", views.author, name="author"),
    path("politics/", views.politics, name="politics"),
    path("post/", views.post, name="post"),
    path("business/", views.business, name="business"),
    path("sports/", views.sports, name="sports"),
    path("art/", views.art, name="art"),
    path("world/", views.world, name="world"),
    path("travel/", views.travel, name="travel"),
    path("news_post/", views.news_post, name="news_post"),
    path("banner1/", views.banner1, name="banner1"),
    path("banner2/", views.banner2, name="banner2"),
    path("banner3/", views.banner3, name="banner3"),
    path("banner4/", views.banner4, name="banner4"),
]