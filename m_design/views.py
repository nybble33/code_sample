from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'm_design/base.html', {})


def starter(request):
    return render(request, 'm_design/starter-template/index.html', {})


def parallax(request):
    return render(request, 'm_design/parallax-template/index.html', {})


def sieve_era(request):
    return render(request, 'm_design/eratosthenes.html', {})


def binary_mouse(request):
    return render(request, 'm_design/binary_mouse.html', {})

def conway_gol(request):
    return render(request, 'm_design/conway_gol.html', {})
