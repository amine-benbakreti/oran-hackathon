# In your Django app views.py file

from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello, world!")
