from django.http import HttpResponse

def about(request):
    return HttpResponse("Rango says here is the about page")


