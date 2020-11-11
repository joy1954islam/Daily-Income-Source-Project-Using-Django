
from django.urls import path,include

from Income import views

urlpatterns = [
    path('IncomeHome/',views.IncomeHome,name='IncomeHome'),
    path('IncomeCreate/',views.IncomeCreate.as_view(),name='IncomeCreate'),
    path('IncomeUpdate/<int:pk>',views.IncomeUpdate.as_view(),name='IncomeUpdate'),
    path('IncomeDelete/<int:pk>',views.IncomeDelete.as_view(),name='IncomeDelete'),
    path('Income/',views.IncomeView.as_view(),name='Income'),

]
