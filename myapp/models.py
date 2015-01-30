from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.sites.models import Site

# Create your models here.

class Post(models.Model) : 
	title = models.CharField(max_length = 100) 
	category = models.CharField(max_length = 50, blank = True)
	date_time = models.DateTimeField(auto_now_add = True)
	content = models.TextField(blank = True, null = True)

	def __str__(self):
    		return self.title.encode('utf-8')

  	class Meta:
        	ordering = ['-date_time']
		