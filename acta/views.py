from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import ActaDefuncion
from .forms import ActaDefuncionForm

# Create your views here.

class ActaDefuncionList(ListView):
    model = ActaDefuncion
    template_name = "acta.listar.template.html"

class ActaDefuncionCreate(CreateView):
    model = ActaDefuncion
    form_class = ActaDefuncionForm
    template_name = "acta.registro.template.html"
    success_url = reverse_lazy('acta_defuncion')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.numero_acta = form.cleaned_data['numero_acta']
        self.object.numero_folio = form.cleaned_data['numero_folio']
        self.object.anho = form.cleaned_data['anho']
        self.object.registrador_civil = form.cleaned_data['registrador_civil']
        self.object.fallecido = form.cleaned_data['fallecido']
        self.object.declarante = form.cleaned_data['declarante']
        return super(ActaDefuncionCreate, self).form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super(ActaDefuncionCreate, self).form_invalid(form)
