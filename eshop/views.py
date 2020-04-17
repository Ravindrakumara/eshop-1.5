from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.http import JsonResponse
from.models import Registration
from.models import Brands
from.models import Categories
from.models import item
from django.views import generic
# Create your views here.

def land(request):
    brand = Brands.objects.all()
    Regi = Registration.objects.all()
    cat = Categories.objects.all()
    Item = item.objects.all()
    return render(request, "index.html", {'brand': brand, 'Regi': Regi , 'cat':cat ,'Item':Item})
 

def items(request,id):  
    brand = Brands.objects.all()
    Regi = Registration.objects.all()
    cat = Categories.objects.all()
    #Item = item.objects.all()
    Item = item.objects.filter(id=id)
    return render(request,"Product-details.html", {'brand': brand, 'Regi': Regi , 'cat':cat ,'Item':Item})
#class item(generic.):
    #pass
    print(Item)

def shop(request):
    brand = Brands.objects.all()
    Regi = Registration.objects.all()
    cat = Categories.objects.all()
    Item = item.objects.all()
    return render(request, "shop.html", {'brand': brand, 'Regi': Regi, 'cat': cat, 'Item': Item})


def Account(request):
    brand = Brands.objects.all()
    Regi = Registration.objects.all()
    cat = Categories.objects.all()
    Item = item.objects.all()
    return render(request, "login.html", {'brand': brand, 'Regi': Regi, 'cat': cat, 'Item': Item})


def cart(request):
    #brand = Brand.objects.all()
    Regi = Registration.objects.all()
    #cat = Catogory.objects.all()
    Item = item.objects.all()
    return render(request, "cart.html", {'Regi': Regi,'Item': Item})
