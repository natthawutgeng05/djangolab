from django.contrib import admin

# Register your models here.

from restnews.models import NewsPost

admin.site.register(NewsPost)