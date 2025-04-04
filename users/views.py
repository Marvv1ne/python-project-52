from django.shortcuts import render
s


def index(request):
    return render(request, 'main_page/index.html')

