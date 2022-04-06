from django.contrib import admin
from .models import Post, Comment
# Register your models here.

my_models = [Post, Comment]

admin.site.register(my_models)
