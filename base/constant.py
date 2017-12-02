from django.utils.translation import ugettext_lazy as _

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
