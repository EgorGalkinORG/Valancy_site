from django.shortcuts import render
from .models import Vacancy

# Create your views here.
def render_vacancy_app(request):
    all_vacancies = Vacancy.objects.all()
    return render(request, "vacancy_app/vacancy.html",context={"all_vacancies":all_vacancies})
