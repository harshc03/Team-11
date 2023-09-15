
from django.shortcuts import render
from .models import Blogs

def blog_list(request):
    blogs = Blogs.objects.all()
    print(blogs)
    return render(request, 'blogs/index.html', {'blogs': blogs})
