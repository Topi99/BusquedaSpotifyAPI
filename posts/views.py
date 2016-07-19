from django.shortcuts import render
from django.views.generic import View
from .models import Post
from django.contrib.auth.models import User

class Index(View):
	def get(self, request):
		user = User.objects.get(username="Topi99")
		posts = user.blog_posts.all()
		template_name = "index.html"
		context = {
			'posts':posts
		}
		return render(request, template_name, context)