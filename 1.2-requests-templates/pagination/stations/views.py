import csv
from pprint import pprint

from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from pagination.settings import BUS_STATION_CSV


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # количество записей на одной странице
    count_stations = 20
    # заготовка списка для передачи в шаблон
    bus_stations_list = []
    # получим параметр(если его нет, покажем первую страничку)
    page = int(request.GET.get('page', 1))
    # так как к CSV файлу нельзя обратиться по индексу строки, перезапишем его в "МАССИВ"(список)
    with open(BUS_STATION_CSV, newline='', encoding="utf-8-sig") as csvfile:
        reader = csv.DictReader(csvfile)
        array = []
        for row in reader:
            array.append(row)
    paginator = Paginator(array, count_stations)
    try:
        bus_stations_list = paginator.page(page)
    except PageNotAnInteger:
        # Если страница не является целым числом, поставим первую страницу
        bus_stations_list = paginator.page(1)
    except EmptyPage:
        # Если страница больше максимальной, доставить последнюю страницу результатов
        bus_stations_list = paginator.page(paginator.num_pages)

    # этот класс явно где-то уже описан, но захотелось попрактиковаться
    class Pages:
        def __init__(self, num, max):
            self.number = num
            self.max = max

        def number(self):
            return self.number

        def has_next(self):
            if self.number < self.max:
                return True
            else:
                return False

        def has_previous(self):
            if self.number > 1:
                return True
            else:
                return False

        def previous_page_number(self):
            if self.number > self.max:
                return self.max - 1
            return self.number - 1

        def next_page_number(self):
            return self.number + 1

    page_obj = Pages(page, paginator.num_pages)
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    context = {
        'bus_stations': bus_stations_list,
        'page': page_obj,
    }
    return render(request, 'stations/index.html', context)
