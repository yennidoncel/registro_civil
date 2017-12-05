from django import forms
from django.utils.translation import ugettext_lazy as _
from base.fields import CedulaField
from base.constant import TIPO_GACETA, SEXO, ESTADO_CIVIL
from base.models import Estado, Municipio, Parroquia
from .models import ActaDefuncion, RegistradorCivil, Fallecido, Declarante, Defuncion, Autoridad

class ActaDefuncionForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ActaDefuncionForm, self).__init__(*args, **kwargs)

        lista_rc = [('','Selecione...')]
        for rc in RegistradorCivil.objects.all():
            lista_rc.append( (rc.id,rc) )
        self.fields['registrador_civil'].choices = lista_rc

        lista_fa = [('','Selecione...')]
        for fa in Fallecido.objects.all():
            lista_fa.append( (fa.id,fa) )
        self.fields['fallecido'].choices = lista_fa

        lista_de = [('','Selecione...')]
        for de in Declarante.objects.all():
            lista_de.append( (de.id,de) )
        self.fields['declarante'].choices = lista_de

        lista_df = [('','Selecione...')]
        for df in Defuncion.objects.all():
            lista_df.append( (df.id,df) )
        self.fields['defuncion'].choices = lista_df

        # Si se ha seleccionado un estado establece el listado de municipios y elimina el atributo disable
        if 'estado' in self.data and self.data['estado']:
            self.fields['municipio'].widget.attrs.pop('disabled')
            self.fields['municipio'].queryset=Municipio.objects.filter(estado=self.data['estado'])

            # Si se ha seleccionado un municipio establece el listado de parroquias y elimina el atributo disable
            if 'municipio' in self.data and self.data['municipio']:
                self.fields['parroquia'].widget.attrs.pop('disabled')
                self.fields['parroquia'].queryset=Parroquia.objects.filter(municipio=self.data['municipio'])

    numero_acta = forms.CharField(
        label = _("Número de Acta"),
        max_length = 10,
        widget = forms.TextInput(
            attrs = {
                'class':'form-control input-sm', 'data-toggle':'tooltip', 'style':'width:250px;',
                'title':_("indique el Número de Acta"),
            }
        )
    )

    numero_folio = forms.CharField(
        label = _("Número de Folio"),
        max_length = 10,
        widget = forms.TextInput(
            attrs = {
                'class':'form-control input-sm', 'data-toggle':'tooltip', 'style':'width:250px;',
                'title':_("indique el Número de Folio"),
            }
        )
    )

    anho= forms.CharField(
        label = _("Año"),
        max_length = 4,
        widget = forms.TextInput(
            attrs = {
                'class':'form-control input-sm', 'data-toggle':'tooltip', 'style':'width:250px;',
                'title':_("indique el Año"),
            }
        )
    )

    registrador_civil = forms.ChoiceField(
        label = _("Registrador Civil"),
        widget = forms.Select(
            attrs = {
                'class':'form-control select2', 'data-toggle':'tooltip', 'style':'width:250px;',
                'title':_("Seleccione al Registrador Civil"),
            }
        )
    )

    fallecido = forms.ChoiceField(
        label = _("Fallecido"),
        widget = forms.Select(
            attrs = {
                'class':'form-control select2', 'data-toggle':'tooltip', 'style':'width:250px;',
                'title':_("Seleccione al Fallecido"),
            }
        )
    )

    declarante = forms.ChoiceField(
        label = _("Declarante"),
        widget = forms.Select(
            attrs = {
                'class':'form-control select2', 'data-toggle':'tooltip', 'style':'width:250px;',
                'title':_("Seleccione al Declarante"),
            }
        )
    )

    defuncion = forms.ChoiceField(
        label = _("Defunción"),
        widget = forms.Select(
            attrs = {
                'class':'form-control select2', 'data-toggle':'tooltip', 'style':'width:250px;',
                'title':_("Seleccione los datos de Defunción"),
            }
        )
    )

    class Meta:
        model = ActaDefuncion
        exclude = [
            'registrador_civil','fallecido','declarante', 'defuncion'
        ]

