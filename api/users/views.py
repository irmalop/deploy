from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.generics import UpdateAPIView
from .serializers import RegisterSerializer, EmailVerificationSerializer, LoginSerializer, ResendSerializer, ResetPasswordEmailRequestSerializer, SetNewPasswordSerializer, ChangePasswordSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .utils import Util
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
import jwt
from django.conf import settings
from django.shortcuts import redirect, render
from django.http import HttpResponsePermanentRedirect
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.shortcuts import redirect
from decouple import config

# Create your views here.
class RegisterView(generics.GenericAPIView):
    serializer_class=RegisterSerializer
    def post(self,request):
        user=request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data=serializer.data
        
        user = User.objects.get(email=user_data['email'])

        token = RefreshToken.for_user(user).access_token

        current_site = get_current_site(request).domain
        relativeLink = reverse('email-verify')

        absurl='http://'+ current_site + relativeLink + "?token="+ str(token)
        email_body = 'Hi ' + user.email + ' Use link below to verify your email \n' + absurl
        data = {'email_body': email_body, 'to_email': user.email,'email_subject': 'Verify your email'}

        Util.send_email(data)
        return Response(user_data, status=status.HTTP_201_CREATED)

class  VerifyEmail(generics.GenericAPIView):
    def get(self, request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(token,settings.SECRET_KEY)
            user = User.objects.get(id = payload['user_id'])
            if not user.is_verified:
                user.is_verified = True
                user.save()
            return redirect(config('FRONTEND_LOGIN_URL', '')+'?token_valid=True&email=Successfully activated')
        except jwt.ExpiredSignatureError as identifier:
            return redirect(config('FRONTEND_LOGIN_URL', '')+'?token_valid=False&error=Activation Expired')
        except jwt.exceptions.DecodeError as identifier:
            return redirect(config('FRONTEND_LOGIN_URL', '')+'?token_valid=False&error=Invalid token')

class  LoginAPIView(generics.GenericAPIView):
    serializer_class= LoginSerializer
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status = status.HTTP_200_OK)
class ResendVerifyEmail(generics.GenericAPIView):
    serializer_class = ResendSerializer
    def post(self, request):
        data = request.data
        # email = data.get('email')
        email = data['email']
        try:
            user = User.objects.get(email=email)
       
            if user.is_verified:
                return Response({'msg':'User is already verified'})
            token = RefreshToken.for_user(user).access_token
            current_site= get_current_site(request).domain
            relativeLink = reverse('email-verify')
            
            absurl = 'http://'+current_site+relativeLink+"?token="+str(token)
            email_body = 'Hi '+ user.email + ' this is the resent link to verify your email \n' + absurl

            data = {'email_body':email_body,'to_email':user.email,
                    'email_subject':'Verify your email'}
            Util.send_email(data)
            return Response({'msg':'The verification email has been sent'}, status=status.HTTP_201_CREATED)
        except User.DoesNotExist:
            return Response({'msg':'No such user, register first'})
class RequestPasswordResetEmail(generics.GenericAPIView):
    serializer_class = ResetPasswordEmailRequestSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        email = request.data['email']
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uidb64=urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            current_site= get_current_site(
                request=request).domain
            relativeLink = reverse(
                'password-reset-confirm', kwargs={'uidb64':uidb64, 'token': token})
            # redirect_url = request.data.get('redirect_url', '')
            redirect_url = config('FRONTEND_PASSWORD_URL', '')
            absurl = 'http://'+current_site+relativeLink
            email_body = 'Hello, \n  Use link below to reset your password \n' + \
                absurl + "?redirect_url="+redirect_url
            data = {'email_body':email_body,'to_email':user.email,
                'email_subject':'Reset your password'}
            Util.send_email(data)
        return Response({'success': 'We have sent you a link to reset your password'}, status=status.HTTP_200_OK)


class CustomRedirect(HttpResponsePermanentRedirect):
    allowed_schemes = [config('APP_SCHEME', ''),'http', 'https']

class PasswordTokenCheckAPI(generics.GenericAPIView):
    serializer_class = SetNewPasswordSerializer
    
    def get(self, request, uidb64, token):
        # redirect_url = request.GET.get('redirect_url')
        redirect_url = config('FRONTEND_PASSWORD_URL', '')

        try:
            id=smart_str(urlsafe_base64_decode(uidb64))
            user=User.objects.get(id=id)
            if not PasswordResetTokenGenerator().check_token(user, token):
                if len(redirect_url) > 3:
                    return CustomRedirect(redirect_url+'?token_valid=False')
                # return Response({'error': 'Token is not valid, please request a new one'})
                else:
                    return CustomRedirect(config('FRONTEND_PASSWORD_URL', '')+'?token_valid=False')
            if redirect_url and len(redirect_url) > 3:
                return CustomRedirect(redirect_url+'?token_valid=True&message=Credencials Valid&uidb64='+uidb64+'&token='+token)
            else:
                return CustomRedirect(config('FRONTEND_PASSWORD_URL', '')+'?token_valid=False')
            
        except DjangoUnicodeDecodeError as identifier:
            try:
                if not PasswordResetTokenGenerator().check_token(user):
                    return CustomRedirect(redirect_url+'?token_valid=False')
            except UnboundLocalError as e:
                return Response({'error': 'Token is not valid, please request a new one'}, status=status.HTTP_400_BAD_REQUEST)
class SetNewPasswordAPIView(generics.GenericAPIView):
    serializer_class = SetNewPasswordSerializer

    def patch(self, request):
        serializer = self.serializer_class(data=request.data)

        serializer.is_valid(raise_exception=True)
        return Response({'success': True, 'message': 'Password reset success'}, status=status.HTTP_200_OK)
    
class ChangePasswordView(UpdateAPIView):
    serializer_class = ChangePasswordSerializer

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({'msg': 'Contraseña actualizada'}, status=status.HTTP_200_OK)
