import django_filters
from .models import job

class JobFilter(django_filters.FilterSet):
    #3shan afilter bklma mwgoda dmn l descraption
    description = django_filters.CharFilter(lookup_expr='icontains')
    title = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = job
        fields = '__all__'
        exclude = ['published_at', 'vacancy', 'salary', 'image', 'slug', 'owner']