from datetime import date
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from ManageObject.models import *

# Create your views here.
class MemberCreate(CreateView): 
    model = Member
    template_name = "Login.html"
    fields = ['firstName', 'lastName', 'email', 'password']
    success_url = reverse_lazy("signIn")

def signIn(request):
    return render(request, "SignIn.html")

def login(request):
    member = Member.objects.get(email=request.POST['email'])
    if(member.password == request.POST['password']):
        return redirect("/Home/"+member.slug)
    msg = "Email ou mot de passe incorrecte"
    return render(request, "SignIn.html", {"msg" : msg})

def home(request, slug):
    member = Member.objects.get(slug = slug)
    list = List.objects.filter(member=member.pk)
    context = {
        "firstName" : member.firstName,
        "lastName" : member.lastName,
        "slugMember" : member.slug,
        "list" : list,
    }
    return render(request, "home.html", context)

def createListForm(request, slug):
    context = {
        "slugMember" : slug
    }
    return render(request, "createList.html", context)

def creationList(request, slug):
    member = Member.objects.get(slug=slug)
    list = List()
    list.title = request.POST['title']
    list.member = member
    list.save()
    list = List.objects.last()
    return redirect("/Home/"+slug+"/"+list.slug)
    
def addObject(request, slug, list):
    list = List.objects.get(slug=list)
    object = list.product_set.all()
    sum = 0
    for o in object : 
        sum += o.price*o.number
    if list.date == date.today() : 
        edit = True
    else : 
        edit = False 
    context = {
        "edit" : edit,
        "list" : list.slug,
        "slug" : slug,
        "object" : object,
        "sum" : sum,
        "slug" : slug,
    }
    
    return render(request, "addObject.html", context)

def addingObject(request, slug, list):
    form = AddObjectForm(request.POST)
    if form.is_valid : 
        object = Product()
        object.name = request.POST['name']
        object.price = request.POST['price']
        object.number = request.POST['number']
        list = List.objects.get(slug=list)
        object.list = list
        object.save()
        return redirect("/Home/"+slug+"/"+list.slug)
    else : 
        return redirect("/Home/"+slug+"/"+list+"/")
    
def deleteObject(request, slug, list, id):
    object = Product.objects.get(pk=id)
    object.delete()
    return redirect("/Home/"+slug+"/"+list)

def deleteList(request, slug, list):
    list = List.objects.get(slug=list)
    list.delete()
    return redirect("/Home/"+slug)