from django.shortcuts import render, get_object_or_404
from .models import poss, Category
# Create your views here.

def blog(request):
    posts = poss.objects.all()
    return render(request,"blog/blog.html",{'posts':posts})

def category(request,category_id):
    category = get_object_or_404(Category,id=category_id)
    #forma chida
    return render(request,"blog/category.html",{"category":category})
    #Forma tipica de hacer
    #posts = poss.objects.filter(categories=category)
    #return render(request,"blog/category.html",{"category":category,"posts":posts})