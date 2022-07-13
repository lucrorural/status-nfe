from rest_framework import routers
from status_nfe.viewsets import StatusNfeViewSet


router = routers.DefaultRouter()

router.register('statusnfe', StatusNfeViewSet, basename='statusnfe')

urlpatterns = router.urls
