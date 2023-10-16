from django.http import HttpResponse
#Request: para realizar peticiones
# HttpResponse: Para enviar la respuesta usando el protocolo HTTP.

#Esto es una vista: 
def bienvenida(request): #Pasamos un objeto de tipo request como primer argumento
    return HttpResponse("Bienvenido a este curso de DJANGO! ")