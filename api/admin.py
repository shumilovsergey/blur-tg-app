from django.contrib import admin
from .models import StendupAuthors
from .models import StendaupFiles


admin.site.register(StendupAuthors)
admin.site.register(StendaupFiles)

