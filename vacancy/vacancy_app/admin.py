from django.contrib import admin

# Register your models here.
from .models import Category, Vacancy, Company

admin.site.register([Category, Vacancy, Company])
