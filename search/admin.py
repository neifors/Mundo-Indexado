from django.contrib import admin
from .models import Web, Article, Alert

# Register your models here.
admin.site.register(Web)
admin.site.register(Article)
admin.site.register(Alert)