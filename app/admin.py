from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Page)
admin.site.register(Type)
admin.site.register(Topic)
admin.site.register(Link)