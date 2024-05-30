from django.shortcuts import render
from quiz.models import Alumno

# Create your views here.
def vista_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'vista_alumnos.html', {'alumnos': alumnos})


    