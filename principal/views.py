from django.http 							import HttpResponseRedirect, HttpResponse
from django.shortcuts 						import render_to_response, redirect
from django.template 						import RequestContext
from .models								import Gallery,Items,Pases

def home(request):	
	datos = {"urlubic": "home/","men1":"active"}
	return render_to_response('home.html', datos, context_instance=RequestContext(request, request.session))

def about(request):
	datos = {"urlubic": "about/","men2":"active"}
	return render_to_response('about.html', datos, context_instance=RequestContext(request, request.session))

def attractive(request):
	datosGallery = Gallery.objects.filter(activo=True)

	listDatos = []

	for gallery in datosGallery:
		listItems = []
		datosItems = Items.objects.filter(gallery_id=gallery.id,activo=True).order_by("orden")
		defultGall1 = ""
		defultGall2 = ""

		if (gallery.default):
			defultGall1 = "active"
			defultGall2 = "active in"

		for items in datosItems:
			listItems.append({
				"ruta":items.ruta,"tipo":items.tipo,"nombre":items.nombre,"title":items.title
			})

		listDatos.append({"nombre":gallery.nombre,"items": listItems,"class1": defultGall1,"class2":defultGall2})

	datos = {"urlubic": "attractives/","men3":"active","gallerys":listDatos}
	return render_to_response('attractive.html', datos, context_instance=RequestContext(request, request.session))

def contact(request):
	datos = {"urlubic": "contact/","men6":"active"}
	return render_to_response('contact.html', datos, context_instance=RequestContext(request, request.session))	

def maintenance(request):
	datos = {"urlubic": "products/maintenance/","men4":"active"}
	return render_to_response('maintenance.html', datos, context_instance=RequestContext(request, request.session))	

def telecom(request):
	datos = {"urlubic": "products/telecom/","men4":"active"}
	return render_to_response('develop.html', datos, context_instance=RequestContext(request, request.session))	

def legal(request):
	datos = {"urlubic": "products/legal/","men4":"active"}
	return render_to_response('develop.html', datos, context_instance=RequestContext(request, request.session))	

def access(request):
	datosPases = Pases.objects.filter(activo=True)

	listDatos = []

	for fpase in datosPases:
		listDatos.append({"id":fpase.id,"langcode":fpase.langcode,"esurl":fpase.esurl,"enurl":fpase.enurl,"default":fpase.default})

	datos = {"urlubic": "products/access/","men4":"active","datos":listDatos}
	return render_to_response('access.html', datos, context_instance=RequestContext(request, request.session))	

def lrcc(request):
	datos = {"urlubic": "products/lrcc/","men4":"active"}
	return render_to_response('develop.html', datos, context_instance=RequestContext(request, request.session))	

def cccn(request):
	datos = {"urlubic": "news/cccn/","men5":"active"}
	return render_to_response('cccnews.html', datos, context_instance=RequestContext(request, request.session))	

def qpasa(request):
	datos = {"urlubic": "news/qpasa/","men5":"active"}
	return render_to_response('qpasa.html', datos, context_instance=RequestContext(request, request.session))	

def cdcliving(request):
	datos = {"urlubic": "news/cdcliving/","men5":"active"}
	return render_to_response('cdcliving.html', datos, context_instance=RequestContext(request, request.session))			