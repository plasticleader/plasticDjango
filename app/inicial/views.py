from django.conf import settings
from django.urls import resolve
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from django.contrib.auth.models import User


def index(request):
	datoUsu = User.objects.filter(id=request.user.id).last()
	usuLogeado = {
		'nombre'  : str(datoUsu.first_name)+' '+str(datoUsu.last_name),
		'email'   : datoUsu.email,
		'usuario' : datoUsu.username,
	}
	return render(request, 'inicial/index.html',{'datoUsu':datoUsu})