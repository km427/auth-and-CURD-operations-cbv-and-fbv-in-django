from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from testapp.models import employee
from django.urls import reverse_lazy

# Create your views here.

class emplist(ListView):
    model = employee

class empcreate(CreateView):
    model = employee
    fields = '__all__'

class empupdate(UpdateView):
    model = employee
    fields = ('ename','email')

class empdelete(DeleteView):
    model = employee
    success_url =reverse_lazy('home')