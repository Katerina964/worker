widgets = {
    'position': forms.TextInput(attrs={'size': 60}),
    'company': forms.TextInput(attrs={'size': 60}),
    'town': forms.TextInput(attrs={'size': 60}),
    'phone': forms.TextInput(attrs={'size': 60}),
    'email': forms.EmailInput(attrs={'size': 60}),
    'password': forms.TextInput(attrs={'placeholder': "Введите пароль для авторизации на сайте", 'size': 60}),
    'description': forms.Textarea(attrs={'placeholder': "Описание вакансии",'cols': 60, 'rows': 10 }),
    'responsibilities': forms.Textarea(attrs={'cols': 60, 'rows': 10 }),
    'skills': forms.Textarea(attrs={'cols': 60, 'rows': 10 }),
    'offer': forms.Textarea(attrs={'cols': 60, 'rows': 10 }),
    'type_work': forms.Textarea(attrs={'placeholder': " Укажите важные для Вас критерии. Например: офис, удаленно, количество часов в день.", 'cols': 60, 'rows': 10 }),
    'salary': forms.TextInput(attrs={'size': 60}),

}
widgets = {
    'first_name': forms.TextInput(attrs={'size': 60}),
    'surname': forms.TextInput(attrs={'size': 60}),
    'position': forms.TextInput(attrs={'placeholder': "Желаемая должность", 'size': 60}),
    'town': forms.TextInput(attrs={'size': 60}),
    'phone': forms.TextInput(attrs={'size': 60}),
    'salary': forms.TextInput(attrs={'size': 60}),
    'email': forms.EmailInput(attrs={'size': 60}),
    'password': forms.TextInput(attrs={'placeholder': "Введите пароль для авторизации на сайте", 'size': 60}),
    'experience': forms.Textarea(attrs={'placeholder': "Укажите  опыт работы в порядке убывания",'cols': 60, 'rows': 10 }),
    'skills': forms.Textarea(attrs={'cols': 60, 'rows': 10 }),
    'achievements': forms.Textarea(attrs={'cols': 60, 'rows': 10 }),
    'education': forms.Textarea(attrs={'cols': 60, 'rows': 10 }),
    'addition': forms.Textarea(attrs={'cols': 60, 'rows': 10 }),
    'type_work': forms.Textarea(attrs={'placeholder': " Укажите важные для Вас критерии. Например: офис, удаленно, количество часов в день.", 'cols': 60, 'rows': 10 }),

}


class Post(models.Model):
    author =  models.ForeignKey(Author, on_delete=models.CASCADE, blank=True)
    admin_site = models.ForeignKey('auth.User', on_delete=models.CASCADE, default='katerina')
    title = models.CharField(max_length=200)
    text = models.TextField()
    img = models.ImageField(upload_to='hairclip', verbose_name='photo', blank=True)
    published_date = models.DateTimeField(
            default=timezone.now)


    def __str__(self):
        return self.title

# @cache_page(60 * 1440)
 p+table { position:absolute; bottom:20%}
 pre+table { position:absolute; bottom:20%}
