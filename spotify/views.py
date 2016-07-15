from django.shortcuts import render
from django.views.generic import View
import requests

class Main(View):
	
	def get(self, request):
		template_name = "home.html"
		q = request.GET.get('q')
		
		if q == None:
			q = 'master of puppets'

		res = buscar(q)
		context = {'name':res['albums']['items'][0]['name'],
							 'img':res['albums']['items'][0]['images'][0]['url'],
							 'type':res['albums']['items'][0]['type'],
							 'url':res['albums']['items'][0]['external_urls']['spotify'],
							 'uri':res['albums']['items'][0]['uri'],
							 'q':q}

		return render(request, template_name, context)

def buscar(q):
	url="https://api.spotify.com/v1/"#search?query=master+of+puppets&offset=0&limit=20&type=album
	resultado = requests.get(url+"search",params = {'query':q,'type':'album'}).json()
	return resultado