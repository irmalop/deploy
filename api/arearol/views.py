from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from .serializers import AreaSerializer, RolSerializer
from .models import Area, Rol
from users.models import User
from users.custum_permissions import IsEmployer, IsApplicant

# Create your views here.

class Area(generics.ListCreateAPIView):
    queryset = Area.objects.all() 
    serializer_class = AreaSerializer
    #permission_classes = (IsAuthenticated, IsEmployer, IsApplicant)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class RetrieveRolById(APIView):
    #permission_classes = (IsAuthenticated, IsEmployer, IsApplicant)       
    def get(self,request, area_id):
        rol_list = Rol.objects.filter(area_id=area_id)
        serializer = RolSerializer(rol_list, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

