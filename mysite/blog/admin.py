from django.contrib import admin
from .models import Post, Comment #Import models you created here

# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)
