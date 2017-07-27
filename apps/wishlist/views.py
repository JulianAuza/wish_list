# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re 
from django.shortcuts import render,redirect
from django.contrib import messages
from models import User, Item, Wishlist
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your views here.
def index(request):
   
    return render(request, 'wishlist/login.html')

def login(request):
    request.session.modified = True
    login_email=request.POST['email']
    login_password=request.POST['password']

    message=''
    try:
        user = User.objects.get(email=login_email)
        request.session['user_email']= user.email
        account=True 
    except:
    # if not User.objects.filter(email=request.POST['email']):
        message+= "/ "+'email not recognized'
        account = False
        messages.error(request,message)
        return redirect('/')
    else:
        if len(login_password) < 8:
            message+= "/ "+'Password must be atleast 8 characters'
            messages.error(request,message)
            return redirect('/')

        if user.password != login_password:
            message+= "/ "+'incorrect password'
            messages.error(request,message)
            return redirect('/')
        else:
            user = User.objects.get(email=login_email)
            request.session['userid']= user.id
            request.session.modified = True
            return redirect('/home')

def sign_up(request):
    search= User.objects.filter(email=request.POST['email'])
    message=''
    if not EMAIL_REGEX.match(request.POST['email']):
        message+= "/ "+'invalid email'
    if (len(str(request.POST['password'])) < 7) :
        message+= "/ "+'Password must be atleast 8 characters'
    if (str(request.POST['password']) != str(request.POST['confirm'])):
        message+= "/ "+'Passwords do not match'
    if len(search):
        message+= "/ "+'email already exists'
    if (message != ''):
        messages.error(request,message)
        return redirect('/')
    else:
        name = request.POST['name']
        user_name = request.POST['user_name']
        email = request.POST['email']
        password= request.POST['password']
        User.objects.create(name = name , email= email, password = password)
        user = User.objects.get(email=email)
        request.session['user_email']= user.email
        print user.email
        request.session.modified = True
        return redirect('/home')

def home(request):
    user = User.objects.get(email=request.session['user_email'])
    not_items = Item.objects.exclude(add_by=user)
    fave_list= Wishlist.objects.filter(owner=user)
    items= Item.objects.filter(add_by=user)
    
    exclude =[]
    for item in fave_list:
        print item.item.name
        exclude.append(item.item.name)
    print exclude
   
    
    context={
       'user': user,
       'items':items, 
       'list': fave_list,
       'not_items':not_items,
       'exclude':exclude

    }

    return render (request, 'wishlist/home.html',context)

def add_item(request):
    user = User.objects.get(email=request.session['user_email'])
    print user.name
    name = request.POST['item']
    message=''
    search = Item.objects.filter(name=request.POST['item'])
    print search

    if len(name) < 2:
        message+= "/ "+'enter valid item'
        messages.error(request,message)
        return redirect('/home')

    elif len(search):
        message+= "/ "+'item already exists'
        messages.error(request,message)
        return redirect('/home')
    else:
        Item.objects.create(name= name, add_by= user)
        return redirect('/home')

def delete_item(request):
    itemid=request.POST['item_id']
    item = Item.objects.get(id=itemid)
    item.delete()

    return redirect('/home')

def log_out(request):
    request.session['userid']= ''
    return redirect ('/')


def add_to_wish(request):
    user = User.objects.get(email=request.session['user_email'])
    owner = user
    itemid = request.POST['item_id']
    item = Item.objects.get(id= itemid)
    wishlist = Wishlist.objects.create(owner=owner,item=item)

    return redirect ('/home')

def remove_list_item(request):
    item_id=request.POST['item_id']
    print item_id
    wishitem = Wishlist.objects.get(id=item_id)
    print wishitem.item.name
    wishitem.delete()


    return redirect ('/home')

def wishers(request,word):
    user = User.objects.get(email=request.session['user_email'])
    not_items = Item.objects.exclude(add_by=user)
    fave_list= Wishlist.objects.all()
    items= Item.objects.filter(add_by=user)
    item_name = str(word)
    print item_name
   

    context={
       'user': user,
       'items':items, 
       'list': fave_list,
       'not_items':not_items,
       'item_name':item_name
    }

    
    return render(request,'wishlist/wishers.html',context)
    
    

