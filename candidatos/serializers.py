from .models import Candidato
from rest_framework import serializers


class CandidatosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidato
        exclude = []