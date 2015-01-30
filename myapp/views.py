from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse
from myapp.models import Post
from datetime import datetime

def home(request):
	post_list = Post.objects.all()
	return render(request, 'home.html', {'post_list' : post_list})

