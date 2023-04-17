from django.shortcuts import render, redirect
from django.urls import reverse
import csv
from django.conf import settings
from django.core.paginator import Paginator


def index(request):
    return redirect(reverse('bus_stations'))




def bus_stations(request):
    # получаем текущую страницу из GET-параметров
    page_number = request.GET.get('page')

    # читаем csv файл и сохраняем его содержимое в список stations
    with open(settings.BUS_STATION_CSV, encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        stations = [row for row in reader]

    # задаем количество элементов на странице и создаем объект пагинации Paginator
    paginator = Paginator(stations, 10)

    # получаем объект текущей страницы
    page_obj = paginator.get_page(page_number)

    context = {
        'bus_stations': page_obj,
        'page': page_obj.number,
    }
    return render(request, 'stations/index.html', context)

