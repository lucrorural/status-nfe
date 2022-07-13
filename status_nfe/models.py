from django.db import models
from django.utils import timezone


class StatusNfe(models.Model):
    autorizador = models.CharField(max_length=20, blank=True, null=True)
    autorizacao = models.CharField(max_length=20, blank=True, null=True)
    retorno_autorizacao = models.CharField(max_length=20, blank=True, null=True)
    inutilizacao = models.CharField(max_length=20, blank=True, null=True)
    consulta_protocolo = models.CharField(max_length=20, blank=True, null=True)
    status_servico = models.CharField(max_length=20, blank=True, null=True)
    tempo_medio = models.CharField(max_length=20, blank=True, null=True)
    consulta_cadastro = models.CharField(max_length=20, blank=True, null=True)
    recepcao_evento = models.CharField(max_length=20, blank=True, null=True)
    ultima_verificacao = models.DateTimeField(null=True, blank=True, default=timezone.now)

    def __str__(self):
        return f'{self.autorizador} - autorizacao={self.autorizacao} ultima={self.ultima_verificacao}'

    class Meta:
        managed = True
        db_table = 'statusnfe'
        verbose_name = 'statusnfe'
        verbose_name_plural = 'statusnfe'
