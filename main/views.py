from django.shortcuts import render
from django.views.generic import View
import requests
import hashlib

class Welcome(View):

	def get(self, request):
		per = "Hulk"
		name = buscar(per)['data']['results'][0]['name']
		descripcion = buscar(per)['data']['results'][0]['description']
		img = buscar(per)['data']['results'][0]['thumbnail']['path']+"."+buscar(per)['data']['results'][0]['thumbnail']['extension']

		template_name = "welcome.html"
		return render(request, template_name, {'name':name, 'descrip':descripcion, 'img':img})

def buscar(nombre):
	ts = "1"
	public_key = "e3ec45ee10546a5704a99007d18e0735"
	private_key = "cb0e48780a020aa0ea0020aeaecc78a2e7decdb4"

	ha = hashlib.md5((ts+private_key+public_key).encode()).hexdigest()

	url = "http://gateway.marvel.com/v1/public/"

	personaje = requests.get(url+"characters", params = {'apikey':public_key,'ts':ts,'hash':ha,'name':nombre}).json()
	
	return personaje
