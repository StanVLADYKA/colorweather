from django.shortcuts import render
from .models import Days, Day
from .forms import SelectDay
from datetime import date



#date = '2022-07-27'
sysdate = date.today()
print(date.today())

range={40:'cw6/img/1.jpg',39:'cw6/img/2.jpg',38:'cw6/img/2.jpg',37:'cw6/img/2.jpg',36:'cw6/img/2.jpg',
    35:'cw6/img/2.jpg',34:'cw6/img/2.jpg',33:'cw6/img/2.jpg',32:'cw6/img/2.jpg',31:'cw6/img/2.jpg',
    30:'cw6/img/2.jpg',29:'cw6/img/3.jpg',28:'cw6/img/3.jpg',27:'cw6/img/3.jpg',26:'cw6/img/3.jpg',
    25:'cw6/img/3.jpg',24:'cw6/img/4.jpg',23:'cw6/img/4.jpg',22:'cw6/img/4.jpg',21:'cw6/img/4.jpg',
    20:'cw6/img/4.jpg',19:'cw6/img/5.jpg',18:'cw6/img/5.jpg',17:'cw6/img/5.jpg',16:'cw6/img/5.jpg',
    15:'cw6/img/5.jpg',14:'cw6/img/6.jpg',13:'cw6/img/6.jpg',12:'cw6/img/6.jpg',11:'cw6/img/6.jpg',
    10:'cw6/img/6.jpg',9:'cw6/img/7.jpg',8:'cw6/img/7.jpg',7:'cw6/img/7.jpg',6:'cw6/img/7.jpg',
    5:'cw6/img/7.jpg',4:'cw6/img/8.jpg',3:'cw6/img/8.jpg',2:'cw6/img/8.jpg',1:'cw6/img/8.jpg',
    0:'cw6/img/8.jpg',-1:'cw6/img/9.jpg',-2:'cw6/img/9.jpg',-3:'cw6/img/9.jpg',-4:'cw6/img/9.jpg',
    -5:'cw6/img/9.jpg',-6:'cw6/img/10.jpg',-7:'cw6/img/10.jpg',-8:'cw6/img/10.jpg',-9:'cw6/img/10.jpg',
    -10:'cw6/img/11.jpg',-11:'cw6/img/11.jpg',-12:'cw6/img/11.jpg',-13:'cw6/img/11.jpg',-14:'cw6/img/11.jpg',
    -15:'cw6/img/12.jpg',-16:'cw6/img/12.jpg',-17:'cw6/img/12.jpg',-18:'cw6/img/12.jpg',-19:'cw6/img/12.jpg',
    -20:'cw6/img/12.jpg',-21:'cw6/img/13.jpg',-22:'cw6/img/13.jpg',-23:'cw6/img/13.jpg',-24:'cw6/img/13.jpg',
    -25:'cw6/img/13.jpg',-26:'cw6/img/13.jpg',-27:'cw6/img/13.jpg',-28:'cw6/img/13.jpg',-29:'cw6/img/13.jpg',
    -30:'cw6/img/14.jpg',-31:'cw6/img/14.jpg',-32:'cw6/img/14.jpg',-33:'cw6/img/14.jpg',
}

def test(request):
    if request.method == "POST":
        newdate = SelectDay(request.POST)
        print(newdate, "форма с данными")
        if newdate.is_valid():
            postdate=newdate.cleaned_data
            sdate=postdate['date']
            sdate=str(sdate)
#            date = sdate[5:15]
#            sdate-date
#           sdate=sdate[5:15]
            print("TEST !!!!!!!!!!!!!!!!!")
            print(sdate, 'sdate in POST')
            print(date, 'date in POST')
            return sdate[5:15]
            #date=sdate
            #give_temp(request)
            #give_temp(date)


    else:
        return sysdate
  #      print('форма пустая',date)


def conv_link(tt):
    return range[tt]

def give_temp(request):
    date = sysdate
#    date = '2022-07-27'
    print(date, "1 date in def give_temp)")
    #print(sdate, "sdate in def give_temp)")
    test(request)
    date=test(request)
    #date = sdate
    print(date,'after test')

    temp = Day.objects.get(date=date)
    temp1 = int(temp.d1)
    temp2 = int(temp.d2)
    temp3 = int(temp.d3)
    temp4 = int(temp.d4)
    temp5 = int(temp.d5)
    temp6 = int(temp.d6)

    img1 = conv_link(temp1)
    img2 = conv_link(temp2)
    img3 = conv_link(temp3)
    img4 = conv_link(temp4)
    img5 = conv_link(temp5)
    img6 = conv_link(temp6)

    selday = SelectDay()


#    if request.method == "POST":
#        newdate = SelectDay(request.POST)
#        print(newdate)
#    else:
#        pass
#    testday=test(request)

    return render(request, 'cw6/index.html',
                  {
                      #"temp": temp,
                      "temp1": temp1,"temp2": temp2,
                    "temp3": temp3,"temp4": temp4, "temp5": temp5,
                    "temp6": temp6, "img1": img1,"img2": img2, "img3": img3,
                   "img4": img4,"img5": img5,"img6": img6,
                   "selday": selday,
#                   "newdate": newdate
                   })


#def manager(request):



#    p4="test44"
#    form3 = SelectDay
#    return render(request, 'cw6/templ.html', {'p': p4, 'form3':form3})

#def test2(request):
#    p2="test22"
#    form2 = TestDay()
#    return render(request, 'cw6/templ2.html', {'p': p2, 'form2':form2})

#def select_day(request):
#    sdate = SelectDay
#    return render (request, 'cw6/index.html', {"sdate": sdate})


