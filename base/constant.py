from django.utils.translation import ugettext_lazy as _

## Mensaje de error para peticiones AJAX
MSG_NOT_AJAX = _("No se puede procesar la petición. "
                 "Verifique que posea las opciones javascript habilitadas e intente nuevamente.")

SEXO = (
    ("M",_("Masculino")),
    ("F",_("Femenino")),
)

ESTADO_CIVIL = (
    ("SO",_("Soltero(a)")),
    ("CA",_("Casado(a)")),
    ("CO",_("Concubino(a)")),
    ("DI",_("Divirciado(a)")),
    ("VI",_("Viudo(a)")),
)

NACIONALIDAD = (
    ("V",_("Venezolano(a)")),
    ("E",_("Extranjero(a)")),
)

TIPO_GACETA = (
    ("M",_("Municipal")),
    ("O",_("Oficial")),
)
