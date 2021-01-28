from django.contrib import admin
from .models import Blogpost, Comment, User
# Register your models here.

class BlogpostAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'date')

admin.site.register(Blogpost, BlogpostAdmin)
admin.site.register(Comment)
admin.site.register(User)