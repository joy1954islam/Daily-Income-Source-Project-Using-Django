
from django.urls import path,include

from Income import views

urlpatterns = [
    path('',views.Home,name = 'home'),

]
