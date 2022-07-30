from django.urls import path
from . import views
from django.urls import include


urlpatterns = [
    path ('', views.give_temp, name = 'give_temp'),
#    path ('index/', views.give_temp, name = 'give_temp2'),
#    path ('temp/', views.test, name = 'test'),
#    path('temp2/', views.test2, name='test')
#    path('search', views.select_day, name="searched")
]