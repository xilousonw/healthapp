

# 自定义过滤规则
# from rest_framework.filters import BaseFilterBackend
#
# class DrugFilter(BaseFilterBackend):
#     def filter_queryset(self, request, queryset, view):
#         # 真正的过滤规则
#         # params=request.GET.get('teacher')
#         # queryset.filter('''''')
#         return queryset[:1]

#

import django_filters
from django_filters.filterset import FilterSet
from django_filters import filters


from . import models
class DrugFilterSet(FilterSet):
    drug_kind = django_filters.CharFilter(field_name='drug_kind', lookup_expr='icontains')
    drug_otc = django_filters.CharFilter(field_name='drug_otc', lookup_expr='icontains')
    drug_yibao = django_filters.CharFilter(field_name='drug_yibao', lookup_expr='icontains')


    class Meta:
        model=models.Drug
        fields=['drug_kind','drug_otc','drug_yibao']