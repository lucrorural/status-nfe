from celery import shared_task
from django.core.cache import cache

from status_nfe.models import StatusNfe
from status_nfe.utils import DisponibilidadeNFe


@shared_task(name='task_status_portal_nfe')
def status_portal_nfe():
    disp_nfe = DisponibilidadeNFe()
    data = disp_nfe.get_status()

    for item in data:
        autorizador = item['autorizador']
        ultima_verificacao = item['ultima_verificacao']

        obj = StatusNfe.objects.filter(autorizador=autorizador)
        if obj.exists():
            obj.update(**item)
        else:
            obj.create(**item)

        print(f'update {autorizador} {ultima_verificacao}')

    cache.clear()
    return 'OK'
