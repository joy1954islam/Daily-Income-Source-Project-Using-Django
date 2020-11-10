from django.shortcuts import render

# Create your views here.


def IncomeHome(request):
    return render(request,'SuperAdminNavbar.html')