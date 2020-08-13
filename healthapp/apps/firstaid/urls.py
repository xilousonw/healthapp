from django.urls import path, re_path, include
from . import views


urlpatterns = [

    # path('', include(router.urls)),
    path('', views.FirstaidView.as_view({'get': 'list'})),
    re_path('detail/(?P<pk>\d+)',views.FirstaidDetailView.as_view({'get': 'retrieve'}))
]
