from celery import shared_task

from status_nfe.models import StatusNfe
from status_nfe.utils import DisponibilidadeNFe


@shared_task(name='task_status_portal_nfe')
def status_portal_nfe():
    disp_nfe = DisponibilidadeNFe()
    data = disp_nfe.get_status()
    print(data)

    for item in data:
        print(item)
        autorizador = item['autorizador']

        obj = StatusNfe.objects.filter(autorizador=autorizador)
        if obj.exists():
            print(f'update = {autorizador}')
            obj.update(**item)
        else:
            print(f'create = {autorizador}')
            obj.create(**item)
    return 'OK'
