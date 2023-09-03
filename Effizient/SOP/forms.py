# forms.py
from django import forms
from .models import SOPDocument

class SOPDocumentForm(forms.ModelForm):
    class Meta:
        model = SOPDocument
        fields = ['title', 'description', 'steps', 'email', 'name', 'age', 'highest_education', 'institute']
