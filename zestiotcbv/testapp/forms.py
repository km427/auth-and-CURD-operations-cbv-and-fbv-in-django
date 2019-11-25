from django import forms

from testapp.models import student

class studentmodel(forms.ModelForm):
    class Meta:
        model=student
        fields='__all__'