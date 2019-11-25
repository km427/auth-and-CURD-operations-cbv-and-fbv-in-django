from django.contrib import admin

# Register your models here.
from testapp.models import employees

class empadmin(admin.ModelAdmin):
    list_display = ['name','phno','email']
admin.site.register(employees,empadmin)