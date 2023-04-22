from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from .serializers import ApplicantVideoSerializer, ApplicantProfileSerializer, AcademicDataSerializer, ApplicantJobInterestSerializer
from .models import ApplicantVideo, ApplicantProfile, AcademicData, ApplicantJobInterest
from users.models import User
from users.custum_permissions import IsApplicant
from arearol.models import Area, Rol  
from arearol.serializers import AreaSerializer, RolSerializer

class  ApplicantVideoView(APIView):
    permission_classes = (IsAuthenticated, IsApplicant, )

    def post(self, request):
        if not ApplicantVideo.objects.filter(user_id=request.user).exists():
            serializer = ApplicantVideoSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(user=request.user) # <---- INCLUDE REQUEST
            return Response(serializer.data, status=status.HTTP_201_CREATED)   
        else:
            return Response({'msg':'Already exists'}, status=status.HTTP_400_BAD_REQUEST)  

    def get(self, request):
        user = get_object_or_404(ApplicantVideo,user=request.user)
        serializer = ApplicantVideoSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        serializer = ApplicantVideoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        video = serializer.data["video"]
        user_id = request.user.id   
        presentation = ApplicantVideo.objects.get(user_id=user_id)
        if presentation.video != video:
            presentation.video = video
            presentation.save()
            return Response({'msg': 'Updated succesfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'msg': 'The link is the same'}, status=status.HTTP_400_BAD_REQUEST)

class ApplicantProfileView(APIView):
    permission_classes = (IsAuthenticated, IsApplicant)
    
    def post(self,request):
        if not ApplicantProfile.objects.filter(user_id=request.user).exists():
            serializer = ApplicantProfileSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(user=request.user) # <---- INCLUDE REQUEST
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'msg':'Already exists'})    

    def get(self, request):
        user = get_object_or_404(ApplicantProfile, user=request.user)
        serializer = ApplicantProfileSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # def put(self, request):
    #     serializer = ApplicantProfileSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     profile = serializer.data["perofile"]
    #     user_id = request.user.id   
    #     applicant = ApplicantProfile.objects.get(user_id=user_id)
    #     if  applicant.profile != profile:
    #         applicant.profile = profile
    #         applicant.save()
    #         return Response({'msg': 'Updated succesfully'}, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response({'msg':'Some field is not valid'}, status=status.HTTP_400_BAD_REQUEST)


class AcademicList(APIView):
    permission_classes = (IsAuthenticated, IsApplicant)

    def post(self,request):
        serializer = AcademicDataSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user) # <---- INCLUDE REQUEST
        return Response(serializer.data, status=status.HTTP_201_CREATED)   
        
    def get(self, request):
        academic_list = AcademicData.objects.filter(user_id=request.user)
        serializer = AcademicDataSerializer(academic_list, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AcademicDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AcademicData.objects.all()
    serializer_class = AcademicDataSerializer
    permission_classes = (IsAuthenticated, IsApplicant)
    
    
class ApplicantJobInterestView(APIView):
    permission_classes = (IsAuthenticated, IsApplicant)
    queryset = ApplicantJobInterest.objects.all()
    serializer_class=ApplicantJobInterestSerializer

    def post(self,request): 
        if not ApplicantJobInterest.objects.filter(user_id=request.user).exists():
            serializer = ApplicantJobInterestSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(user=request.user) # <---- INCLUDE REQUEST
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'msg':'Already exists'})     
              
    def get(self, request):
        user = get_object_or_404(ApplicantJobInterest, user=request.user)
        serializer = ApplicantJobInterestSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # def put(self, request):
    #     serializer = ApplicantJobInterestSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     jobinterest = serializer.data["job_interest"]
    #     user_id = request.user.id   
    #     applicantjobinterest = ApplicantJobInterest.objects.get(user_id=user_id)
    #     if  applicantjobinterest.jobinterest != jobinterest:
    #         applicantjobinterest.jobinterest = jobinterest
    #         applicantjobinterest.save()
    #         return Response({'msg': 'Updated succesfully'}, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response({'msg':'Some field is not valid'}, status=status.HTTP_400_BAD_REQUEST)     
