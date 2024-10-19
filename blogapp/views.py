from django.shortcuts import render
from blogapp.models import Post
# Create your views here.

def index(request):
 posts = Post.objects.all()
 return render(request,"blogapp/index.html",{"allposts": posts})

def single_post(request,post_id):
 post = Post.objects.get(id=post_id)
 return render(request,"blogapp/single_post.html",{"post": post})

