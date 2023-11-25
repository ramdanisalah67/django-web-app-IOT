from django.urls import  path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('getSum', views.sumCalc, name='sumCalc')

]