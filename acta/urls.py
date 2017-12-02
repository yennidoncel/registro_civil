from django.conf.urls import url
from .views import ActaDefuncionList, ActaDefuncionCreate
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^acta-defuncion/$', login_required(ActaDefuncionList.as_view()), name='acta_defuncion'),
    url(r'^acta-defuncion/registro/$', login_required(ActaDefuncionCreate.as_view()), name='acta_defuncion_registro'),
]
