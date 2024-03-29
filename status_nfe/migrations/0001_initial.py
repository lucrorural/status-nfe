# Generated by Django 3.2.14 on 2022-07-13 18:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StatusNfe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autorizador', models.CharField(blank=True, max_length=20, null=True)),
                ('autorizacao', models.CharField(blank=True, max_length=20, null=True)),
                ('retorno_autorizacao', models.CharField(blank=True, max_length=20, null=True)),
                ('inutilizacao', models.CharField(blank=True, max_length=20, null=True)),
                ('consulta_protocolo', models.CharField(blank=True, max_length=20, null=True)),
                ('status_servico', models.CharField(blank=True, max_length=20, null=True)),
                ('tempo_medio', models.CharField(blank=True, max_length=20, null=True)),
                ('consulta_cadastro', models.CharField(blank=True, max_length=20, null=True)),
                ('recepcao_evento', models.CharField(blank=True, max_length=20, null=True)),
                ('ultima_verificacao', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
            ],
            options={
                'verbose_name': 'statusnfe',
                'verbose_name_plural': 'statusnfe',
                'db_table': 'statusnfe',
                'managed': True,
            },
        ),
    ]
