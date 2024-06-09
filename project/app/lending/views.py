from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'lending/index.html')


def about(request):
    return render(request, 'lending/about.html')


def contact(request):
    return render(request, 'lending/contact.html')