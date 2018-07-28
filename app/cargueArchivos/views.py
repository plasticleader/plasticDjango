from django.conf import settings
from django.urls import resolve
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from django.template.loader import get_template, render_to_string
from django.views.generic import View
from .models import *
from decimal import Decimal
from datetime import datetime, date, timedelta,time
import re
import simplejson as json
from django.db.models import Sum, Avg, Max
import os
from .forms import *
from django.views.generic import ListView,CreateView
from .clientes import *
from .falabella import *
from .crezcamos import *
from .ejecucion import *
from django.contrib.auth import authenticate, login
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.contrib import messages




def preProcesar(request):
	id_archivo              = request.GET.get('id_archivo')
	archivo                 = DataArchivoCargueProcesar.objects.filter(id=id_archivo).last()
	valores, columnas       = iniPreviw(id_archivo,archivo.archivocargueprocesararchivo,archivo.archivocargueprocesararchivotipocargue.id,archivo.archivocargueprocesararchivoobservacion)
	iniPreviws = dict(valores=valores,columnas=columnas.tolist(),id=id_archivo)
	return HttpResponse(json.dumps(iniPreviws), content_type='application/json')



def ProcesarArchivo(request,idAsiganacion):
	datoUsu =   datosUsu(request.user.id)
	print('Aca llego',idAsiganacion)
	return render(request, 'cargueArchivos/procesandoArchivo.html',{'datoUsu':datoUsu,'id_archivo':idAsiganacion})



def ProcesarArchivoUpdate(request,id_archivo):
	datoUsu =   datosUsu(request.user.id)
	return render(request, 'cargueArchivos/procesandoArchivoUpdate.html',{'datoUsu':datoUsu,'id_archivo':id_archivo})

 	

def ProcesarArchivoFinal(request,idAsiganacion):
	datoUsu =   datosUsu(request.user.id)
	print('Star')
	# archivo                 = DataAsignacionarchivosStraus.objects.filter(id=idAsiganacion).last() 
	# cliente                 = archivo.archivos_portafolio.portafolio_cliente.cliente_nombre
	# empresa                 = archivo.archivos_portafolio.portafolio_cliente.cliente_empresa
	# if cliente == 'Crezcamos':
	# 	procesado       = procesadoFinalCrezcamos(idAsiganacion,archivo.archivos_archivo,archivo.archivos_portafolio,request.user.id,cliente,empresa)
	# else:
	# 	print('Ejecucion del ETL/DASH')
	# 	procesado       = procesadoFinalFalabella(idAsiganacion,archivo.archivos_archivo,archivo.archivos_portafolio,request.user.id,cliente,empresa)
	# 	pass
	# contexto ={
	# 	'personas':procesado['personas'],
	# 	'obligaciones':procesado['obligaciones'],
	# 	'telefonos':procesado['telefonos'],
	# 	'correos':procesado['correos'],
	# 	'tokens':procesado['tokens'],
	# 	'datoUsu':datoUsu,
	# }
	# if procesado['obligaciones']>0:
	# 	DataAsignacionarchivosStraus.objects.filter(id=id_archivoFinal).update(archivos_estado=True)
	# 	pass
	ejecucionInicial(idAsiganacion)
	contexto = {}
	return render(request, 'cargueArchivos/procesandoArchivoOk.html',contexto)



def ProcesarArchivoFinalUpdate(request,id_archivoFinal):
	datoUsu =   datosUsu(request.user.id)
	print('Star Update')
	archivo                 = DataarchivosStraus.objects.filter(id=id_archivoFinal).last() 
	cliente                 = archivo.archivos_portafolio.portafolio_cliente.cliente_nombre
	empresa                 = archivo.archivos_portafolio.portafolio_cliente.cliente_empresa
	if cliente == 'Crezcamos':
		print(1)
		procesado       = procesadoFinalCrezcamosUpdate(id_archivoFinal,archivo.archivos_archivo,archivo.archivos_portafolio,request.user.id,cliente,empresa)
	else:
		print(2)
		procesado       = procesadoFinalFalabellaUpdate(id_archivoFinal,archivo.archivos_archivo,archivo.archivos_portafolio,request.user.id,cliente,empresa)
		pass
	contexto ={
		'personas':procesado['personas'],
		'obligaciones':procesado['obligaciones'],
		'telefonos':procesado['telefonos'],
		'correos':procesado['correos'],
		'tokens':procesado['tokens'],
		'datoUsu':datoUsu,
	}
	if procesado['obligaciones']>0:
		DataAsignacionarchivosStraus.objects.filter(id=id_archivoFinal).update(archivos_estado=True)
		pass
	return render(request, 'cargueArchivos/procesandoArchivoUpdateOk.html',contexto)





