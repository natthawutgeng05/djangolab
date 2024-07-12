from django.contrib import admin

from gengtest_app.models import Author, Post

# Register your models here.

admin.site.register(Author)
admin.site.register(Post)