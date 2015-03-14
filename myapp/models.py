from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.sites.models import Site
from django import forms 
from django.forms.widgets import *
from django.core.mail import send_mail, BadHeaderError
from ckeditor.fields import RichTextField

# Create your models here.

class Post(models.Model) : 
	title = models.CharField(max_length = 100) 
	category = models.CharField(max_length = 50, blank = True)
	date_time = models.DateTimeField(auto_now_add = True)
	content = RichTextField()

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
    pic = RichTextField(config_name = 'pic')
    linkedin = models.CharField(max_length = 100)

    def __str__(self):
        return self.name.encode('utf-8')


class Gallery(models.Model) :
    pic = RichTextField(config_name = 'pic')
    team = models.CharField(max_length = 50)
		