from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.permissions import IsAuthenticated
from users.custum_permissions import IsEmployer

from .models import EmployerProfile
# , EmployerVacancyRegistration
from .serializers import EmployerProfileSerializer
# , EmployerVacancyRegistrationSerializer, MyVacanciesListFiltersSerializer

class EmployerProfileView(APIView):
    permission_classes = (IsAuthenticated, IsEmployer)
   
    def post(self,request):     
        if not EmployerProfile.objects.filter(user_id=request.user).exists():
            serializer = EmployerProfileSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(user=request.user) # <---- INCLUDE REQUEST
            return Response(serializer.data, status=status.HTTP_201_CREATED)   
        else:
            return Response({'msg':'Already exists'})

    def get(self, request):
        user = get_object_or_404(EmployerProfile, user=request.user)
        profile_serializer = EmployerProfileSerializer(user)
        return Response(profile_serializer.data, status=status.HTTP_200_OK)
   

# class EmployerVacancyRegistrationView(APIView):
#     permission_classes = (IsAuthenticated, IsEmployer)
   
#     def post(self,request):
#         if not EmployerProfile.objects.filter(user_id=request.user).exists():
#             return Response({'message': 'Por favor, primero captura el perfil de tu empresa'}, 
#             status = status.HTTP_400_BAD_REQUEST)   
#         serializer = EmployerVacancyRegistrationSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         empleador = EmployerProfile.objects.get(user=self.request.user)
#         serializer.save(employer_profile=empleador) # <---- INCLUDE REQUEST
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
   
#     def get(self, request):
#         if not EmployerProfile.objects.filter(user_id=request.user).exists():
#             return Response({'message': 'Por favor, primero captura el perfil de tu empresa'}, 
#             status = status.HTTP_400_BAD_REQUEST)  
#         empleador = EmployerProfile.objects.get(user=self.request.user)
#         vacancy_list = EmployerVacancyRegistration.objects.filter(employer_profile=empleador)
#         serializer = EmployerVacancyRegistrationSerializer(vacancy_list, many=True)
#         return Response(serializer.data, status = status.HTTP_200_OK)      
           
        
# class EmployerVacancyRegistrationDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = EmployerVacancyRegistration.objects.all()
#     serializer_class = EmployerVacancyRegistrationSerializer
#     permission_classes = (IsAuthenticated, )        


# class  MyVacanciesListFiltersView(generics.ListAPIView):
#     serializer_class = MyVacanciesListFiltersSerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['area', 'rol', 'job_type', 'modality']
#     permission_classes = (IsAuthenticated, IsEmployer)
#     # queryset = EmployerVacancyRegistration.objects.all()

#     def get_queryset(self): 
#         if not EmployerProfile.objects.filter(user_id=self.request.user).exists():
#             return Response({'message': 'Por favor, primero captura el perfil de tu empresa'}, 
#             status = status.HTTP_400_BAD_REQUEST)
#         empleador = EmployerProfile.objects.get(user=self.request.user)
#         return EmployerVacancyRegistration.objects.filter(employer_profile=empleador)
           

