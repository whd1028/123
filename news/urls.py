from xml.etree.ElementInclude import include
from django.urls import path, include
from . import views
#from rest_framework import routers

# router = routers.DefaultRouter(trailing_slash=False)
#router.register('plan', views.TodoView)

urlpatterns = [
    #path('', include(router.urls)),
    path("", views.index, name="index"),
    path("author/", views.author, name="author"),
    path("politics/", views.politics, name="politics"),
    path("post/", views.post, name="post"),
    path("business/", views.business, name="business"),
    path("sports/", views.sports, name="sports"),
    path("art/", views.art, name="art"),
    path("world/", views.world, name="world"),
    path("travel/", views.travel, name="travel"),
    path("travel1/", views.NCategory, name="NCategory"),
    path("home/", views.NSummarization, name="NSummarization"),
    path("banner3/", views.banner3, name="banner3"),
    # path("TodoView", views.TodoView, name="TodoView"),
    # path("NewsView", views.views.NewsView, name="NewsView"),
]