#@login_required
def getFalabella(request):
	datoUsu =   datosUsu(request.user.id)
	inner_qs = DataAsignacion.objects.filter(asignacion_cliente='Falabella')
	lista = []
	for x in inner_qs:
		lista.append(x.id)
		pass
	campFalabella = DataAsignacionarchivosStraus.objects.filter(archivos_asignacion__in=lista)
	vista = 0
	return render(request, 'cargueArchivos/falabella.html',{'idAsiganacion':0,'idFile':0,'campFalabella':campFalabella,'vista':vista,'datoUsu':datoUsu})



def falabellaCampanacrear(request):
	print(request.POST)
	datoUsu =   datosUsu(request.user.id)

	if request.method == 'POST':
		strs_nombre = request.POST['archivos_nombre']
		porta  = getValidate(strs_nombre,'Falabella',request.user.id,'Falabella')
		if porta=='Exite':
			messages = 1
			form = UploadArchivosAsignacion()
			resultados = 0
			return render(request,'cargueArchivos/archivosProcesarCreateFalabella.html',{'idAsiganacion':resultados,'messages':messages,'form':form,'portafolio':strs_nombre,'datoUsu':datoUsu})
		else:
			form = UploadArchivosAsignacion(request.POST, request.FILES)
			if form.is_valid():
				idForm = form.save()
				valores1,valores2,valores,resultados  = getFalabellaClientePreview(porta,'Falabella',idForm.id,request.user.id,strs_nombre)
				vista = 1
				lista1 = []
				lista2 = []
				lista3 = []
				listaFin = []
				for x in valores:
					lista1.append(x)
					pass
				for x in valores1:
					lista2.append(x)
					pass

				for x in valores2:
					lista3.append(x)
					pass
				listaFin.append(dict(lista=lista1,lista1=lista2,lista2=lista3))
				return render(request, 'cargueArchivos/falabella.html',{'idFile':idForm.id,'lista':listaFin,'vista':vista,'datoUsu':datoUsu,'idAsiganacion':resultados})
			else:
				print('No se esta validando el formulario')
				pass
			pass
	else:
		form = UploadArchivosAsignacion()
		resultados = 0
	return render(request, 'cargueArchivos/archivosProcesarCreateFalabella.html', {'idAsiganacion':resultados,'form':form,'datoUsu':datoUsu})



#  Crezcamos

def getCrezcamos(request):
	datoUsu =   datosUsu(request.user.id)
	inner_qs = DataAsignacion.objects.filter(asignacion_cliente='Crezcamos')
	lista = []
	for x in inner_qs:
		lista.append(x.id)
		pass
	campCrezcamos = DataAsignacionarchivosStraus.objects.filter(archivos_asignacion__in=lista)
	vista = 0
	return render(request, 'cargueArchivos/Crezcamos/crezcamos.html',{'idFile':0,'campCrezcamos':campCrezcamos,'vista':vista,'datoUsu':datoUsu})




def crezcamosCampanacrear(request):
	datoUsu =   datosUsu(request.user.id)
	if request.method == 'POST':
		strs_nombre = request.POST['archivos_nombre']
		porta  = getValidate(strs_nombre,'Crezcamos',request.user.id,'Crezcamos')
		if porta=='Exite':
			messages = 1
			form = UploadArchivosAsignacion()
			return render(request,'cargueArchivos/Crezcamos/archivosProcesarCreateCrezcamos.html',{'datoUsu':datoUsu,'messages':messages,'form':form,'portafolio':strs_nombre})
		else:
			form = UploadArchivosAsignacion(request.POST, request.FILES)
			if form.is_valid():
				idForm = form.save()
				valores1,valores2,valores,resultados = getCrezcamosClientePreview(porta,'Crezcamos',idForm.id,request.user.id)
				vista = 1
				lista1 = []
				lista2 = []
				lista3 = []
				listaFin = []
				for x in valores:
					lista1.append(x)
					pass
				for x in valores1:
					lista2.append(x)
					pass

				for x in valores2:
					lista3.append(x)
					pass
				listaFin.append(dict(lista=lista1,lista1=lista2,lista2=lista3))
				return render(request, 'cargueArchivos/Crezcamos/crezcamos.html',{'datoUsu':datoUsu,'idFile':idForm.id,'lista':listaFin,'vista':vista,'idAsiganacion':resultados})
			else:
				print('No se esta validando el formulario')
				pass
			pass
	else:
		form = UploadArchivosAsignacion()
	return render(request, 'cargueArchivos/Crezcamos/archivosProcesarCreateCrezcamos.html', {'datoUsu':datoUsu,'form':form})




