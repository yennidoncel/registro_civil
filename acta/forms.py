from django import forms
from django.utils.translation import ugettext_lazy as _
from base.fields import CedulaField
from .models import ActaDefuncion, RegistradorCivil

class ActaDefuncionForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ActaDefuncionForm, self).__init__(*args, **kwargs)

        lista_rc = [('','Selecione...')]
        for rc in RegistradorCivil.objects.all():
            lista_rc.append( (rc.id,rc) )
        self.fields['registrador_civil'].choices = lista_rc

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

    class Meta:
        model = ActaDefuncion
        exclude = [
            'registrador_civil','fallecido',
        ]
