from django.shortcuts import render, redirect
from .models import item, cartItem


def loadHomePage(request):
    return render(request, 'home.html')


def loadVegetables(request):
    items = item.objects.raw("SELECT * FROM Market_item WHERE category = 'Vegetable'")

    return render(request, 'final_index.html', {'items': items})


def loadFruits(request):
    items = item.objects.raw("SELECT * FROM Market_item WHERE category = 'Fruit'")

    return render(request, 'final_index.html', {'items': items})


def loadCereals(request):
    items = item.objects.raw("SELECT * FROM Market_item WHERE category = 'Cereal'")

    return render(request, 'final_index.html', {'items': items})

def add(request):
    name = request.POST['name']
    qty = int(request.POST['qty'])

    cate = None

    items = item.objects.all()

    ci = cartItem()

    ci.name = name
    ci.qty = qty

    for i in items:
        if i.name == ci.name:
            ci.price = i.price
            cate = i.category

    ci.total = ci.qty * ci.price

    ci.save()

    list = []

    for i in items:
        if i.category == cate:
            list.append(i)

    return render(request, 'final_index.html', {'items': list})

def bookpage(request):
    items = item.objects.all()

    tot = 0

    cartItems = cartItem.objects.all()

    for j in cartItems:
        tot = tot + j.total


    return render(request, 'final_page.html', {'cartItems': cartItems, 'items': items, 'total':tot})

def confirm(request):
    cartItems = cartItem.objects.all()

    cartItems.delete()

    return render(request, 'home.html')