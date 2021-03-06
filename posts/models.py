from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):

	SATUS_CHOICES = (
			('draft','Draft'),
			('published', 'Published'),
		)

	autor = models.ForeignKey(User,related_name='blog_posts',blank=True, null=True)
	titulo = models.CharField(max_length=100)
	cuerpo = models.TextField()
	creado = models.DateTimeField(auto_now=True,blank=True, null=True)
	actualizado = models.DateTimeField(auto_now_add=True,blank=True, null=True)
	status = models.CharField(max_length=10, choices=SATUS_CHOICES, default='draft',blank=True, null=True)
	slug = models.SlugField(max_length=200, unique_for_date='creado',blank=True, null=True)

	class Meta:
		ordering = ('-creado',)

	def __str__(self):
		return self.titulo		