from django.shortcuts import render
from django.http import JsonResponse
from .models import Blog

# Create your views here.

def blog_page(request):
    return render(request, '.html')

def load_more_blogs(request):
    start = int(request.GET.get('start', 0))
    end = start + 6
    blogs = Blog.objects.all().order_by('-date')[start:end]
    
    blog_data = []
    for blog in blogs:
        blog_data.append({
            'id': blog.id,
            'title': blog.title,
            'image_url': blog.image.url,
            'content': blog.content,
        })
    
    return JsonResponse(blog_data, safe=False)