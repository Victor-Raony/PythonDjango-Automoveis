from django.conf.urls import url
from .views import *

urlpatterns = [
  url(r'^veiculo/listar/$', listar_veiculo, name='listar_veiculo'),

]