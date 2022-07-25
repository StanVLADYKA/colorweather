from django.shortcuts import render
from .models import Days

#from .models import Days
#from django.http import HttpResponse

#def home(request, slug=None):
    #context = {
    #    "categories": Category.objects.all(),
    #}
#return render(request, "cw6/index.html", context)
# Create your views here.

#def index(request):
#    return render(request, 'cw6/home.html')



def give_temp(request):
    #dd = Days.objects.all()
    temp = Days.objects.filter(date='2022-07-27')
    return render(request, 'cw6/home.html', {"temp": temp})


"""select * from cw6_days;"""
#def test(request):
#    return HttpResponse ("TEST PAGE")
