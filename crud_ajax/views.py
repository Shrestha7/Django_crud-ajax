from django.shortcuts import render
from django.views.generic import ListView
from .models import CrudUser
# Create your views here.

class CrudView(ListView):
    model = CrudUser
    template_name = 'crud_ajax/crud.html'
    context_object_name = 'users'