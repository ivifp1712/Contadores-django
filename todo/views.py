from argparse import ArgumentDefaultsHelpFormatter
from re import L
from turtle import title
from django.shortcuts import render
from django.views.defaults import page_not_found
from todo.models import Todo
import time
from random import choice as ch
from datetime import datetime as dt
# Create your views here.
def codigo(request, code):
    a = Todo.objects.get(codigo=code)
    #b = f"{dt(a.created.date()).strftime('%s')}"
    #seconds = int(time.mktime(a.created.timetuple()))

    fcreado = dt.utcfromtimestamp(a.dia /1000).strftime('%Y-%m-%d %H:%M:%S')
    date = a.dia
    if 'contra' in request.POST and not a.completed:
        if str(request.POST['contra']) == str(a.contra):
            a.completed = True
            ahora = dt.now()
            f = ahora.strftime("%Y-%m-%d %H:%M")
            fecha = dt.strptime(f, '%Y-%m-%d %H:%M')
            un = f"{int(time.mktime(fecha.timetuple()))}000"
            un = int(un)
            a.fcompleted = un
            a.save()
        else:
            return render(request, 'contador.html', { "codigo": a, "date": date, "fcreado": fcreado, "falsa": f'{a.contra} in:  {str(request.POST["contra"])})' })
    if a.completed:
        return render(request, 'contador.html', { "codigo": a, "date": date, "com": a.fcompleted , "fcreado": fcreado})
    return render(request, 'contador.html', { "codigo": a, "date": date, "fcreado": fcreado})


def crear(request):
    a = Todo.objects.filter(private=False)
    if 'nombre' in request.POST:
        creador=request.POST['creador']
        name = request.POST['nombre']
        f = request.POST['fecha'] + " " + request.POST['hora']
        fecha = dt.strptime(f, '%Y-%m-%d %H:%M')
        un = f"{int(time.mktime(fecha.timetuple()))}000"
        un = int(un)
        codigo = f"{''.join([ch('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<=>@#%&+') for i in range(6)])}"
        contra = request.POST['contra']
        while Todo.objects.filter(codigo=codigo).count() > 0:
            codigo = f"{''.join([ch('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<=>@#%&+') for i in range(6)])}"
        if 'private' in request.POST:
            private=True
        else:
            private=False
        cont = Todo.objects.create(
            title=name,
            codigo=codigo,
            dia = un,
            creador=creador,
            contra = contra
        )
        resul = "Ha sido creado con exito, y se encuentra disponible en /" + codigo
        return render(request, 'crear.html', {'resul':resul, 'codigo': codigo, 'a': a})
    return render(request, 'crear.html', {"a": a})

def contadoresfp(request):
    a = Todo.objects.all()
    return render(request, "lista.html",{"a": a})

def mi_error_404(request, exception):
    return page_not_found(request, "404.html")