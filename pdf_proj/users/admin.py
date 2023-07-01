from django.contrib import admin
from .models import *

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ['id','name','logo','description']
admin.site.register(User, UserAdmin) 