from django import forms

from .models import Resume, Vacancy

class ResumeForm(forms.ModelForm):

    class Meta:
        model = Resume
        fields = ('first_name', 'surname', 'position', 'town',
        'phone', 'email','password', 'experience','skills','achievements', 'education','type_work','published_date')
        error_messages = {

                'blank': "Заполните,пожалуйста, поле %(field_labels) ",
            }

        widgets = {
            'first_name': forms.TextInput(attrs={'size': 60}),
            'surname': forms.TextInput(attrs={'size': 60}),
            'position': forms.TextInput(attrs={'placeholder': "Желаемая должность", 'size': 60}),
            'town': forms.TextInput(attrs={'size': 60}),
            'phone': forms.TextInput(attrs={'size': 60}),
            'phone': forms.TextInput(attrs={'size': 60}),
            'email': forms.TextInput(attrs={'size': 60}),

            'password': forms.TextInput(attrs={'placeholder': "Введите пароль для авторизации на сайте", 'size': 60}),
            'experience': forms.Textarea(attrs={'placeholder': "Укажите  опыт работы в порядке убывания",'cols': 60, 'rows': 10 }),
            'skills': forms.Textarea(attrs={'cols': 60, 'rows': 10 }),
            'achievements': forms.Textarea(attrs={'cols': 60, 'rows': 10 }),
            'education': forms.Textarea(attrs={'cols': 60, 'rows': 10 }),
            'type_work': forms.Textarea(attrs={'placeholder': " Укажите важные для Вас критерии. Например: офис, удаленно, количество часов в день.", 'cols': 60, 'rows': 10 }),

        }

class VacancyForm(forms.ModelForm):

    class Meta:
        model = Vacancy
        fields = ( 'position',  'company', 'type_work', 'town',
        'phone', 'email', 'password', 'description', 'responsibilities','skills', 'offer','published_date')

        widgets = {
            'position': forms.TextInput(attrs={'size': 60}),
            'company': forms.TextInput(attrs={'size': 60}),
            'town': forms.TextInput(attrs={'size': 60}),
            'phone': forms.TextInput(attrs={'size': 60}),
            'email': forms.TextInput(attrs={'size': 60}),

            'password': forms.TextInput(attrs={'placeholder': "Введите пароль для авторизации на сайте", 'size': 60}),
            'description': forms.Textarea(attrs={'placeholder': "Описание вакансии",'cols': 60, 'rows': 10 }),
            'responsibilities': forms.Textarea(attrs={'cols': 60, 'rows': 10 }),
            'skills': forms.Textarea(attrs={'cols': 60, 'rows': 10 }),
            'offer': forms.Textarea(attrs={'cols': 60, 'rows': 10 }),
            'type_work': forms.Textarea(attrs={'placeholder': " Укажите важные для Вас критерии. Например: офис, удаленно, количество часов в день.", 'cols': 60, 'rows': 10 }),

        }
