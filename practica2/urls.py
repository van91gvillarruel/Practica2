"""practica2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from rest_framework.routers import DefaultRouter

from competencia.views import CompetenciaViewSet
from jugador.views import JugadorViewSet
from team.views import TeamViewSet

router = DefaultRouter()
router.register(r'competencia', CompetenciaViewSet, base_name='competencias')
router.register(r'player', JugadorViewSet, base_name='player')
router.register(r'team', TeamViewSet, base_name='teams')
urlpatterns = router.urls
