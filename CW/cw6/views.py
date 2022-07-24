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
    #d=input("enter id days")
    #dd = Days.objects.all()
    dd = Days.objects.filter(date='2022-07-24')
    d1 = Days.objects.all()
    #dd = Days.objects.all()
    #dd = Days.objects.filter(id='1')
    #print(dd)
    return render(request, 'cw6/home.html', {'dd' : dd})
                  #{'d1' : d1}

"""select * from cw6_days;"""
#def test(request):
#    return HttpResponse ("TEST PAGE")
