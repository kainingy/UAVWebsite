from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.sites.models import Site
from django import forms 
from django.forms.widgets import *
from django.core.mail import send_mail, BadHeaderError

# Create your models here.

class Post(models.Model) : 
	title = models.CharField(max_length = 100) 
	category = models.CharField(max_length = 50, blank = True)
	date_time = models.DateTimeField(auto_now_add = True)
	content = models.TextField(blank = True, null = True)

	def get_absolute_url(self):
        	path = reverse('detail', kwargs={'id':self.id})
        	return "http://127.0.0.1:8000%s" % path

	def __str__(self):
    		return self.title.encode('utf-8')


  	class Meta:
        	ordering = ['-date_time']


class ContactForm(forms.Form):
    email = forms.EmailField()
    topic = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

class Member(models.Model) :
    name = models.CharField(max_length = 100)
    team = models.CharField(max_length = 50)
    pic = models.CharField(max_length = 200)
    linkedin = models.CharField(max_length = 100)

    def __str__(self):
        return self.name.encode('utf-8')


class Gallary(models.Model) :
    pic = models.CharField(max_length = 200)
    team = models.CharField(max_length = 50)
		