class RegistradorCivilForm(forms.ModelForm):

    nombre = forms.CharField(
        label = _("Nombres"),
        max_length = 100,
        widget = forms.TextInput(
            attrs = {
                'class':'form-control input-sm', 'data-toggle':'tooltip', 'style':'width:250px;',
                'title':_("indique los Nombres"),
            }
        )
    )

    apellido = forms.CharField(
        label = _("Apellidos"),
        max_length = 100,
        widget = forms.TextInput(
            attrs = {
                'class':'form-control input-sm', 'data-toggle':'tooltip', 'style':'width:250px;',
                'title':_("indique los Apellidos"),
            }
        )
    )

    cedula = CedulaField()

    resolucion = forms.CharField(
        label = _("Resolución"),
        max_length = 100,
        widget = forms.TextInput(
            attrs = {
                'class':'form-control input-sm', 'data-toggle':'tooltip', 'style':'width:250px;',
                'title':_("indique la Resolución"),
            }
        )
    )

    fecha_resolucion = forms.CharField(
        label = _("Fecha de Resolución"),
        widget = forms.TextInput(
            attrs = {
                'class':'form-control input-sm', 'data-toggle':'tooltip', 'style':'width:250px;',
                'title':_("indique la fecha de la Resolución"),
            }
        )
    )

    gaceta = forms.CharField(
        label = _("Gaceta"),
        max_length = 100,
        widget = forms.TextInput(
            attrs = {
                'class':'form-control input-sm', 'data-toggle':'tooltip', 'style':'width:250px;',
                'title':_("indique la Gaceta"),
            }
        )
    )

    tipo_gaceta = forms.ChoiceField(
        label = _("Tipo de la Gaceta"),
        choices=(('',_('Seleccione...')),)+TIPO_GACETA,
        widget = forms.Select(
            attrs = {
                'class':'form-control select2', 'data-toggle':'tooltip', 'style':'width:250px;',
                'title':_("Seleccione el Tipo de la Gaceta"),
            }
        )
    )

    fecha_gaceta = forms.CharField(
        label = _("Fecha de la Gaceta"),
        widget = forms.TextInput(
            attrs = {
                'class':'form-control input-sm', 'data-toggle':'tooltip', 'style':'width:250px;',
                'title':_("indique la Fecha de la Gaceta"),
            }
        )
    )

    class Meta:
        model = RegistradorCivil
        exclude = [
            'persona',
        ]

