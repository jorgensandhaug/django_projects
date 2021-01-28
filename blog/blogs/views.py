from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Comment, Blogpost

from django.shortcuts import render

# Create your views here.

def index(request):
    blogposts = Blogpost.objects.all()

    return render(request, 'index.html', {'blogposts': blogposts})


def detail(request, blog_id):
    blogpost = get_object_or_404(Blogpost, pk=blog_id)

    comments = Comment.objects.filter(blogpost = blogpost)
    return render(request, 'detail.html', {'comments': comments, 'blogpost': blogpost})
