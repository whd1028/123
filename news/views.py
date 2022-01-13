from django.shortcuts import render
from .models import *


# Create your views here.
def index(req):
    # post_latest = Post.objects.order_by("-createDate")[:6]
    context = {
        # "post_latest": post_latest
    }

    return render(req, "index.html", context=context)


def author(req):
    # post_latest = Post.objects.order_by("-createDate")[:6]
    context = {
        # "post_latest": post_latest
    }

    return render(req, "author.html", context=context)


def politics(req):
    # post_latest = Post.objects.order_by("-createDate")[:6]
    context = {
        # "post_latest": post_latest
    }

    return render(req, "politics.html", context=context)


def post(req):
    # post_latest = Post.objects.order_by("-createDate")[:6]
    context = {
        # "post_latest": post_latest
    }

    return render(req, "post.html", context=context)


def business(req):
    # post_latest = Post.objects.order_by("-createDate")[:6]
    context = {
        # "post_latest": post_latest
    }

    return render(req, "business.html", context=context)


def sports(req):
    # post_latest = Post.objects.order_by("-createDate")[:6]
    context = {
        # "post_latest": post_latest
    }

    return render(req, "sports.html", context=context)


def art(req):
    # post_latest = Post.objects.order_by("-createDate")[:6]
    context = {
        # "post_latest": post_latest
    }

    return render(req, "art.html", context=context)


def world(req):
    # post_latest = Post.objects.order_by("-createDate")[:6]
    context = {
        # "post_latest": post_latest
    }

    return render(req, "world.html", context=context)


def travel(req):
    # post_latest = Post.objects.order_by("-createDate")[:6]
    context = {
        # "post_latest": post_latest
    }

    return render(req, "travel.html", context=context)


def travel1(req):
    # post_latest = Post.objects.order_by("-createDate")[:6]
    context = {
        # "post_latest": post_latest
    }

    return render(req, "travel1.html", context=context)

def NCategory(req):

    n = 3
    get_title = News.objects.get(n_id=n)
    title = "계룡시, 시민과 함께한 2020년 해맞이행사 성료"
    raw = f"select nc_id, n_content from N_content inner join News on N_content.n_id = News.n_id  where n_title = '{get_title.n_title}'"
    NC = N_content.objects.raw(raw)
    nn = NC[0].n_content

    return render(req, "travel1.html", {"NCategory": nn})
<<<<<<< HEAD

def home(req):
    ns = N_summarization.objects.all()
    return render(req, 'home.html', {'ns': ns}) 
=======
>>>>>>> 52ff0fa5d60c4e4a8105eb5c84acf5822031daf0