class FallecidoForm(forms.ModelForm):

    nombre = forms.CharField(
        label = _("Nombres"),
        max_length = 100,
        widget = forms.TextInput(
            attrs = {
                'class':'form-control input-sm', 'data-toggle':'tooltip', 'style':'width:250px;',
                'title':_("indique los Nombres"),
            }
        )
    )

    apellido = forms.CharField(
        label = _("Apellidos"),
        max_length = 100,
        widget = forms.TextInput(
            attrs = {
                'class':'form-control input-sm', 'data-toggle':'tooltip', 'style':'width:250px;',
                'title':_("indique los Apellidos"),
            }
        )
    )

    cedula = CedulaField()

    fecha_nacimiento = forms.CharField(
        label = _("Fecha de Nacimiento"),
        widget = forms.TextInput(
            attrs = {
                'class':'form-control input-sm', 'data-toggle':'tooltip', 'style':'width:250px;',
                'title':_("indique la fecha de Nacimiento"),
            }
        )
    )

    sexo = forms.ChoiceField(
        label = _("Sexo"),
        choices=(('',_('Seleccione...')),)+SEXO,
        widget = forms.Select(
            attrs = {
                'class':'form-control select2', 'data-toggle':'tooltip', 'style':'width:250px;',
                'title':_("Seleccione el Sexo"),
            }
        )
    )

    edad = forms.CharField(
        label = _("Edad"),
        max_length = 100,
        widget = forms.NumberInput(
            attrs = {
                'class':'form-control input-sm', 'data-toggle':'tooltip', 'style':'width:250px;',
                'title':_("indique la Edad"),
            }
        )
    )

    estado_civil = forms.ChoiceField(
        label = _("Estado Civil"),
        choices=(('',_('Seleccione...')),)+ESTADO_CIVIL,
        widget = forms.Select(
            attrs = {
                'class':'form-control select2', 'data-toggle':'tooltip', 'style':'width:250px;',
                'title':_("Seleccione el Estado Civil"),
            }
        )
    )

    profesion = forms.CharField(
        label = _("Profesión"),
        widget = forms.TextInput(
            attrs = {
                'class':'form-control input-sm', 'data-toggle':'tooltip', 'style':'width:250px;',
                'title':_("indique la Profesión"),
            }
        )
    )

    ocupacion = forms.CharField(
        label = _("Ocupación"),
        widget = forms.TextInput(
            attrs = {
                'class':'form-control input-sm', 'data-toggle':'tooltip', 'style':'width:250px;',
                'title':_("indique la Ocupación"),
            }
        )
    )

    direccion = forms.CharField(
        label = _("Dirección"),
        widget = forms.TextInput(
            attrs = {
                'class':'form-control input-sm', 'data-toggle':'tooltip', 'style':'width:250px;',
                'title':_("indique la Dirección"),
            }
        )
    )

    ## Estado en el que se encuentra ubicado el municipio
    estado = forms.ModelChoiceField(
        label=_("Estado"), queryset=Estado.objects.all(), empty_label=_("Seleccione..."),
        widget=forms.Select(attrs={
            'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:250px;',
            'title': _("Seleccione el estado en donde se encuentra ubicada"),
            'onchange': "actualizar_combo(this.value,'base','Municipio','estado','pk','nombre','id_municipio')"
        })
    )

    ## Municipio en el que se encuentra ubicada la parroquia
    municipio = forms.ModelChoiceField(
        label=_("Municipio"), queryset=Municipio.objects.all(), empty_label=_("Seleccione..."),
        widget=forms.Select(attrs={
            'class': 'form-control select2', 'data-toggle': 'tooltip', 'disabled': 'true', 'style':'width:250px;',
            'title': _("Seleccione el municipio en donde se encuentra ubicada"),
            'onchange': "actualizar_combo(this.value,'base','Parroquia','municipio','pk','nombre','id_lugar_nacimiento')"
        }), required = False
    )

    ## Parroquia en donde se encuentra ubicada la dirección suministrada
    lugar_nacimiento = forms.ModelChoiceField(
        label=_("Lugar de Nacimiento"), queryset=Parroquia.objects.all(), empty_label=_("Seleccione..."),
        widget=forms.Select(attrs={
            'class': 'form-control select2', 'data-toggle': 'tooltip', 'disabled': 'true', 'style':'width:250px;',
            'title': _("Seleccione la parroquia en donde se encuentra ubicada"),
        }),
    )

    class Meta:
        model = Fallecido
        exclude = [
            'persona','lugar_nacimiento'
        ]

class DeclaranteForm(forms.ModelForm):

    nombre = forms.CharField(
        label = _("Nombres"),
        max_length = 100,
        widget = forms.TextInput(
            attrs = {
                'class':'form-control input-sm', 'data-toggle':'tooltip', 'style':'width:250px;',
                'title':_("indique los Nombres"),
            }
        )
    )

    apellido = forms.CharField(
        label = _("Apellidos"),
        max_length = 100,
        widget = forms.TextInput(
            attrs = {
                'class':'form-control input-sm', 'data-toggle':'tooltip', 'style':'width:250px;',
                'title':_("indique los Apellidos"),
            }
        )
    )

    cedula = CedulaField()

    edad = forms.CharField(
        label = _("Edad"),
        max_length = 100,
        widget = forms.NumberInput(
            attrs = {
                'class':'form-control input-sm', 'data-toggle':'tooltip', 'style':'width:250px;',
                'title':_("indique la Edad"),
            }
        )
    )

    profesion = forms.CharField(
        label = _("Profesión"),
        widget = forms.TextInput(
            attrs = {
                'class':'form-control input-sm', 'data-toggle':'tooltip', 'style':'width:250px;',
                'title':_("indique la Profesión"),
            }
        )
    )

    ocupacion = forms.CharField(
        label = _("Ocupación"),
        widget = forms.TextInput(
            attrs = {
                'class':'form-control input-sm', 'data-toggle':'tooltip', 'style':'width:250px;',
                'title':_("indique la Ocupación"),
            }
        )
    )

    direccion = forms.CharField(
        label = _("Dirección"),
        widget = forms.TextInput(
            attrs = {
                'class':'form-control input-sm', 'data-toggle':'tooltip', 'style':'width:250px;',
                'title':_("indique la Dirección"),
            }
        )
    )

    class Meta:
        model = Declarante
        exclude = [
            'persona'
        ]

class DefuncionForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(DefuncionForm, self).__init__(*args, **kwargs)

        lista_au = [('','Selecione...')]
        for au in Autoridad.objects.all():
            lista_au.append( (au.id,au) )
        self.fields['autoridad'].choices = lista_au

    fecha_hora = forms.CharField(
        label = _("Fecha y Hora"),
        widget = forms.TextInput(
            attrs = {
                'class':'form-control input-sm', 'data-toggle':'tooltip', 'style':'width:250px;',
                'title':_("indique la Fecha y la Hora"),
            }
        )
    )

    causa = forms.CharField(
        label = _("Causa"),
        max_length = 200,
        widget = forms.TextInput(
            attrs = {
                'class':'form-control input-sm', 'data-toggle':'tooltip', 'style':'width:250px;',
                'title':_("indique la Causa"),
            }
        )
    )

    certificado_defuncion = forms.CharField(
        label = _("Certificado de Defunción"),
        widget = forms.TextInput(
            attrs = {
                'class':'form-control input-sm', 'data-toggle':'tooltip', 'style':'width:250px;',
                'title':_("indique El Certificado de Defunción"),
            }
        )
    )

    ## Estado en el que se encuentra ubicado el municipio
    estado = forms.ModelChoiceField(
        label=_("Estado"), queryset=Estado.objects.all(), empty_label=_("Seleccione..."),
        widget=forms.Select(attrs={
            'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:250px;',
            'title': _("Seleccione el estado en donde se encuentra ubicada"),
            'onchange': "actualizar_combo(this.value,'base','Municipio','estado','pk','nombre','id_municipio')"
        })
    )

    ## Municipio en el que se encuentra ubicada la parroquia
    municipio = forms.ModelChoiceField(
        label=_("Municipio"), queryset=Municipio.objects.all(), empty_label=_("Seleccione..."),
        widget=forms.Select(attrs={
            'class': 'form-control select2', 'data-toggle': 'tooltip', 'disabled': 'true', 'style':'width:250px;',
            'title': _("Seleccione el municipio en donde se encuentra ubicada"),
            'onchange': "actualizar_combo(this.value,'base','Parroquia','municipio','pk','nombre','id_lugar')"
        }), required = False
    )

    ## Parroquia en donde se encuentra ubicada la dirección suministrada
    lugar = forms.ModelChoiceField(
        label=_("Lugar de Nacimiento"), queryset=Parroquia.objects.all(), empty_label=_("Seleccione..."),
        widget=forms.Select(attrs={
            'class': 'form-control select2', 'data-toggle': 'tooltip', 'disabled': 'true', 'style':'width:250px;',
            'title': _("Seleccione la parroquia en donde se encuentra ubicada"),
        }),
    )

    direccion = forms.CharField(
        label = _("Dirección"),
        widget = forms.TextInput(
            attrs = {
                'class':'form-control input-sm', 'data-toggle':'tooltip', 'style':'width:250px;',
                'title':_("indique la Dirección"),
            }
        )
    )

    autoridad = forms.ChoiceField(
        label = _("Autoridad"),
        widget = forms.Select(
            attrs = {
                'class':'form-control select2', 'data-toggle':'tooltip', 'style':'width:250px;',
                'title':_("Seleccione la Autoridad"),
            }
        )
    )

    class Meta:
        model = Defuncion
        exclude = [
            'autoridad', 'lugar'
        ]

class AutoridadForm(forms.ModelForm):

    nombre = forms.CharField(
        label = _("Nombres"),
        max_length = 100,
        widget = forms.TextInput(
            attrs = {
                'class':'form-control input-sm', 'data-toggle':'tooltip', 'style':'width:250px;',
                'title':_("indique los Nombres"),
            }
        )
    )

    apellido = forms.CharField(
        label = _("Apellidos"),
        max_length = 100,
        widget = forms.TextInput(
            attrs = {
                'class':'form-control input-sm', 'data-toggle':'tooltip', 'style':'width:250px;',
                'title':_("indique los Apellidos"),
            }
        )
    )

    cedula = CedulaField()


    numero_mpps = forms.CharField(
        label = _("Número MPPS"),
        widget = forms.TextInput(
            attrs = {
                'class':'form-control input-sm', 'data-toggle':'tooltip', 'style':'width:250px;',
                'title':_("indique el Número de MPPS"),
            }
        )
    )

    class Meta:
        model = Autoridad
        exclude = [
            'persona'
        ]
