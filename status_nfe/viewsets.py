from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ReadOnlyModelViewSet

from status_nfe.serializers import StatusNfeSerializer
from status_nfe.models import StatusNfe


webservice = {
    'AM': 'AM',
    'BA': 'BA',
    'GO': 'GO',
    'MG': 'MG',
    'MS': 'MS',
    'MT': 'MT',
    'PE': 'PE',
    'PR': 'PR',
    'RS': 'RS',
    'SP': 'SP',
    'MA': 'SVAN',
    'AC': 'SVRS',
    'AL': 'SVRS',
    'AP': 'SVRS',
    'CE': 'SVRS',
    'DF': 'SVRS',
    'ES': 'SVRS',
    'PA': 'SVRS',
    'PB': 'SVRS',
    'PI': 'SVRS',
    'RJ': 'SVRS',
    'RN': 'SVRS',
    'RO': 'SVRS',
    'RR': 'SVRS',
    'SC': 'SVRS',
    'SE': 'SVRS',
    'TO': 'SVRS',
}

CACHE_TIME = 60 * 10  # 10 minutes

@method_decorator(cache_page(CACHE_TIME), name='dispatch')
class StatusNfeViewSet(ReadOnlyModelViewSet):
    serializer_class = StatusNfeSerializer
    queryset = StatusNfe.objects.all().order_by('autorizador')
    permission_classes = ()
    pagination_class = None
    filter_backends = (SearchFilter, OrderingFilter,)
    filterset_fields = '__all__'
    ordering_fields = '__all__'

    def get_queryset(self):
        qs = self.queryset
        uf = self.request.query_params.get('uf', None)
        if uf:
            if uf.upper() not in webservice.keys():
                return qs
            return qs.filter(autorizador=webservice[uf.upper()])
        return qs