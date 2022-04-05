from django.contrib import admin
from .models import Person, Code, Language

# Register your models here.

admin.site.register(Person)
admin.site.register(Code)
admin.site.register(Language)
