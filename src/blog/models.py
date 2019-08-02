from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model



User = settings.AUTH_USER_MODEL
DEFAULT_ID = 1
# Create your models here.
class Blog(models.Model):

	name = models.ForeignKey(User, default = DEFAULT_ID, null = True, on_delete = models.SET_NULL)
	post = models.TextField()
	#name = models.CharField(default = )

    

	#blogpost_set.all() gets all the blog posts from the user






