from django.contrib import admin

# Register your models here.
from testapp.models import employee

class empadmin(admin.ModelAdmin):
    list_display = ['ename','eno','email']
    list_filter = ['ename']
admin.site.register(employee,empadmin)