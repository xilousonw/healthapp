from django.urls import path, re_path, include
from . import views


urlpatterns = [

    # path('', include(router.urls)),
    path('', views.AidView.as_view({'get': 'list'})),
    path('drugs', views.DrugView.as_view({'get': 'list'})),
    re_path('drug/(?P<pk>\d+)',views.DrugDetailView.as_view({'get': 'retrieve'}))
]
