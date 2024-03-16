from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Post


# Create your views here.
# ______________________________________________________________________
def posts_list(request):
    posts = Post.objects.all().order_by("-date")
    return render(request, "posts/posts_list.html", {"posts": posts})


# ______________________________________________________________________
def post_page(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, "posts/post_page.html", {"post": post})


# ______________________________________________________________________
@login_required(login_url="/users/login/")
def post_new(request):
    return render(request, "posts/post_new.html")
