from django.contrib import admin
from .models import Contact
from .models import Post

admin.site.register(Contact)
admin.site.register(Post)