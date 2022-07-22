from django.shortcuts import render
#from .models import Days
#from django.http import HttpResponse

#def home(request, slug=None):
    #context = {
    #    "categories": Category.objects.all(),
    #}
#return render(request, "cw6/index.html", context)
# Create your views here.

def index(request):
    return render(request, 'index.html')

#def test(request):
#    return HttpResponse ("TEST PAGE")
