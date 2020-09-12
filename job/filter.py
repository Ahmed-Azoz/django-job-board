import django_filters
from .models import job

class JobFilter(django_filters.FilterSet):
    class Meta:
        model = job
        fields = '__all__'
        exclude = ['published_at', 'vacancy', 'salary', 'image']