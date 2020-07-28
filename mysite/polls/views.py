from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. fc03d482 is the polls index.")