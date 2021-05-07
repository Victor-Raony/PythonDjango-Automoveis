from django.core import paginator
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from .models import *

# Create your views here.

def listar_veiculo(request, template_name="veiculo_list.html"):
    query = request.GET.get("busca", '')
    page = request.GET.get('page', '')
    ordenar = request.GET.get("ordenar", '')
    if query:
        veiculo = Veiculo.objects.filter(modelo__icontains=query)
    else:
        try:
            if ordenar:
                veiculo = Veiculo.objects.all().order_by(ordenar)
            else:
                veiculo = Veiculo.objects.all()
            veiculo = Paginator(veiculo, 2)
            veiculo = veiculo.page(page)
        except PageNotAnInteger:
            veiculo = veiculo.page(1)
        except EmptyPage:
            veiculo = paginator.page(paginator.num_pages)
    veiculos = {'lista': veiculo}
    return render(request, template_name, veiculos)