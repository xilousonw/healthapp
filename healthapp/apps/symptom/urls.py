from django.urls import path, re_path, include
from . import views

urlpatterns = [

    path('', views.SymptomView.as_view({'get': 'list'})),
    # re_path('detail/(?P<pk>\d+)',views.DiseaseDetailView.as_view({'get': 'retrieve'}))
]
