from django.db import models
from django.forms import ModelForm
# Create your models here.

class citites(models.Model) :
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class movie(models.Model) :
    name = models.CharField(max_length=200)
    city = models.ForeignKey(citites, related_name="city_movie", on_delete=models.PROTECT)


class pvrusers(models.Model) :
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    city = models.ForeignKey(citites, related_name="city_user", on_delete=models.PROTECT)


class userForm(ModelForm) :
    class Meta :
        model = pvrusers
        fields = ['first_name', 'last_name', 'email', 'city']

class movieForm (ModelForm) :
    class Meta :
        model = movie
        fields = ['name', 'city']