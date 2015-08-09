from django.template import RequestContext
from django.shortcuts import render_to_response, render, redirect
from blog.models import Entrada , Contacto , Mensajes
from django.core.mail import send_mail
from django.conf import settings
import os
# Create your views here.

def home(request):
    context=RequestContext(request)
    return render_to_response('home.html', context)

def calc(request):
    return render_to_response('Calculadora.html',{})

def conv(request):
    return render_to_response('Conversor.html',{})

def crono(request):
    return render_to_response('Cronometro.html',{})

def cv(request):
    return render_to_response('Curriculum.html',{})

def img(request):
    return render_to_response('Imagen.html',{})

def price(request):
    return render_to_response('Premio.html',{})

def principal(request):
    context = RequestContext(request)
    posts = Entrada.objects.filter(published = True)
    return render_to_response('Principal.html', 
                              {'posts':posts},
                              context)
def ver_post(request, id_post):
    context = RequestContext(request)
    mi_post = Entrada.objects.get(id=id_post)
    return render_to_response('post.html', 
                              {'post':mi_post},
                              context)

def contact(request):
    context = RequestContext(request)

    if request.method == 'POST':
        nombre= request.POST['nombre']
        celu= request.POST['celu']
        mail= request.POST['mail']
        mensaje= request.POST['mensaje']
        contacto = Contacto()
        contacto.nombre = nombre
        contacto.celu = celu
        contacto.mail = mail
        contacto.mensaje = mensaje
        contacto.save()
        subject = 'Saludos'
        mensajes = 'Hola soy '+nombre+' y este es mi comentario '+mensaje+'\n Este es mi email para comunicarte conmigo: '+mail
        from_email = settings.EMAIL_HOST_USER
        send_mail(subject, mensajes, from_email,['garciasantione@gmail.com'],fail_silently=False)
        
        
    return render_to_response('contact.html', 
                              context)

def save_message(request):
    context = RequestContext(request)
    mensajes = None
    if request.method == 'POST':
        mi_post = Entrada.objects.get(id=request.POST['id'])
        nombre= request.POST['nombre']
        mensaje= request.POST['mensaje']        
        msje = Mensajes()
        msje.nombre = nombre
        msje.mensaje = mensaje
        msje.published_in = mi_post
        msje.published = True
        msje.save()
        
        mensajes = Mensajes.objects.filter(published_in=mi_post,published = True)
    
    return render_to_response('mensajes.html', 
                              {'mensajes':mensajes},
                              context)
def mensaje(request, id_post):
    context = RequestContext(request)
    post = Entrada.objects.get(pk=id_post)
    if request.method == 'POST':
        nombre= request.POST['nombre']
        mensaje= request.POST['mensaje']        
        contacto = Mensajes()
        contacto.nombre = nombre
        contacto.mensaje = mensaje
        contacto.published_in = post
        contacto.save()
        
       
    
    return render_to_response('post.html', 
                              {'post':post},
                              context)
        
def ver_mensajes(request, id_mensaje):
    context = RequestContext(request)
    mensajes = Entrada.objects.filter(published = True)
    return render_to_response('post.html', 
                              {'mensaje':mensajes},
                              context)

def __unicode__(self):
    return smart_unicode(("%s" % self.descripcion))