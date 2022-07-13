from rest_framework import serializers

from status_nfe.models import StatusNfe


class StatusNfeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusNfe
        fields = '__all__'
