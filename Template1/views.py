from django.shortcuts import render
from .models import Baiviet

def list(request):
    Data = {'Baiviet': Baiviet.objects.all().order_by('date')}
    return render(request, 'pages/blog.html', Data)

def post(request, id):
    post = Baiviet.objects.get(id=id)
    return render(request, 'pages/post.html', {'post': post})