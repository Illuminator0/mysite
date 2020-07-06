from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Item, Tender
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm, AddItemForm
from .tables import ItemTable


def homepage(request):
    return render(request = request,
                  template_name="main/home.html",
                  context = {"items": Item.objects.all})

def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New Account Created: {username}")
            messages.info(request, f"You are now logged in as {username}")
            login(request, user)
            return redirect("main:homepage")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

    form = NewUserForm()
    return render(request,
                  "main/register.html",
                  context={"form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("main:homepage")

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect("main:homepage")
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")

    form = AuthenticationForm()
    return render(request,
                  "main/login.html",
                  {"form":form})


def tender(request):
    return render(request,
                  "main/tender.html",
                  context = {"items": Item.objects.all})

def item_list(request):
    table = ItemTable(Item.objects.all())

    return render(request, "main/item_list.html", {
        "table": table
    })

def add_item(request):
    if request.method == 'POST':
        form = AddItemForm(request.POST)
        if form.is_valid():
            # Item.item_name = form.cleaned_data['item_name']
            # Item.item_no = form.cleaned_data['item_no']
            # Item.item_quantity = form.cleaned_data['item_quantity']
            # Item.item_price = form.cleaned_data['item_price']
            # Item.item_description = form.cleaned_data['item_description']
            #Item.item_updated = datetime.now()
            Item = form.save()
            return redirect("main:items")

    else:
        form = AddItemForm()


    return render(request, "main/add_item.html", {'form': form})






