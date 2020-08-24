from django import form
from .models import Apply

class Applyform(ModelForm):
    class Meta:
        model = Apply
        fields = ['name', 'email', 'website', 'cover_letter', 'cearted_at']