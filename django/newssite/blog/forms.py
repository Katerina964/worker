from django import forms
from .models import Resume, Vacancy
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.core import validators


# def validate_space(value):
#     if value.isspace():
#         raise ValidationError(
#             _('%(value)s is not an even number'),
#             params={'value': value},
#        )

# class CharField(forms.Field):
#
#      def validate(self, value):
#         super().validate(value)
#         if value.isspace():
#             raise forms.ValidationError("You have forgotten about Fred!")

# def validate_even(value):
#     if value.isspace():
#         raise ValidationError('%s is not an even number' % value)

# class MyField(forms.CharField):
#     default_validators = [validate_even]
    # def check_space(self, value):
    #     if value.isspace():
    #         raise ValidationError('%s is not an even number' % value)


class ResumeForm(forms.ModelForm):
    # default_validators = [validate_even]
    # def validate(self,value):
    #     if value.isspace():
    #         raise ValidationError('%s is not an even number' % value)

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
