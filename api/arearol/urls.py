from django.urls import path
from .views import Area, RetrieveRolById  


urlpatterns=[
    path('area/', Area.as_view(), name = "area"),
    path('area/<int:area_id>/', RetrieveRolById.as_view(), name = "area"),
] 