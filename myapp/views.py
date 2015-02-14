from django.shortcuts import render
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from myapp.models import Post
from datetime import datetime
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from myapp.models import ContactForm
from django.template import RequestContext, Context
from django import forms 
from django.forms.widgets import *
from django.core.mail import send_mail
from myapp.models import ContactForm

def contactview(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['topic'],
                cd['message'],
                cd['email'],
                ['896736975@qq.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm()
    return render(request, 'contacts.html', {'form': form})

def thankyou(request):
        return render(request, 'thankyou.html')


def home(request):
	posts = Post.objects.all()
	paginator = Paginator(posts, 3)
	page = request.GET.get('page')
	try:
		post_list = paginator.page(page)
	except PageNotAnInteger :
		post_list = paginator.page(1)
	except EmptyPage :
		post_list = paginator.paginator(paginator.num_pages)
	return render(request, 'home.html', {'post_list' : post_list})

def detail(request, id):
    try:
        post = Post.objects.get(id=str(id))
    except Post.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post' : post})

def index(request):
	return render(request, 'index.html')

def archives(request) :
    try:
        post_list = Post.objects.all()
    except Post.DoesNotExist :
        raise Http404
    return render(request, 'archives.html', {'post_list' : post_list, 
                                            'error' : False})

def search_tag(request, tag) :
    try:
        post_list = Post.objects.filter(category__iexact = tag) #contains
    except Post.DoesNotExist :
        raise Http404
    return render(request, 'tag.html', {'post_list' : post_list})
