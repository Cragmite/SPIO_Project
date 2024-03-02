from django import forms
from .models import Machine

class MachineSelectionForm(forms.Form):
    machine = forms.ModelChoiceField(queryset=Machine.objects.all(), empty_label=None)