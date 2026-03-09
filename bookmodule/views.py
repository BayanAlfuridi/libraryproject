from django.http import HttpResponse

def index(request):
    name = request.GET.get('name', 'world!')
    return HttpResponse(f"Hello, {name}")

def index2(request, val1):
    return HttpResponse(f"value1 = {val1}")