def descargaArchivoCampanaSinProcesar(request,id_archivoFinal):
	infoArchivo  = DataAsignacionarchivosStraus.objects.filter(id=id_archivoFinal).last()
	return redirect('http://poseidon.intelibpo.com:8000/static/upload/%s'%(infoArchivo.archivos_archivo))






def getUpdateCrezcamos(request):
	datoUsu =   datosUsu(request.user.id)
	clie = DataClientesStraus.objects.filter(cliente_nombre='Crezcamos').last()
	inner_qs = DataAsignacion.objects.filter(portafolio_usuario=request.user.id,portafolio_cliente=clie.id)
	if request.is_ajax(): 
		idPortafolio =  str(request.GET.get('id', None)) 
		idPortafolioValor =  str(request.GET.get('valor', None))  
		idPortafolioDato =  str(request.GET.get('dato', None))
		if ( (idPortafolioDato=='1') | (idPortafolioDato==1)):
			DataAsignacion.objects.filter(id=idPortafolio).update(portafolio_contrapropuesta=idPortafolioValor)
		else:
			DataAsignacion.objects.filter(id=idPortafolio).update(portafolio_descuentos=idPortafolioValor)
			pass
		response = {'tipo': "ok"}
		return HttpResponse(json.dumps(response), content_type='application/json')
	else:
		if request.method == 'POST':
			form = UploadArchivos(request.POST, request.FILES)
			if form.is_valid():
				idForm = form.save()
				valores1,valores2,valores = getCrezcamosClientePreviewUdate(idForm.id)
				lista1 = []
				lista2 = []
				lista3 = []
				listaFin = []
				for x in valores:
					lista1.append(x)
					pass
				for x in valores1:
					lista2.append(x)
					pass

				for x in valores2:
					lista3.append(x)
					pass
				listaFin.append(dict(lista=lista1,lista1=lista2,lista2=lista3))
				vista = 1
				return render(request, 'cargueArchivos/UpdateCampañas/Crezcamos/updateCrezcamos.html',{'idFile':idForm.id,'lista':listaFin,'vista':vista,'form':form,'campCrezcamos':inner_qs,'datoUsu':datoUsu})
			else:
				print('No se esta validando el formulario')
				pass
		else:
			form = UploadArchivos()
			vista = 0
			idForm = 0
		return render(request, 'cargueArchivos/UpdateCampañas/Crezcamos/updateCrezcamos.html',{'idFile':idForm,'vista':vista,'form':form,'campCrezcamos':inner_qs,'datoUsu':datoUsu})



def trazabilidad(request):
	datoUsu =   datosUsu(request.user.id)
	clie = 'Crezcamos'
	inner_qs = DataAsignacion.objects.filter(portafolio_usuario=request.user.id,portafolio_cliente=clie.id)
	if request.method == 'POST':
		form = UploadArchivos(request.POST, request.FILES)
		print(form)
		if form.is_valid():
			idForm = form.save()
			getCrezcamosClientePreviewUdate(idForm.id)
			return render(request, 'cargueArchivos/UpdateCampañas/Crezcamos/updateCrezcamos.html',{'form':form,'campCrezcamos':inner_qs,'datoUsu':datoUsu})
		else:
			print('No se esta validando el formulario')
			pass
	else:
		print(2)
		form = UploadArchivos()
	return render(request, 'cargueArchivos/UpdateCampañas/Crezcamos/updateCrezcamos.html',{'form':form,'campCrezcamos':inner_qs,'datoUsu':datoUsu})



def limpiar(request):
	datoUsu =   datosUsu(request.user.id)

	deleteDatosOrigen        = DataUbicacionInfoOrigen.objects.all()
	deleteDatosOrigen.delete()

	deleteUbicaEmp           = DataUbicacionEmpresa.objects.all()
	deleteUbicaEmp.delete()

	deleteUbica              = DataUbicacion.objects.all()
	deleteUbica.delete()

	deleteCorreos            = DataCorreoelectronico.objects.all()
	deleteCorreos.delete()

	deleteTele               = DataTelefonos.objects.all()
	deleteTele.delete()

	deleteObliga             = DataObligacion.objects.all()
	deleteObliga.delete()

	deletePersonas           = DataPersonas.objects.all()
	deletePersonas.delete()

	deletePortaArchivoStra   = DataAsignacionarchivosStraus.objects.all()
	deletePortaArchivoStra.delete()

	deleteArchiStra          = DataarchivosStraus.objects.all()
	deleteArchiStra.delete()

	deletePorta              = DataAsignacion.objects.all()
	deletePorta.delete()

	return render(request, 'cargueArchivos/limpiar.html',{'datoUsu':datoUsu})