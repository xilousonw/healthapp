from django.urls import path, re_path, include
from . import views

urlpatterns = [

    # path('', include(router.urls)),
    path('', views.AccompanyView.as_view({'get': 'list'})),
    path('appointment',views.AppointmentView.as_view({'post':'create'})),
    path('patient', views.PatientView.as_view({'get': 'list'})),
    path('hospital', views.HospitalView.as_view({'get': 'list'})),
    path('patientadd',views.PatientAddView.as_view({'post':'create'})),

    # re_path('detail/(?P<pk>\d+)',views.FirstaidDetailView.as_view({'get': 'retrieve'}))
]
