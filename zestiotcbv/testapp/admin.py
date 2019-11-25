from django.contrib import admin

# Register your models here.
from testapp.models import student

class studentadmin(admin.ModelAdmin):
    list_display =['name','email','phno']

admin.site.register(student,studentadmin)