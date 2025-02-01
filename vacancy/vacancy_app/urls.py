from django.urls import path
from .views import render_vacancy_app

urlpatterns = [
    path('vacancy/', render_vacancy_app)
]