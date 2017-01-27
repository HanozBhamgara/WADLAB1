from django.http import HttpResponse
from django.shortcuts import render

def index(request):

    # construct a dictionary to pass to the template engine as its context
    # Note the key boldmessage is the same as {{boldmessage}} in the template
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, 'rango/index.html', context=context_dict)

    return HttpResponse("Rango says hey there partner! <Bbr/> <a> href='/rango/about/'>About</a>")

def about(request):

    return render(request, 'rango/about.html')
    return HttpResponse("This tutorial has been put together by <Hanoz> <Bbr/> Rango says here is the about page <a href='/rango/'>Index</a>")

