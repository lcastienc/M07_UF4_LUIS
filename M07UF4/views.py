from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

# Create your views here.

#def index(request):
   # return HttpResponse("hello, world")

'''
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
'''
'''
def index(request):

    professor = {"name":"Roger", "surname":"Sobrino", "age":"17"}
    template = loader.get_template('index.html')
    dades = template.render({'nombre':professor["name"], 'surname':professor["surname"], 'age':professor["age"]})
    return HttpResponse(dades)
'''

def index(request):

    professor = {"name":"Roger", "surname":"Sobrino", "age":"17"}
    return render(request, 'index.html', {'nombre':professor["name"], 'surname':professor["surname"], 'age':professor["age"]})

professors = [
        {
            'id':'1',
            'name': 'Felipe',
            'surname': 'Encinas',
            'age': '32',
        },
        {
            'id': '2'
            'name': 'Angel',
            'surname': 'e2e3e3',
            'age':'55',
        },
        {
            'id': '3'
            'name': 'Julian',
            'surname': 'Martinez',
            'age': '34',
        }
    ]

def teachers(request):
    teachers =

def students(request):