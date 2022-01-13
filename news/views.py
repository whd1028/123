from django.shortcuts import render

from .models import *
from .models import NSummarization


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

# class PostDetailView(generic.DetailView):
#     model = Post


# class PostCreate(LoginRequiredMixin, CreateView):
#     model = Post
#     fields = ["title", "title_image", "content", "category"]

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

def home(req):
    ns = NSummarization.objects.all()
    return render(req, "home.html", {'ns': ns})

def NCategory(req):
    NC = NCategory.objects.all()
    a = NC[0]
    an = a.c_name
    # c_id = models.AutoField(primary_key=True)
    # c_name = models.CharField(unique=True, max_length=5)
    return render(req, "travel1.html", {"NCategory": an})

# def NSummarization(req):
#     ns = NSummarization.objects.all()
#     b = ns[0]
#     bn = b.ns_content
    
#     return render(req, "home.html", {"NSummarization: bn"})
#     ns_id = models.AutoField(primary_key=True)
#     n = models.OneToOneField('News', models.DO_NOTHING, blank=True, null=True)
#     ns_content = models.TextField(blank=True, null=True)
