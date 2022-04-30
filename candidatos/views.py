from rest_framework import viewsets
from candidatos.models import Candidato
from django.shortcuts import render
from candidatos.serializers import CandidatosSerializer
import django_tables2 as tables

class CandidatosViewSet(viewsets.ModelViewSet):
    serializer_class = CandidatosSerializer
    queryset = Candidato.objects.all()


# this class will create the table just like how we create forms
class SimpleTable(tables.Table):
    
    class Meta:
        model = Candidato
      


# this will render table
class TableView(tables.SingleTableView):
   table_class = SimpleTable
   queryset = Candidato.objects.all()
   template_name = "tabela.html"