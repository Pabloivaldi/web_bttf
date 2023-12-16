from django.shortcuts import render#, HttpResponse
def home(request):
    return render(request, "core/home.html")

    #return HttpResponse(html_base+"<p>hola</p><h2>Portada</h2>")#se puede hacer un html, esto es hardcodear codigo(forzarlo a que funcione) y es solo para demostrar que estamos trabajando con django.

def about(request):
     return render(request, "core/about.html")
    #return HttpResponse(html_base+"<p>hola, mucho gusto<p/>")



def contact(request):
    return render(request, "core/contact.html")
    #return HttpResponse(html_base+"<p>eMail: carlos.arroyo</p>")

def curiosidades(request):
    return render(request, "core/curiosidades.html")

#vamos a crear un menu, vamos a crear una variable

#esta es una forma de ver un poco de html, desde el backend, visto atraves de views:

#html_base ="""
 #   <h1>Mi web personal</h1>
 #       <ul>
#            <li><a href="/">Portada</a></li>
 #           <li><a href="/about-me">Acerca de </a></li>
 #           <li><a href="/portfolio">Portfolio</a></li>
 #           <li><a href="/contact">Contacto</a></li>
#        </ul>
# Create your views here.
#creamos una funcion que nos permita ver un html#

