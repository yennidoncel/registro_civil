from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import ActaDefuncion, Persona, RegistradorCivil, Fallecido, Declarante, Defuncion, Autoridad
from base.models import Parroquia
from .forms import ActaDefuncionForm, RegistradorCivilForm, FallecidoForm, DeclaranteForm, DefuncionForm, AutoridadForm

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

        registrador_civil = RegistradorCivil.objects.get(pk=form.cleaned_data['registrador_civil'])
        self.object.registrador_civil = registrador_civil

        fallecido = Fallecido.objects.get(pk=form.cleaned_data['fallecido'])
        self.object.fallecido = fallecido

        declarante = Declarante.objects.get(pk=form.cleaned_data['declarante'])
        self.object.declarante = declarante

        defuncion = Defuncion.objects.get(pk=form.cleaned_data['defuncion'])
        self.object.defuncion = defuncion

        return super(ActaDefuncionCreate, self).form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super(ActaDefuncionCreate, self).form_invalid(form)

class RegistradorCivilCreate(CreateView):

    model = RegistradorCivil
    form_class = RegistradorCivilForm
    template_name = "acta.registrador.civil.template.html"
    success_url = reverse_lazy('acta_defuncion_registro')

    def form_valid(self, form):
        persona = Persona.objects.create(
            nombre = form.cleaned_data['nombre'],
            apellido = form.cleaned_data['apellido'],
            cedula = form.cleaned_data['cedula'],
        )

        self.object = form.save(commit=False)
        self.object.resolucion = form.cleaned_data['resolucion']
        self.object.fecha_resolucion = form.cleaned_data['fecha_resolucion']
        self.object.gaceta = form.cleaned_data['gaceta']
        self.object.tipo_gaceta = form.cleaned_data['tipo_gaceta']
        self.object.fecha_gaceta = form.cleaned_data['fecha_gaceta']
        self.object.persona = persona
        return super(RegistradorCivilCreate, self).form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super(RegistradorCivilCreate, self).form_invalid(form)

class FallecidoCreate(CreateView):

    model = Fallecido
    form_class = FallecidoForm
    template_name = "acta.fallecido.template.html"
    success_url = reverse_lazy('acta_defuncion_registro')

    def form_valid(self, form):
        persona = Persona.objects.create(
            nombre = form.cleaned_data['nombre'],
            apellido = form.cleaned_data['apellido'],
            cedula = form.cleaned_data['cedula'],
        )

        self.object = form.save(commit=False)
        self.object.fecha_nacimiento = form.cleaned_data['fecha_nacimiento']
        self.object.sexo = form.cleaned_data['sexo']
        self.object.edad = form.cleaned_data['edad']
        self.object.estado_civil = form.cleaned_data['estado_civil']
        self.object.profesion = form.cleaned_data['profesion']
        self.object.ocupacion = form.cleaned_data['ocupacion']
        self.object.direccion = form.cleaned_data['direccion']
        #lugar_nacimiento = Parroquia.objects.get(pk=form.cleaned_data['lugar_nacimiento'])
        self.object.lugar_nacimiento = form.cleaned_data['lugar_nacimiento']
        self.object.persona = persona
        return super(FallecidoCreate, self).form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super(FallecidoCreate, self).form_invalid(form)

class DeclaranteCreate(CreateView):

    model = Declarante
    form_class = DeclaranteForm
    template_name = "acta.declarante.template.html"
    success_url = reverse_lazy('acta_defuncion_registro')

    def form_valid(self, form):
        persona = Persona.objects.create(
            nombre = form.cleaned_data['nombre'],
            apellido = form.cleaned_data['apellido'],
            cedula = form.cleaned_data['cedula'],
        )

        self.object = form.save(commit=False)
        self.object.edad = form.cleaned_data['edad']
        self.object.profesion = form.cleaned_data['profesion']
        self.object.ocupacion = form.cleaned_data['ocupacion']
        self.object.direccion = form.cleaned_data['direccion']
        self.object.persona = persona
        return super(DeclaranteCreate, self).form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super(DeclaranteCreate, self).form_invalid(form)

class DefuncionCreate(CreateView):

    model = Defuncion
    form_class = DefuncionForm
    template_name = "acta.defuncion.template.html"
    success_url = reverse_lazy('acta_defuncion_registro')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.fecha_hora = form.cleaned_data['fecha_hora']
        self.object.causa = form.cleaned_data['causa']
        self.object.certificado_defuncion = form.cleaned_data['certificado_defuncion']
        self.object.direccion = form.cleaned_data['direccion']
        self.object.lugar = form.cleaned_data['lugar']
        autoridad = Autoridad.objects.get(pk=form.cleaned_data['autoridad'])
        self.object.autoridad = autoridad
        return super(DefuncionCreate, self).form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super(DefuncionCreate, self).form_invalid(form)

class AutoridadCreate(CreateView):

    model = Autoridad
    form_class = AutoridadForm
    template_name = "acta.autoridad.template.html"
    success_url = reverse_lazy('defuncion')

    def form_valid(self, form):
        persona = Persona.objects.create(
            nombre = form.cleaned_data['nombre'],
            apellido = form.cleaned_data['apellido'],
            cedula = form.cleaned_data['cedula'],
        )
        self.object = form.save(commit=False)
        self.object.numero_mpps = form.cleaned_data['numero_mpps']
        self.object.persona = persona
        return super(AutoridadCreate, self).form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super(AutoridadCreate, self).form_invalid(form)
