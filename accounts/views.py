from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from accounts.forms import UserRegisterForm, UserUpdateForm
from accounts.forms import ProfileForm


def home(request):
    if request.user.is_authenticated:
         messages.success(request,"Login Successfully")
         return redirect('IncomeHome')
    return HttpResponse("login failed")


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


def BaseHome(request):
    return render(request,'SuperAdminNavbar.html',)


def Profile(request):
    return render(request,'accounts/profile.html')


def ChangeProfile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'accounts/change_profile.html', context)