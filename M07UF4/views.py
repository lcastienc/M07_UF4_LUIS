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

professor =[{"name":"Roger", "surname":"Sobrino", "age":"17"}, {"name":"Pere", "surname":"Gobrino", "age":"30"}, {"name":"Soger", "surname":"Nobrino", "age":"71"}]

teachers= [
    {
        "id":"1",
        "name":"Luis",
        "surname":"Castillo",
        "age":"22"
    },
    {
        "id":"2",
        "name":"Leonardo",
        "surname":"Ricaurte",
        "age":"33"
    },
    {
        "id":"3",
        "name": "Andres",
        "surname": "Carles",
        "age": "44"
    }
]


def teachers(request):
    teachers = [
        {
            "id": "1",
            "name": "Luis",
            "surname": "Castillo",
            "age": "22"
        },
        {
            "id": "2",
            "name": "Leonardo",
            "surname": "Ricaurte",
            "age": "33"
        },
        {
            "id": "3",
            "name": "Andres",
            "surname": "Carles",
            "age": "44"
        }
    ]
    context = {'ts':teachers}
    return render(request, 'teachers.html',context)

def students(request):
    students = [
        {
            "id": "4",
            "name": "Kevin",
            "surname": "Villegas",
            "age": "23"
        },
        {
            "id": "5",
            "name": "Raul",
            "surname": "Rufo",
            "age": "20"
        },
        {
            "id": "6",
            "name": "Raul",
            "surname": "Vaquerizo",
            "age": "20"
        },
        {
            "id": "7",
            "name": "Joan",
            "surname": "Gimenez",
            "age": "25"
        },
        {
            "id": "8",
            "name": "Pepito",
            "surname": "Pancho",
            "age": "33"
        },
        {
            "id": "9",
            "name": "Sancho",
            "surname": "Panza",
            "age": "18"
        }
    ]
    context = {'stds':students}
    return render(request,'students.html',context)