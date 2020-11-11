from django.http import HttpResponseRedirect, request
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView,CreateView,DetailView,DeleteView,UpdateView
from Income.models import Income
from Income.forms import IncomeForm


def IncomeHome(request):
    return render(request,'SuperAdminNavbar.html')


class IncomeView(ListView):
    model = Income
    template_name = 'Income/IncomeList.html'
    context_object_name = 'Incomes'


class IncomeCreate(CreateView):
    model = Income
    template_name = 'Income/IncomeCreateForm.html'
    form_class = IncomeForm
    success_url = '/Income/'

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)


class IncomeUpdate(UpdateView):
    model = Income
    form_class = IncomeForm
    template_name = 'Income/IncomeUpdateForm.html'
    success_url = '/Income/'


class IncomeDelete(DeleteView):
    model = Income
    template_name = 'Income/IncomeDeleteForm.html'
    success_url = '/Income/'



