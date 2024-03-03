from django import forms
from .models import Machine, Failure

class MachineSelectionForm(forms.Form):
    machine = forms.ModelChoiceField(queryset=Machine.objects.all(), empty_label=None)


class FailureSelectionForm(forms.Form):
    failure = forms.ModelChoiceField(queryset=Failure.objects.all(), empty_label=None)