from rest_framework import serializers
from django.core.validators import MaxValueValidator, MinValueValidator

from users.models import User
from .models import ApplicantVideo, ApplicantProfile, AcademicData, ApplicantJobInterest

from .choices import LEVEL, STATUS, sex, marital_status, state, modality, job_type

from arearol.models import Area, Rol
from arearol.serializers import AreaSerializer, RolSerializer

class ApplicantVideoSerializer(serializers.ModelSerializer):
    user= serializers.PrimaryKeyRelatedField(read_only=True,)  

    class Meta:
        model = ApplicantVideo
        fields = '__all__'

    
class ApplicantProfileSerializer(serializers.ModelSerializer):
    user= serializers.PrimaryKeyRelatedField(read_only=True,)
    sex = serializers.ChoiceField(
        required=True, allow_null=False, choices=sex)
    marital_status = serializers.ChoiceField(
        required=True, allow_null=False, choices=marital_status)
    email = serializers.EmailField(
        allow_blank=True)
    state = serializers.ChoiceField(
        required=True, allow_null=False, choices=state)

    class Meta:
        model = ApplicantProfile
        fields = '__all__'


class AcademicDataSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')
    level = serializers.ChoiceField(required=True, allow_null=False, choices=LEVEL)
    status = serializers.ChoiceField(required=True, allow_null=False, choices=STATUS)
    class Meta:
        model = AcademicData
        fields = '__all__'
        
     
class ApplicantJobInterestSerializer(serializers.ModelSerializer):
    user= serializers.PrimaryKeyRelatedField(read_only=True,)
    modality = serializers.ChoiceField(
        required=True, allow_null=False, choices=modality)
    job_type = serializers.ChoiceField(
        required=True, allow_null=False, choices=job_type)
   
    class Meta:
        model = ApplicantJobInterest
        fields = '__all__'
        
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['area'] = AreaSerializer(instance.area).data
        response['rol'] = RolSerializer(instance.rol).data
        return response 
