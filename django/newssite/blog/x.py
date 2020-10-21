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



class Author(models.Model):
    name =models.CharField(max_length=50)
    surname = models.CharField(max_length=50)






      <!-- {% for key, value in each.items %} -->

     <!-- <p>{{ each.snippet|striptags|cut:"&nbsp;..."|truncatechars:272  }}</p>
     Заработная плата: {{ each.salary|default:":не указана" }}
     <pre>Компания: {{ each.company }}         Дата обновления: {{ each.updated|slice:":10" }}</pre> -->

<!-- {% endfor %} -->
