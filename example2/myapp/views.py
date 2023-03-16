from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'myapp/index.html')

def mon(request):
    return render(request, 'myapp/mon.html')

def tues(request):
    return render(request, 'myapp/tues.html')

def wends(request):
    return render(request, 'myapp/wends.html')

def hello(request, name):
    print(name)
    context = {
        'name': name
        }
    return render(request, 'myapp/hello.html', context)

def sum_num(request, a, b):

    context = {
        'name': a + b
        }

    return render(request, 'myapp/hello.html', context)