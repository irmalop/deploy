from django_filters import rest_framework
from rest_framework import serializers
from employers.models import EmployerProfile
from employers.serializers import EmployerProfileSerializer
# from employers.models import EmployerVacancyRegistration
from employers.choices import state, modality, job_type

from arearol.serializers import AreaSerializer, RolSerializer

# from .models import ApplicantVacancyPostulation

# class AllVacanciesListSerializer(serializers.ModelSerializer):
#     company_name = serializers.StringRelatedField(source = 'employer_profile')
#     # job_type = serializers.ChoiceField(
#     #     required=True, allow_null=False, choices=job_type)
#     # modality = serializers.ChoiceField(
#     #     required=True, allow_null=False, choices=modality) 
    
#     class Meta:
#         model = EmployerVacancyRegistration 
#         fields = ['id','job_type','modality', 'job_description','requierements',
#         'video_explanation', 'salary','question_1', 'question_2', 'question_3', 
#         'state', 'municipality', 'area', 'rol', 'company_name']
#         # '__all__'
    #     depth = 1
    
    # def to_representation(self, instance):
    #     response = super().to_representation(instance)
    #     response['area'] = AreaSerializer(instance.area).data
    #     response['rol'] = RolSerializer(instance.rol).data
    #     return response       

class AllCompanyListSerializer(serializers.ModelSerializer):
    # company_name = serializers.StringRelatedField(source = 'employer_profile')

    
    class Meta:
        model = EmployerProfile
        fields = ['id', 'company_name']
        # '__all__'

# class CompanyFilter(rest_framework.FilterSet):
#     company_name = rest_framework.CharFilter(field_name='employer_profile__company_name', lookup_expr='exact')

#     class Meta:
#         # fields = ("company_name",)
#         fields = ['job_type','modality', 'area', 'rol', 'company_name']
#         depth = 1
#         model = EmployerVacancyRegistration
    

# class  PostulationVacancySerializer(serializers.ModelSerializer):
#     applicant= serializers.PrimaryKeyRelatedField(read_only=True,)
#     vacancy= serializers.PrimaryKeyRelatedField(read_only=True,)  

#     class Meta:
#         model = ApplicantVacancyPostulation
#         fields = ['id', 'vacancy', 'applicant', 'postulated_time', 'link_video']

# class  PostulationVacancySinVideoSerializer(serializers.ModelSerializer):
#     applicant= serializers.PrimaryKeyRelatedField(read_only=True,)  
#     vacancy= serializers.PrimaryKeyRelatedField(read_only=True,)  

#     class Meta:
#         model = ApplicantVacancyPostulation
#         fields = ['id', 'vacancy', 'applicant', 'postulated_time']

# class MyPostulationListSerializer(serializers.ModelSerializer):
#     company_name = serializers.StringRelatedField(source = 'employer_profile')
    
#     class Meta:
#         model = EmployerVacancyRegistration 
#         fields = ['id','area', 'rol', 'job_type', 'modality', 'salary', 'company_name']
#         depth = 1

#     def to_representation(self, instance):
#         response = super().to_representation(instance)
#         response['area'] = AreaSerializer(instance.area).data
#         response['rol'] = RolSerializer(instance.rol).data
#         return response
    
# class VacancyDetailSerializer(serializers.ModelSerializer):
#     company_name = serializers.StringRelatedField(source = 'employer_profile')
#     class Meta:
#         model = EmployerVacancyRegistration 
#         fields = ['id','job_type','modality', 'job_description','requierements',
#         'video_explanation', 'salary','question_1', 'question_2', 'question_3', 
#         'state', 'municipality', 'area', 'rol', 'company_name']
#         depth = 1
#     def to_representation(self, instance):
#         response = super().to_representation(instance)
#         response['area'] = AreaSerializer(instance.area).data
#         response['rol'] = RolSerializer(instance.rol).data
#         return response