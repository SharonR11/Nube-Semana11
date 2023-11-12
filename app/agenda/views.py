from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required


from .models import Persona
from django.db.models import Q

@login_required
def menu(request):
    persona_list=Persona.objects.all()
    context={"persona_list":persona_list}
    return render(request,'plantilla/menu.html',context)

#Crear Persona
def insertarpersona(request):
    nombre=request.POST["txtnombre"]
    apellido=request.POST["txtapellido"]
    email=request.POST["txtemail"]
    celular=request.POST["txtcelular"]    
    persona=Persona.objects.create(nombre=nombre,apellido=apellido,email=email,celular=celular)
    return redirect('/')

def datapersona(request,idPersona):
    persona=Persona.objects.get(idPersona=idPersona)
    context={"persona":persona}
    return render(request, 'plantilla/editar.html', context)

#Editar Contacto
def editar(request,idPersona):
    persona=get_object_or_404(Persona,idPersona=idPersona)

    if request.method == 'POST':
        nombre = request.POST.get('txtnombre')
        apellido = request.POST.get('txtapellido')
        email = request.POST.get('txtemail')
        celular = request.POST.get('txtcelular')

        persona.nombre = nombre
        persona.apellido = apellido
        persona.email = email
        persona.celular = celular

        # Guardar los cambios en la venta
        persona.save()

        # Redireccionar a una página de éxito o a la página de detalles de la venta
        return redirect('/')
    return render(request, '/', {'persona': persona})

#Eliminar Contacto
def eliminar(request, idPersona):

    persona = Persona.objects.get(idPersona=idPersona)
    persona.delete()
    return redirect('/')