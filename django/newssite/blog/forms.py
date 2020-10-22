from django import forms

from .models import Resume

class ResumeForm(forms.ModelForm):

    class Meta:
        model = Resume
        fields = ('first_name', 'surname', 'position', 'town',
        'phone', 'email','password', 'experience','skills','achievements', 'education','type_work','published_date')
