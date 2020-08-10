from django.urls import path, re_path, include
from . import views


urlpatterns = [

    path('', views.NewsView.as_view({'get': 'list'})),
    re_path('detail/(?P<pk>\d+)',views.NewsDetailView.as_view({'get': 'retrieve'}))
]
