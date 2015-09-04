#Este middleware revisa todas las peticiones post en busca del parametro lang 
# y cambia el idioma al recibido por el parametro.

class setLanguaje(object):
    def process_request(self, request):
        try:
				if request.method == 'POST':
					request.session['lang_code'] = request.POST['lang']
				else:
					if not "lang_code" in request.session:
						request.session['lang_code'] = "es"
        except KeyError:
            pass        