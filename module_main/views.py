from django.shortcuts import render, HttpResponse
from django.views.generic import FormView
from django.urls import reverse_lazy
from .forms import MachineSelectionForm
from .models import Machine

# Create your views here.

def home(request):
    return render(request, "home.html")


class MachineListView(FormView):
    template_name = 'machine_list.html'
    form_class = MachineSelectionForm
    success_url = reverse_lazy('selected_machine')

    def form_valid(self, form):
        selected_machine = form.cleaned_data['machine']
        self.request.session['selected_machine'] = selected_machine.pk
        return super().form_valid(form)

def selected_machine(request):
    machine_pk = request.session.get('selected_machine')
    selected_machine = Machine.objects.get(pk=machine_pk)
    return render(request, 'selected_machine.html', {'selected_machine': selected_machine})