# coding='utf-8'
from django.shortcuts import render
from django.utils import timezone
from .models import Post # view에다가 같은 폴더에 있는 models에 있는 Post를 가져옴
from django.shortcuts import render, get_object_or_404

# Create your views here.

def post_list(request):
#    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts = Post.objects.order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
