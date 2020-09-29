from django.shortcuts import render
from django.views.generic import ListView,View
from .models import CrudUser
from django.http import JsonResponse
# Create your views here.

class CrudView(ListView):
    model = CrudUser
    template_name = 'crud_ajax/crud.html'
    context_object_name = 'users'

class CreateCrudUser(View):
    def  get(self, request):
        name1 = request.GET.get('name', None)
        address1 = request.GET.get('address', None)
        age1 = request.GET.get('age', None)

        obj = CrudUser.objects.create(
            name = name1,
            address = address1,
            age = age1
        )

        user = {'id':obj.id,'name':obj.name,'address':obj.address,'age':obj.age}

        data = {
            'user': user
        }
        return JsonResponse(data)