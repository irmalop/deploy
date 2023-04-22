from rest_framework import serializers
from .models import EmployerProfile
# ,EmployerVacancyRegistration
from .choices import state, modality, job_type
from arearol.serializers import AreaSerializer, RolSerializer


class EmployerProfileSerializer(serializers.ModelSerializer):
    user= serializers.PrimaryKeyRelatedField(read_only=True,)
    logo = serializers.ImageField(required=False, allow_null=False)
    
    class Meta:
        model = EmployerProfile
        fields = '__all__'

                         
# class EmployerVacancyRegistrationSerializer(serializers.ModelSerializer):
#     employer_profile= serializers.PrimaryKeyRelatedField(read_only=True,)
#     job_type = serializers.ChoiceField(required=True, allow_null=False, choices=job_type)
#     modality = serializers.ChoiceField(required=True, allow_null=False, choices=modality)
#     state = serializers.ChoiceField(required=True, allow_null=False, choices=state)
#     salary = serializers.CharField(required=True, allow_blank=True)
#     question_1 = serializers.CharField(required=True, allow_blank=True)
#     question_2 = serializers.CharField(required=True, allow_blank=True)
#     question_3 = serializers.CharField(required=True, allow_blank=True)

#     class Meta:
#         model = EmployerVacancyRegistration 
#         # fields = '__all__'
#         exclude = ('applicants',)
    
#     def to_representation(self, instance):
#         response = super().to_representation(instance)
#         response['area'] = AreaSerializer(instance.area).data
#         response['rol'] = RolSerializer(instance.rol).data
        
#         return response
     
# class MyVacanciesListFiltersSerializer(serializers.ModelSerializer):
#     employer_profile = serializers.CharField(source='employer_profile.company') 

#     class Meta:
#         model = EmployerVacancyRegistration 
#         # fields = '__all__'
#         exclude = ('applicants',)
    
#     def to_representation(self, instance):
#         response = super().to_representation(instance)
#         response['area'] = AreaSerializer(instance.area).data
#         response['rol'] = RolSerializer(instance.rol).data
        
#         return response
    
    
         
