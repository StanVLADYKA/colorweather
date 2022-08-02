from django.shortcuts import render
from .models import Day
from .forms import SelectDay
from datetime import date
import requests


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

def setday(request):               #  функция перерасчета отображения при выборе новой даты
    if request.method == "POST":
        newdate = SelectDay(request.POST)
        if newdate.is_valid():
            postdate=newdate.cleaned_data
            sdate=postdate['date']
            sdate=str(sdate)
            return sdate[5:15]
    else:
        return sysdate


def createforecast(sysdate):   # функция создания экземпляра модели Day если её нет на текущую дату
    try:                       # используется запрос данных на 8 дней из ресурса : penweathermap.org
        info = Day.objects.get(date=sysdate)
    except:
        url = 'https://api.openweathermap.org/data/3.0/onecall?lat=53.94&lon=27.59&units=metric&exclude=current,minutely,hourly,alerts&appid=3fa7183f2bd29d62f19b1de12be26a15'
        res = requests.get(url).json()
        res1 = res['daily']
        print("ALARM!!! до 1000 запросов в день бесплатно")
        listtemp = [str(sysdate)]
        for key in res1:
            listtemp.append(round(key['temp']['max']))
        Day.objects.create(date=listtemp[0], d1=listtemp[1], d2=listtemp[2], d3=listtemp[3],
                           d4=listtemp[4], d5=listtemp[5], d6=listtemp[6], d7=listtemp[7])
    else:
        pass


def conv_link(tt):  # функция возврата ссылки на картинку по данным температуры
    return range[tt]

def give_temp(request): # основная функция, запускается из домашней страницы

    createforecast(sysdate) # вызывает функцию, если нет прогноза от текущей даты в модели, записываес в Day

    date=setday(request)  # при выборе на сайте новой даты, вызываес функцию с перерисовкой

    temp = Day.objects.get(date=date)
    temp1 = int(temp.d1)
    temp2 = int(temp.d2)
    temp3 = int(temp.d3)
    temp4 = int(temp.d4)
    temp5 = int(temp.d5)
    temp6 = int(temp.d6)
    temp7 = int(temp.d7)

    img1 = conv_link(temp1)
    img2 = conv_link(temp2)
    img3 = conv_link(temp3)
    img4 = conv_link(temp4)
    img5 = conv_link(temp5)
    img6 = conv_link(temp6)
    img7 = conv_link(temp7)

    selday = SelectDay()  # ссылка на форму для выбора даты (формат odelChoiceField)

    return render(request, 'cw6/index.html',
                  {
                      "temp1": temp1,"temp2": temp2,"temp3": temp3,"temp4": temp4,
                      "temp5": temp5, "temp6": temp6, "temp7": temp7,
                      "img1": img1,"img2": img2, "img3": img3, "img4": img4,
                      "img5": img5,"img6": img6, "img7": img7, "selday": selday,
                      "date": str(date)
                   })

