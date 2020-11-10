
from django.urls import path,include

from Income import views

urlpatterns = [
    path('IncomeHome/',views.IncomeHome,name='IncomeHome'),

]
