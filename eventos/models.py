from django.db import models
from django.contrib.auth.models import User

class Endereco(models.Model):
    logadouro = models.CharField(max_length=128)
    complemento = models.CharField(max_length=256, null=True)
    uf = models.CharField(max_length=2, null=True)
    cidade = models.CharField(max_length=64, null=True)
    cep = models.CharField(max_length=10)

    def __str__(self):
        return '{} - {}, {}'.format(self.logadouro, self.cidade, self.uf)


class Pessoa(models.Model):
    nome = models.CharField(max_length=128)
    descricao = models.TextField()
    data_nascimento = models.DateField(blank=True, null=True)
    endereco = models.ForeignKey(Endereco, related_name='pessoas', null=True, blank=False)
    usuario = models.OneToOneField(User)

    def __str__(self):
        return self.nome

class PessoaFisica(Pessoa):
    cpf = models.CharField(max_length=11, blank=False)
    mae = models.CharField(max_length=150, null=True, blank=False)
    pai = models.CharField(max_length=150, null=True, blank=False)

    def __str__(self):
        return '{} - {}'.format(self.nome, self.cpf)

class Evento(models.Model):
    nome = models.CharField(max_length=128)
    descricao = models.TextField()
    sigla = models.CharField(max_length=5,blank=False)
    numero = models.CharField(max_length=10, null=True, blank=False)
    ano = models.DateField(blank=False, null=True)
    realizador = models.ForeignKey(PessoaFisica, related_name='pessoasfisicas', null=True, blank=False)
    endereco = models.ForeignKey(Endereco, related_name='enderecos', null=True, blank=False)
    logo = models.CharField(max_length=1, null=True)
    data_de_inicio = models.DateField(blank=False, null=True)
    data_de_fim = models.DateField(blank=False, null=True)

    def __str__(self):
        return '{} - {}'.format(self.nome, self.sigla)

class Inscricao(models.Model):
    evento = models.ForeignKey(Evento, null=True, blank=False)
    pessoa = models.ForeignKey(PessoaFisica, null=True, blank=False)
    data = models.DateField(blank=False, null=True)
    preco = models.FloatField(max_length=10, null=True, blank=False)

    def __str__(self):
        return self.evento.nome