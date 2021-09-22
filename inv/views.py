from django import forms
from django.shortcuts import get_object_or_404, render, redirect
from django.core.mail import send_mail

from .models import Products
from .forms import AddProductForm


# Create your views here.

def index(request):
    products = Products.objects.all()
    context = {
        'products' : products,
    }

    return render(request, 'index.html', context)

def addProduct(request):
    if request.method == "POST":
        form = AddProductForm(request.POST)

        if form.is_valid():
            form.save()

            if int(form.cleaned_data['quantity']) == 0:
                sendEmail(form.cleaned_data['name'], form.cleaned_data['category'])

            return redirect('index')

    else:
        form = AddProductForm
        return render(request, 'addNewProduct.html', {'form' : form})

def editProduct(request, pk):
    product = get_object_or_404(Products, pk=pk)

    if request.method == "POST":
        form = AddProductForm(request.POST, instance=product)

        if form.is_valid():
            form.save()

            if int(form.cleaned_data['quantity']) == 0:
                sendEmail(form.cleaned_data['name'], form.cleaned_data['category'])

            return redirect('index')

    else:
        form = AddProductForm(instance=product)
        return render(request, 'editProduct.html', {'form' : form})

def deleteProduct(request, pk):
    get_object_or_404(Products, pk=pk).delete()

    return index(request)

def sendEmail(product, category):
    subject = "0 Inventory Alert!"
    message = 'Product "{}" ({}) has been added or edited and has 0 inventory!'.format(product, category)
    sender = "testing@example.com"
    to = ["testing@example.com"]

    send_mail(subject, message, sender, to)

def displayGraph(request):
    products = Products.objects.all()
    
    # context_category = {
    #     'Food'    : 0,
    #     'Clothes' : 0,
    #     'Other'   : 0,
    # }
    # for p in products:
    #     context_category[p.category] += 1
    
    # print(context_category)

    # context_all = {
    #     'products' : products,
    # }

    # context = {
    #     'category' : context_category,
    #     'all'      : context_all,
    # }

    products = Products.objects.all()
    context = {
        'products' : products,
    }

    return render(request, 'graphs.html', context)
