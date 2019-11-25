from django import forms
from testapp.models import employee
class createform(forms.ModelForm):
    class Meta:
        model=employee
        fields='__all__'