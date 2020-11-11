from django.forms import ModelForm

from Income.models import Income


class IncomeForm(ModelForm):
    class Meta:
        model = Income
        fields = ['amount','description','Source','currency']
