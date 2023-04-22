from django.urls import path
from .views import ApplicantVideoView, ApplicantProfileView, ApplicantJobInterestView 
from .views import AcademicList, AcademicDetail  
# from postulations.views import PostulationVacancyView, MyPostulationListView

urlpatterns=[
    path('presentation/', ApplicantVideoView.as_view(), name = "applicant-video"),
    path('profile/', ApplicantProfileView.as_view(), name = "applicant-profile"),    
    path('academic/', AcademicList.as_view(), name = "applicant-academic"),
    path('academic/<int:pk>/', AcademicDetail.as_view(), name = "applicant-academic-detail"),
    path('jobinterest/', ApplicantJobInterestView.as_view(), name = "applicant-jobinterest"),
    # path('postulation/vacancy/<int:vacancy_id>/', PostulationVacancyView.as_view(), name = "postulation-vacancy"),
    # path('my/postulations/', MyPostulationListView.as_view(), name = "my-postulation"),
]
