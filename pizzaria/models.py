from django.db import models
from django.urls import reverse

class Pizzaria(models.Model):

    STATUS = (
        (1, "Doing"),
        (2, "Done")
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    done = models.CharField(
        max_length=1,
        choices=STATUS,

    )
    

# A view abaixo é utilizada para listar os produtos de uma determinada categoria
# Este URLconf trata requisições para http://localhost:8000/computador/
# path('<slug:slug_da_categoria>/', views.lista_produtos, name='lista_produtos_por_categoria'),
# /computador/
# /celular/
# /eletrodomestico/

# from shop.models import Produto
# c = Categoria.objects.get(id=1)
# c.get_absolute_path()
# '/computador/'
