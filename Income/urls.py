
from django.urls import path,include

from Income import views

urlpatterns = [
    path('IncomeHome/',views.IncomeHome,name='IncomeHome'),
    path('IncomeCreate/',views.IncomeCreate.as_view(),name='IncomeCreate'),
    path('Income/',views.IncomeView.as_view(),name='Income'),

]
