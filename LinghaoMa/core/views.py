from django.shortcuts import render


def stations(request):
    return render(request, 'core/stations.html')
