from django.contrib import admin
from eventos.models import *
# Register your models here.
admin.site.register(Pessoa)
admin.site.register(Endereco)
admin.site.register(PessoaFisica)
admin.site.register(Evento)
admin.site.register(Inscricao)