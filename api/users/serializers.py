from asyncore import write
from logging import raiseExceptions
from rest_framework import serializers
from .models import User
from django.core.exceptions import ValidationError
from rest_framework.exceptions import AuthenticationFailed

from django.contrib import auth

from .models import FailedAttempt
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
    
special_characters = "[~\!@#\$%\^&\*\(\)_\+{}\":;'\[\]]"

def validate_password(password):

    if not any(char.isdigit() for char in password):
        raise ValidationError('Password must contain at least 1 digit.')
    if not any(char.isalpha() for char in password):
        raise ValidationError('Password must contain at least 1 letter.') 
    if not any(char in special_characters for char in password):
        raise ValidationError('Password must contain at least 1 special character.')
    if not any(char.isupper() for char in password):
        raise ValidationError('Password must contain at least 1 uppercase.')
    return password
class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(max_length=60, min_length=6, write_only=True, style={'input_type': 'password'})
    password2 = serializers.CharField(max_length=60, min_length=6, write_only=True, style={'input_type': 'password'})
    class Meta:
        model = User
        fields = ['email', 'password', 'password2'
        , 'is_applicant', 'is_employer'
        ]
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def save(self):
        user = User(
            email = self.validated_data['email'],
            is_applicant = self.validated_data['is_applicant'],
            is_employer = self.validated_data['is_employer'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'Password must match'})
        user.set_password(password)
        user.save()
        return user

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password')
        password = validate_password(password)
        return attrs
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class  EmailVerificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=555)

    class Meta:
        model = User
        fields = ['token']

class  LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length = 255, min_length = 3)
    password = serializers.CharField(max_length=20, min_length = 6, write_only = True, style={'input_type': 'password'})
    tokens_refresh = serializers.CharField(max_length=68, min_length = 6, read_only = True)
    tokens_access = serializers.CharField(max_length=68, min_length = 6, read_only = True)
    is_applicant = serializers.BooleanField(read_only = True)
    is_employer = serializers.BooleanField(read_only = True)
    class Meta:
        model = User
        fields = ['email', 'password', 'tokens_refresh', 'tokens_access', 'id','is_applicant', 'is_employer']

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')

        user = auth.authenticate(email=email, password=password)
        # import pdb
        # pdb.set_trace()


        if not user:

            raise AuthenticationFailed('Invalid credential, try again')
        if not user.is_active:
            raise AuthenticationFailed('Account disabled, contact admin')
        if not user.is_verified:
            raise AuthenticationFailed('Email is not verified')

        return {
            'email': user.email,
            'tokens_refresh': user.tokens_refresh(),
            'tokens_access': user.tokens_access(),
            'id': user.id,
            'is_applicant': user.is_applicant,
            'is_employer': user.is_employer
        }

    def monitor_login( auth_func ):
        """
        Function that replaces Django authentication() function with one that tracks failed logins and blocks further attempts based on a threshold
        """
        if hasattr( auth_func, '__PROTECT_FAILED_LOGINS__' ) :
        # avoiding multiple decorations
            return auth_func
    
        def decorate( *args, **kwargs ):
            """ Wrapper for Django authentication function """
            user = kwargs.get( 'email', '' )
            if not user:
                raise ValueError( 'username must be supplied by the \
                authentication function for FailedLoginBlocker to operate' )
                
            try:
                fa = FailedAttempt.objects.get( email=user )
                if fa.recent_failure( ):
                    if fa.too_many_failures( ):
                        # block the authentication attempt because
                        # of too many recent failures
                        fa.failures += 1
                        fa.save( )
                        raise ValidationError({'email': 'Your account has been locked due to too many failed login attempts.'})
                else:
                    # the block interval is over, reset the count
                    fa.failures = 0
                    fa.save( )
            except FailedAttempt.DoesNotExist:
                fa = None

            result = auth_func( *args, **kwargs )
            if result:
                # the authentication was successful
                return result
            # authentication failed 
            fa = fa or FailedAttempt( email=user, failures=0 )
            fa.failures += 1
            fa.save( )
            # return with unsuccessful auth
            return None

        decorate.__PROTECT_FAILED_LOGINS__ = True
        return decorate
    auth.authenticate = monitor_login( auth.authenticate )

class  ResendSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length = 255, min_length = 3)

    class Meta:
        model = User
        fields = ['email']

class ResetPasswordEmailRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length=2)
    class Meta:
        fields = ['email']

class SetNewPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(min_length=6, max_length=68, write_only=True)
    token = serializers.CharField(min_length=1, write_only=True)
    uidb64 = serializers.CharField(min_length=1, write_only=True)

    class Meta:
        fields = ['password', 'token', 'uidb64']
    # password = validate(password)
    def validate(self, attrs):
        password = attrs.get('password')
        password = validate_password(password)
        token = attrs.get('token')
        uidb64 = attrs.get('uidb64')

        id = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(id = id)

        if not PasswordResetTokenGenerator().check_token(user, token):
            raise AuthenticationFailed('The reset link is invalid', 401)
        user.set_password(password)
        user.save()
        return (user)

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(max_length=60, min_length=6, write_only=True, required=True)
    new_password1 = serializers.CharField(max_length=60, min_length=6, write_only=True, required=True)
    new_password2 = serializers.CharField(max_length=60, min_length=6, write_only=True, required=True)
    
    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({"old_password": "Old password is not correct"})
        return value

    def validate(self, attrs):
        new_password1 = attrs.get('new_password1')
        new_password2 = attrs.get('new_password2')
        if new_password1 != new_password2:
            raise serializers.ValidationError({'message': 'Password must match'})
        new_password1 = validate_password(new_password1)
        return attrs

    def save(self, **kwargs):
        password = self.validated_data['new_password1']
        user = self.context['request'].user
        user.set_password(password)
        user.save()
        return user