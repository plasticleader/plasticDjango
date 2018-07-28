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
from django.contrib.auth import authenticate, login
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.contrib import messages


# def index(request):
# 	personas = ''
# 	titulo = 'Dashboard Cargue Archivos'
# 	context = {
# 		'personas': personas, 
# 	}
# 	return render(request, 'archivos/index.html', context)



def crearEmpresaCreate(request):
	if request.method == 'POST':
		form = empresasCreate(request.POST)
		if form.is_valid():
			form.save()
		return redirect('empresaslistar')
	else:
		form = empresasCreate()
		return render(request, 'archivos/empresasCreate.html', {'form':form})



def editarTiposEdit(request, id_tipo):
	ediTipo = DataEmpresaStraus.objects.get(id=id_tipo)
	if request.method == 'GET':
		form = tipoCargue(instance=ediTipo)
	else:
		form = tipoCargue(request.POST,instance=ediTipo)
		if form.is_valid():
			form.save()
		return redirect('empresaslistar')
	return render(request, 'archivos/empresasCreate.html', {'form':form})


def deleteTiposDelete(request, id_tipo):
	deleteTipo = DataEmpresaStraus.objects.get(id=id_tipo)
	if request.method == 'POST':
		deleteTipo.delete()
		return redirect('empresaslistar')
	return render(request, 'archivos/tipocarguesDelete.html', {'deleteTipo':deleteTipo})



class EmpresaList(ListView):
	model           = DataEmpresaStraus
	template_name   = 'cargueArchivos/tipoempresa.html'



		
class ArchivosCargueList(ListView):
	model           = DataEmpresaStraus
	template_name   = 'cargueArchivos/tipoarchivoslistar.html'



class ArchivosCargueProcesar(ListView):
	model           = DataEmpresaStraus
	template_name   = 'cargueArchivos/archivosprocesarlistar.html'





def crearTiposArchivos(request):
	if request.method == 'POST':
		form = TiposArchivos(request.POST)
		if form.is_valid():
			form.save()
			return redirect('archivoscargueslistar')
		else:
			print('No se esta validando el formulario')
			pass
	else:
		form = TiposArchivos()
	return render(request, 'cargueArchivos/tipoarchivosCreate.html', {'form':form})





