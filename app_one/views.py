from django.shortcuts import render
from .models import Estudiante, Profesor # si queremos importar todo  usamos *
from django.http import HttpResponse



def pagina_formulario(request):
    return render(request, "form.html")


def busqueda_profesor(request):
    
    if request.GET["profesor"]:

        nombre_solicitado = request.GET["profesor"]

        try:
            profesor = Profesor.objects.get(Nombre_y_apellido = nombre_solicitado)
        except Exception as ex:
            mensaje = f"Ocurrio un error: {ex}"
        else:
            mensaje = f'Años de experiencia: {profesor.tiempo_exp}  <br> Asignatura: {profesor.Asignatura}'
        finally:
            return HttpResponse("<h1>"+mensaje+"</h1>")

    else:
        return HttpResponse("<h1 style='color: green; background-color: white'>Busqueda vacia</h1>") # se puede editar como un documento html

#<h1 style='color: green'>Busqueda vacia</h1>


lista_estudiantes = Estudiante.objects.all()

def busqueda_estudiante(request):

    if request.GET["estudiante"]:
        
        nombre_solicitado = request.GET["estudiante"]
        
        lista_personas = Estudiante.objects.filter(Nombre_y_apellido__icontains = nombre_solicitado) 
       
       #lista_personas = []
        #for i in lista_estudiantes:
                #if i.Nombre_y_apellido == nombre_solicitado:
                    #lista_personas.append(i)'''
        
        return render(request, "resultados.html", {"busqueda": nombre_solicitado, "personas": lista_personas})
    else:
        return HttpResponse("Busqueda vacia")


