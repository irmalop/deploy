from rest_framework import serializers
from .models import Area, Rol
from users.models import User

class AreaSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        required=True, allow_null=False)
    
    class Meta:
        model = Area
        fields = '__all__'


class RolSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        required=True, allow_null=False)
    class Meta:
        model = Rol
        fields = '__all__'     
        