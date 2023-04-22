from django.urls import path

from .views import AllCompanyView
# AllVacanciesListView, VacancyDetailView
# PostulationVacancyView, MyPostulationListView,

urlpatterns = [
    # path('all/vacancies/list/', AllVacanciesListView.as_view(), name = "all-vacancies-list"),
    path('all/companies/', AllCompanyView.as_view(), name = "all-companies-list"),

    # path('postulation/vacancy/<int:vacancy_id>/', PostulationVacancyView.as_view(), name = "postulation-vacancy"),
    # path('my/postulations/', MyPostulationListView.as_view(), name = "my-postulation"),
    # path('detail/vacancy/<int:pk>/', VacancyDetailView.as_view(), name = "detail-vacancy"),

]