from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend 
from django_filters import rest_framework as filters
from rest_framework import filters
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from employers.models import EmployerProfile
from users.custum_permissions import IsApplicant
# from employers.models import EmployerVacancyRegistration
from applicants.models import ApplicantProfile
# from .models import ApplicantVacancyPostulation
from .serializers import AllCompanyListSerializer
#  AllVacanciesListSerializer, CompanyFilter 
# from .serializers import PostulationVacancySerializer, PostulationVacancySinVideoSerializer
# from .serializers import MyPostulationListSerializer, VacancyDetailSerializer
from rest_framework.views import APIView
# Create your views here.
class AllCompanyView(APIView):
    #permission_classes = (IsAuthenticated, IsEmployer, IsApplicant)       
    def get(self,request):
        company_list = EmployerProfile.objects.all()
        serializer = AllCompanyListSerializer(company_list, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# class AllVacanciesListView(generics.ListCreateAPIView):
#     #permission_classes = (IsAuthenticated, IsEmployer, IsApplicant)        
#     permission_classes = (IsAuthenticated,)        
#     queryset = EmployerVacancyRegistration.objects.all()
#     serializer_class=AllVacanciesListSerializer
#     filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['area', 'rol', 'job_type', 'modality']
    # ordering_fields = ['area', 'rol', 'job_type', 'modality', 'company_name']
    # filterset_class = CompanyFilter

    # def get_queryset(self):
    #     return EmployerVacancyRegistration.objects.all().select_related('employer_profile')             
    # # def filter(self, request):
    #     user = get_object_or_404(EmployerVacancyRegistration, user=request.user)
    #     serializer = EmployerVacancyRegistrationSerializer(user)
    #     return Response(serializer.data, status=status.HTTP_200_OK)    


# class  PostulationVacancyView(generics.ListCreateAPIView):
#     permission_classes = (IsAuthenticated, IsApplicant)
#     queryset=ApplicantVacancyPostulation.objects.all()
#     lookup_fields = 'vacancy_id'
#     lookup_url_kwarg = 'vacancy_id'

#     def get_queryset(self):
#         vacancy = self.lookup_url_kwarg['vacancy_id']
#         return ApplicantVacancyPostulation.objects.filter(vacancy=vacancy)

#     def get_serializer_class(self):
#         vacancy = EmployerVacancyRegistration.objects.filter(id = self.kwargs['vacancy_id'])
#         if vacancy.filter(question_1=''):
#             # print('hola')
#             return PostulationVacancySinVideoSerializer
#         # print('hola de nuevo')
#         return PostulationVacancySerializer
        
#     def post(self, request, *args, **kwargs):
#         vacancy = EmployerVacancyRegistration.objects.get(id = self.kwargs['vacancy_id'])
#         if not ApplicantProfile.objects.filter(user_id=request.user).exists():
#             return Response({'message': 'Por favor, primero captura tus datos personales'}, 
#             status = status.HTTP_400_BAD_REQUEST)  
#         applicant = ApplicantProfile.objects.get(user=request.user)
#         if not ApplicantVacancyPostulation.objects.filter(applicant_id=applicant, vacancy_id=vacancy).exists():
#             serializer = self.get_serializer(data=request.data)
#             serializer.is_valid(raise_exception=True)
#             serializer.save(vacancy = vacancy, applicant=applicant) # <---- INCLUDE REQUEST
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response({'msg':'You already postulated'}, status=status.HTTP_400_BAD_REQUEST)   
   
#     def get(self, request, *args, **kwargs):
#         vacancy = EmployerVacancyRegistration.objects.get(id = self.kwargs['vacancy_id'])
#         applicant = ApplicantProfile.objects.get(user=request.user)
#         postulation = get_object_or_404(ApplicantVacancyPostulation, applicant_id=applicant, vacancy_id=vacancy)
#         serializer = self.get_serializer(postulation)
#         return Response(serializer.data, status=status.HTTP_200_OK)  

# class MyPostulationListView(generics.ListCreateAPIView):
#     permission_classes = (IsAuthenticated, IsApplicant)
#     serializer_class = MyPostulationListSerializer
#     def get_queryset(self):
#         applicant = ApplicantProfile.objects.get(user=self.request.user)
#         vacancy = ApplicantVacancyPostulation.objects.filter(applicant_id=applicant).values_list('vacancy_id', flat=True)
#         ids = list(vacancy)
#         # print(ids)
#         return EmployerVacancyRegistration.objects.filter(id__in=ids).select_related('employer_profile')  

# class VacancyDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = EmployerVacancyRegistration.objects.all()
#     serializer_class = VacancyDetailSerializer
#     permission_classes = (IsAuthenticated, )  