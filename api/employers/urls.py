from django.urls import path

from .views import EmployerProfileView
# , EmployerVacancyRegistrationView, MyVacanciesListFiltersView
# EmployerVacancyRegistrationDetail, 

urlpatterns=[
    path('profile/', EmployerProfileView.as_view(), name = "employer-profile"),  
    # path('vacancy/registration/', EmployerVacancyRegistrationView.as_view(), name = "employer-vacancy-registration"),
    # # path('vacancy/registration/<int:pk>/', EmployerVacancyRegistrationDetail.as_view(), name = "employer-vacancy-registration-detail"),
    # path('my/vacancies/list/', MyVacanciesListFiltersView.as_view(), name = "my-vacancies-list"),
]      



 

