import re
from django.shortcuts import render
from .models import *
from django.contrib import messages
from django.db.models import Q
#from django.views.generic import View

# -2022.01.24 park_jong_won
import logging
logger = logging.getLogger('news')


# Create your views here.
def index(req):
    raw = f"select ns_id, ns_content from N_summarization where ns_id = 3"
    NC = N_summarization.objects.raw(raw)
    # ns = NC[0].ns_content

    if req.method == 'POST':
        # form = TestForm(req.POST)
        form = req.POST
        
        logger.info(f"index POST log test => [scroll = {form['scroll']}, deltaTime = {form['deltaTime']}]")
        # logger.info(f"index POST log test")
    else:
        logger.info("index GET log test")

    # return render(req, "index.html", {'banner': ns})
    return render(req, "index.html")

def index1(req):
    context = {
        # "post_latest": post_latest
    }

    return render(req, "index1.html", context=context)


# def i_sum(req):
#     raw = f"select ns_id, ns_content from N_summarization where ns_id = 9"
#     NC = N_summarization.objects.raw(raw)
#     ns = NC[0].ns_content

#     return render(req, "index.html", {'i_sum': ns})

# def i_sum2(req):
#     raw = f"select ns_id, ns_content from N_summarization where ns_id = 5"
#     NC = N_summarization.objects.raw(raw)
#     ns = NC[0].ns_content

#     return render(req, "index.html", {'i_sum2': ns})

# def i_sum3(req):
#     raw = f"select ns_id, ns_content from N_summarization where ns_id = 7"
#     NC = N_summarization.objects.raw(raw)
#     ns = NC[0].ns_content

#     return render(req, "index.html", {'i_sum3': ns})        

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


def news_post(req):
    # post_latest = Post.objects.order_by("-createDate")[:6]
    context = {
        # "post_latest": post_latest
    }

    return render(req, "news_post.html", context=context)


def banner1(req):
    raw = f"select nc_id, n_content from N_content where nc_id = 1"
    NC = N_content.objects.raw(raw)
    ns = NC[0].n_content
    return render(req, 'banner1.html', {'banner1': ns})


def banner2(req):
    raw = f"select nc_id, n_content from N_content where nc_id = 9"
    NC = N_content.objects.raw(raw)
    ns = NC[0].n_content
    return render(req, 'banner2.html', {'banner2': ns})


def banner3(req):
    raw = f"select nc_id, n_content from N_content where nc_id = 40"
    NC = N_content.objects.raw(raw)
    ns = NC[0].n_content
    return render(req, 'banner3.html', {'banner3': ns})


def banner4(req):
    raw = f"select nc_id, n_content from N_content where nc_id = 64"
    NC = N_content.objects.raw(raw)
    ns = NC[0].n_content
    return render(req, 'banner4.html', {'banner4': ns})
