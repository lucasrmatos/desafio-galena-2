from django.urls import URLPattern, path, include
from rest_framework.routers import DefaultRouter
from .views import CandidatosViewSet

router = DefaultRouter()
router.register(r'', CandidatosViewSet, basename='Base de Candidatos.')

candidatos_urls = router.urls
