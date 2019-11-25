from django import forms
from testapp.models import employees
from django.contrib.auth.models import User

class userform(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','email']