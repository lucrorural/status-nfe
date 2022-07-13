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
            return qs.filter(autorizador=webservice[uf])
        return qs