def crearArchivosProcesados(request):
	print(request.POST)
	if request.method == 'POST':
		form = UploadArchivos(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('archivosprocesarlistar')
		else:
			print('No se esta validando el formulario')
			pass
	else:
		form = UploadArchivos()
	return render(request, 'cargueArchivos/archivosProcesarCreate.html', {'form':form})



def preProcesar(request):
	id_archivo              = request.GET.get('id_archivo')
	archivo                 = DataArchivoCargueProcesar.objects.filter(id=id_archivo).last()
	valores, columnas       = iniPreviw(id_archivo,archivo.archivocargueprocesararchivo,archivo.archivocargueprocesararchivotipocargue.id,archivo.archivocargueprocesararchivoobservacion)
	iniPreviws = dict(valores=valores,columnas=columnas.tolist(),id=id_archivo)
	return HttpResponse(json.dumps(iniPreviws), content_type='application/json')




def ProcesarArchivo(request,id_archivo):
	datoUsu =   datosUsu(request.user.id)
	return render(request, 'cargueArchivos/procesandoArchivo.html',{'datoUsu':datoUsu,'id_archivo':id_archivo})



def ProcesarArchivoUpdate(request,id_archivo):
	datoUsu =   datosUsu(request.user.id)
	return render(request, 'cargueArchivos/procesandoArchivoUpdate.html',{'datoUsu':datoUsu,'id_archivo':id_archivo})

 	

def ProcesarArchivoFinal(request,id_archivoFinal):
	datoUsu =   datosUsu(request.user.id)
	print('Star')
	archivo                 = DataPortafolioarchivosStraus.objects.filter(id=id_archivoFinal).last() 
	cliente                 = archivo.archivos_portafolio.portafolio_cliente.cliente_nombre
	empresa                 = archivo.archivos_portafolio.portafolio_cliente.cliente_empresa
	if cliente == 'Crezcamos':
		procesado       = procesadoFinalCrezcamos(id_archivoFinal,archivo.archivos_archivo,archivo.archivos_portafolio,request.user.id,cliente,empresa)
	else:
		procesado       = procesadoFinalFalabella(id_archivoFinal,archivo.archivos_archivo,archivo.archivos_portafolio,request.user.id,cliente,empresa)
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
		DataPortafolioarchivosStraus.objects.filter(id=id_archivoFinal).update(archivos_estado=True)
		pass
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
		DataPortafolioarchivosStraus.objects.filter(id=id_archivoFinal).update(archivos_estado=True)
		pass
	return render(request, 'cargueArchivos/procesandoArchivoUpdateOk.html',contexto)





#@login_required
def getFalabella(request):

	datoUsu =   datosUsu(request.user.id)

	# print(request.user.first_name)
	#print(request.session)
	# if request.user.is_authenticated():
	# 	print('ok')
	# else:
	# 	print('no')
	# deleteTipo = DataPortafolioarchivosStraus.objects.all()
	# deleteTipo.delete()
	# inner = DataPortafolio.objects.all()
	# inner.delete()
	# DataEstadoobligacion.objects.create(
	# 	estadoobligaciondescripcion='Activo')
	# DataEstadoobligacion.objects.create(
	# 	estadoobligaciondescripcion='Inactivo')
	# DataEstadoobligacion.objects.create(
	# 	estadoobligaciondescripcion='Suspendido')
	# DataEstadoobligacion.objects.create(
	# 	estadoobligaciondescripcion='Pendiente')
	# DataEstadoobligacion.objects.create(
	# 	estadoobligaciondescripcion='Proceso De Revicion')
	# DataEstadoobligacion.objects.create(
	# 	estadoobligaciondescripcion='Aceptado Por El Usuario')
	# DataEstadoobligacion.objects.create(
	# 	estadoobligaciondescripcion='Aceptado Por El Sistema')
	# DataEstadoobligacion.objects.create(
	# 	estadoobligaciondescripcion='Rechazado Por El Usuario')
	# DataEstadoobligacion.objects.create(
	# 	estadoobligaciondescripcion='Rechazado Por El Sistema')
	clie = DataClientesStraus.objects.filter(cliente_nombre='Falabella').last()
	inner_qs = DataPortafolio.objects.filter(portafolio_cliente=clie.id,portafolio_usuario=request.user.id)
	lista = []
	for x in inner_qs:
		lista.append(x.id)
		pass
	campFalabella = DataPortafolioarchivosStraus.objects.filter(archivos_portafolio__in=lista)
	vista = 0
	return render(request, 'cargueArchivos/falabella.html',{'idFile':0,'campFalabella':campFalabella,'vista':vista,'datoUsu':datoUsu})



def falabellaCampanacrear(request):
	print(request.POST)
	datoUsu =   datosUsu(request.user.id)
	if request.method == 'POST':
		strs_nombre = request.POST['archivos_nombre']
		porta, cliente  = getValidate(strs_nombre,'Falabella',request.user.id)
		if porta=='Exite':
			messages = 1
			form = UploadArchivosFallabella()
			return render(request,'cargueArchivos/archivosProcesarCreateFalabella.html',{'messages':messages,'form':form,'portafolio':strs_nombre,'datoUsu':datoUsu})
		else:
			#print(2)
			form = UploadArchivosFallabella(request.POST, request.FILES)
			#print ('Aca Form',form)
			if form.is_valid():
				#files = request.FILES.getlist('file_field')
				#print(files)
				#for f in files:
				idForm = form.save()
				valores1,valores2,valores  = getFalabellaClientePreview(porta,cliente,idForm.id)
				#print('valores',valores)
				#iniPreviws = dict(valores=valores,columnas=columnas.tolist(),id=id_archivo)
				#return HttpResponse(json.dumps(iniPreviws), content_type='application/json')
				#return redirect('falabella')
				vista = 1
				# print(type(valores))
				# valores.replace("&", "&amp;").replace("\"", "&quot;").replace("'", "&apos;").replace(">", "&gt;").replace("<", "&lt;");
				# tmp = valores.replace('[','')
				# print(valores)
				# for x in valores:
				# 	tmp = x
				# 	pass
				# print(valores.tolist())
				# print(type(valores))
				# # tmp = valores.split('-')
				print ('valores',valores)
				#tmp = valores.replace('Pandas','')
				#print ('valores',valores)
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
				return render(request, 'cargueArchivos/falabella.html',{'idFile':idForm.id,'lista':listaFin,'vista':vista,'datoUsu':datoUsu})
			else:
				print('No se esta validando el formulario')
				pass
			pass
	else:
		form = UploadArchivosFallabella()
	return render(request, 'cargueArchivos/archivosProcesarCreateFalabella.html', {'form':form,'datoUsu':datoUsu})


#  Crezcamos

def getCrezcamos(request):
	datoUsu =   datosUsu(request.user.id)
	clie = DataClientesStraus.objects.filter(cliente_nombre='Crezcamos').last()
	inner_qs = DataPortafolio.objects.filter(portafolio_cliente=clie.id,portafolio_usuario=request.user.id)
	lista = []
	for x in inner_qs:
		lista.append(x.id)
		pass
	campCrezcamos = DataPortafolioarchivosStraus.objects.filter(archivos_portafolio__in=lista)
	vista = 0
	return render(request, 'cargueArchivos/Crezcamos/crezcamos.html',{'idFile':0,'campCrezcamos':campCrezcamos,'vista':vista,'datoUsu':datoUsu})




def crezcamosCampanacrear(request):
	datoUsu =   datosUsu(request.user.id)
	if request.method == 'POST':
		strs_nombre = request.POST['archivos_nombre']
		porta, cliente  = getValidate(strs_nombre,'Crezcamos',request.user.id)
		if porta=='Exite':
			messages = 1
			form = UploadArchivosFallabella()
			return render(request,'cargueArchivos/Crezcamos/archivosProcesarCreateCrezcamos.html',{'datoUsu':datoUsu,'messages':messages,'form':form,'portafolio':strs_nombre})
		else:
			form = UploadArchivosFallabella(request.POST, request.FILES)
			if form.is_valid():
				idForm = form.save()
				valores1,valores2,valores  = getCrezcamosClientePreview(porta,cliente,idForm.id)
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
				return render(request, 'cargueArchivos/Crezcamos/crezcamos.html',{'datoUsu':datoUsu,'idFile':idForm.id,'lista':listaFin,'vista':vista})
			else:
				print('No se esta validando el formulario')
				pass
			pass
	else:
		form = UploadArchivosFallabella()
	return render(request, 'cargueArchivos/Crezcamos/archivosProcesarCreateCrezcamos.html', {'datoUsu':datoUsu,'form':form})




def descargaArchivoCampanaSinProcesar(request,id_archivoFinal):
	infoArchivo  = DataPortafolioarchivosStraus.objects.filter(id=id_archivoFinal).last()
	return redirect('http://poseidon.intelibpo.com:8000/static/upload/%s'%(infoArchivo.archivos_archivo))






def getUpdateCrezcamos(request):
	datoUsu =   datosUsu(request.user.id)
	clie = DataClientesStraus.objects.filter(cliente_nombre='Crezcamos').last()
	inner_qs = DataPortafolio.objects.filter(portafolio_usuario=request.user.id,portafolio_cliente=clie.id)
	if request.is_ajax(): 
		idPortafolio =  str(request.GET.get('id', None)) 
		idPortafolioValor =  str(request.GET.get('valor', None))  
		idPortafolioDato =  str(request.GET.get('dato', None))
		if ( (idPortafolioDato=='1') | (idPortafolioDato==1)):
			DataPortafolio.objects.filter(id=idPortafolio).update(portafolio_contrapropuesta=idPortafolioValor)
		else:
			DataPortafolio.objects.filter(id=idPortafolio).update(portafolio_descuentos=idPortafolioValor)
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
	clie = DataClientesStraus.objects.filter(cliente_nombre='Crezcamos').last()
	inner_qs = DataPortafolio.objects.filter(portafolio_usuario=request.user.id,portafolio_cliente=clie.id)
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

	deleteTrazaCamp          = DataTrazabilidadCampanasArchivos.objects.all()
	deleteTrazaCamp.delete()

	deletePortaToken         = DataPersonaPortafolioToken.objects.all()
	deletePortaToken.delete()

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

	deletePersonas           = DataPersona.objects.all()
	deletePersonas.delete()

	deletePortaArchivoStra   = DataPortafolioarchivosStraus.objects.all()
	deletePortaArchivoStra.delete()

	deleteArchiStra          = DataarchivosStraus.objects.all()
	deleteArchiStra.delete()

	deletePorta              = DataPortafolio.objects.all()
	deletePorta.delete()

	return render(request, 'cargueArchivos/limpiar.html',{'datoUsu':datoUsu})