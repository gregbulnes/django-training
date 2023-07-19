from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import BlogPost
from .forms import ContactForm, BlogPostForm

from datetime import date

def blog_detail(request, post_id):
    # I didn't declare a database and connected to it
    post = BlogPost.objects.get(id=post_id)
    return render(request, 'detail.html', {'post': post})

def hello_world(request):
    return HttpResponse("<h1>Hello World!</h1>")

def blogpost_list(request):
    blogposts = BlogPost.objects.order_by("-created_at")
    today = date.today()
    name = request.user.first_name + " " + request.user.last_name.upper()

    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogpost_list')
    else:
        form = BlogPostForm()

    return render(request, 'blogpost_list.html', {'blogposts': blogposts, 'date': today, 'name': name, 'form': form})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the data in form.cleaned_data
            # send mail
            print(request.POST["name"])
            return redirect('success')
        else:
            return HttpResponse("Sorry message not sent")
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

def success(request):
    return HttpResponse((
        "<h1>Success!</h1>"
        "<p>Your form has been successfully submitted. We'll be in touch soon.</p>"
    ))















#import py2copy
#
#credentials = {
#    'username' : 'xxx',
#    'password' : 'yyy'
#}
#db_adress = 'zzz'
#
#def example_view_direct_db_interact(request, post_id):
#    # I didn't declare a database and connected to it
#    connection = pycopy.connect(credentials, db_adress)
#    data = connection.query("""
#        FROM XX
#    """)
#    #operations on data
#    to_Date
#    bon
#    return render(request, 'detail.html', {'data': data, ...})


#import some package to run dlls

#def example_view_dlls(request, post_id):
#    # I didn't declare a database and connected to it
#    data = dll_package.execute("some dll file")
#    #operations on data
#    to_Date
#    bon
#    return render(request, 'detail.html', {'data': data, ...})

#if dlls exposed in api
# import requests

#def example_view_dlls(request, post_id):
#    # I didn't declare a database and connected to it
#    data = requests.get("api url")
#    #operations on data
#    to_Date
#    bon
#    return render(request, 'detail.html', {'data': data, ...})