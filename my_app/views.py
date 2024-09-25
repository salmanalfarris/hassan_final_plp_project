
# my_app/views.py
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Hassan!")
