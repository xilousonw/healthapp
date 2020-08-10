from django.urls import path, re_path, include
from . import views

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
# router.register('firstaid', views.FirstaidView, 'firstaid')
# router.register('firstaid/detail', views.FirstaidDetailView, 'firstaid/detail')
urlpatterns = [

    # path('', include(router.urls)),
    path('', views.FirstaidView.as_view({'get': 'list'})),
    re_path('detail/(?P<pk>\d+)',views.FirstaidDetailView.as_view({'get': 'retrieve'}))
]
