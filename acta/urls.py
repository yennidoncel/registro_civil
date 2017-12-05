from django.conf.urls import url
from .views import ActaDefuncionList, ActaDefuncionCreate, RegistradorCivilCreate, FallecidoCreate, DeclaranteCreate, DefuncionCreate, AutoridadCreate
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^acta-defuncion/$', login_required(ActaDefuncionList.as_view()), name='acta_defuncion'),
    url(r'^acta-defuncion/registro/$', login_required(ActaDefuncionCreate.as_view()), name='acta_defuncion_registro'),
    url(r'^acta-defuncion/registrador-civil/$', login_required(RegistradorCivilCreate.as_view()), name='registrador_civil'),
    url(r'^acta-defuncion/fallecido/$', login_required(FallecidoCreate.as_view()), name='fallecido'),
    url(r'^acta-defuncion/declarante/$', login_required(DeclaranteCreate.as_view()), name='declarante'),
    url(r'^acta-defuncion/defuncion/$', login_required(DefuncionCreate.as_view()), name='defuncion'),
    url(r'^acta-defuncion/autoridad/$', login_required(AutoridadCreate.as_view()), name='autoridad'),
]
