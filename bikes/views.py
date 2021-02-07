from django.shortcuts import render

from .models import Bikes


def bike_list(request):
    bike_list = Bikes.objects.all()

    context = {'bike_list' : bike_list,}

    return render(request, 'Bikes/list.html', context)


def bike_detail(request, slug):
    bike_detail = Bikes.objects.get(slug=slug)

    context = {'bike_detail' : bike_detail}

    return render(request, 'Bikes/detail.html', context)