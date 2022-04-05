from django.db import models
from django.urls import reverse


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    picture = models.FileField()

    def __str__(self):
        return self.name;


class Code(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    code_type = models.CharField(max_length=100)
    lang_logo = models.FileField()

    def get_absolute_url(self):
        return reverse("cType", kwargs={"code_type": self.code_type})

    def __str__(self):
        return self.code_type;


class Language(models.Model):
    code = models.ForeignKey(Code, on_delete=models.CASCADE)
    project_details = models.CharField(max_length=300)
    project = models.TextField()

    def get_absolute_url(self):
        return reverse("cType", kwargs={"code_type": self.code_type})
    

    def __str__(self):
        return self.project_details;
