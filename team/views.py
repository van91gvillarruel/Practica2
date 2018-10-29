from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
# Create your views here.
from .serializers import CreateTeamSerializer


class TeamViewSet(viewsets.ModelViewSet):

    def create(self, request):
        serializer = CreateTeamSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        resp = serializer.crear()
        return Response(resp)




