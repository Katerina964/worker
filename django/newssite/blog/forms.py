from django import forms
from .models import Resume, Vacancy
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.core import validators


def validate_capitalized(value):
    resault = value.istitle()
    if resault == False:
        raise ValidationError(
            ('must be ')) # it work


class NewField(forms.CharField):
    default_validators = [validate_capitalized]


class MultiField(forms.Field):
    def to_python(self, value):
        """Normalize data to a list of strings."""
        # Return an empty list if no input was given.
        if not value:
            return []
        return value.split(',')

    def validate(self, value):
        """Check if value consists only of valid emails."""
        # Use the parent's handling of required fields, etc.
        super().validate(value)
        for email in value:
            validate_capitalized(email)


class ResumeForm(forms.ModelForm):
    example2 = MultiField()
    example = NewField()

    def clean(self):   # it works as validators, with msg top on field
        super().clean()
        first_name = self.cleaned_data.get("first_name")
        print(first_name)
        surname = self.cleaned_data.get("surname")

        if first_name not in surname:
            msg = "Must put 'help' in subject when cc'ing yourself."
            self.add_error('surname', msg)

    class Meta:
        model = Resume
        fields = ('first_name', 'surname', 'position', 'town',
        'phone', 'email','password', 'experience','skills','achievements', 'education','type_work','addition' ,'salary')
        widgets = {
            'first_name': forms.TextInput(),
            'surname': forms.TextInput(),
            'position': forms.TextInput(attrs={'placeholder': "Желаемая должность"}),
            'town': forms.TextInput(),
            'phone': forms.TextInput(),
            'salary': forms.TextInput(),
            'email': forms.EmailInput(),
            'password': forms.TextInput(attrs={'placeholder': "Введите пароль для авторизации на сайте"} ),
            'experience': forms.Textarea(attrs={'placeholder': "Укажите  опыт работы в порядке убывания" }),
            'skills': forms.Textarea(),
            'achievements': forms.Textarea(),
            'education': forms.Textarea(),
            'addition': forms.Textarea(),
            'type_work': forms.Textarea(attrs={'placeholder': " Укажите важные для Вас критерии. Например: офис, удаленно, количество часов в день."}),

        }

class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ( 'position',  'company', 'type_work', 'town',
        'phone', 'email', 'password', 'description', 'responsibilities','skills', 'offer','salary', 'published_date')
        widgets = {
            'position': forms.TextInput(),
            'company': forms.TextInput(),
            'town': forms.TextInput(),
            'phone': forms.TextInput(),
            'email': forms.EmailInput(),
            'password': forms.TextInput(attrs={'placeholder': "Введите пароль для авторизации на сайте"}),
            'description': forms.Textarea(attrs={'placeholder': "Описание вакансии"}),
            'responsibilities': forms.Textarea(),
            'skills': forms.Textarea(),
            'offer': forms.Textarea(),
            'type_work': forms.Textarea(attrs={'placeholder': " Укажите важные для Вас критерии. Например: офис, удаленно, количество часов в день."}),
            'salary': forms.TextInput(),
        }
