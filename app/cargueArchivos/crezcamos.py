# -*- coding: utf-8 -*-

from .models import *
from configparser import ConfigParser
#from config import config
import os,sys
import numpy as np
import pandas as pd
from pprint import pprint
from glob import glob
import requests,json
from openpyxl import load_workbook
from openpyxl import Workbook
from django.utils.crypto import get_random_string
from django.contrib.auth.models import User
from datetime import datetime, date, time, timedelta
import calendar
import psycopg2
from sqlalchemy import create_engine





def getCrezcamosClientePreview(straPorta,straCliente,straFile,straUsuario):

	DataAsignacionarchivosStraus.objects.filter(id=straFile).update(archivos_asignacion=straPorta)
	infoArchivo  = DataAsignacionarchivosStraus.objects.filter(id=straFile).last()
	archivo = '/home/pentaho/strauss/cargues/static/upload/%s'%(infoArchivo.archivos_archivo)
	df_asignacion = pd.read_excel(archivo)
	def unirnombre(row):
	    row["nombre y apellido"] = row["Primer Nombre"] + " " + row["Primer Apellido"]
	    return row
	df_asignacion = df_asignacion.apply(unirnombre,axis=1)
	df_personas = df_asignacion[['Cedula','nombre y apellido','Numero Credito','Capital Mora','Total Mora','Zona','Oficina','Area','Telefono1','Telefono2']]
	df_personas["tipo_identificacion_id"] = df_personas['Cedula'].apply(lambda x: "CC")
	df_personas=df_personas[['Cedula','tipo_identificacion_id','nombre y apellido','Numero Credito','Capital Mora','Total Mora','Zona','Oficina','Area','Telefono1','Telefono2']]
	df_personas.columns = ['identificacion','tipo_identificacion_id','nombre','Numero Credito','Capital Mora','Total Mora','Zona','Oficina','Area','Telefono1','Telefono2']
	df_personas['nombre'] = df_personas['nombre'].str.strip()
	resultados = procesadoFinal(straFile,archivo,straPorta,straUsuario,'Crezcamos')
	for row in df_personas.head(1).itertuples(index=False):
		lista1 = row
	for row in df_personas.head(2).itertuples(index=False):
		lista2 = row
	for row in df_personas.head(3).itertuples(index=False):
		lista = row
	lista1 = 0
	lista2 = 0
	lista = 0
	return lista1,lista2,lista,resultado



def procesadoFinal(stra_id,stra_file,stra_portafolio,straUsuario,strCliente):
	try:
	    # connect to the PostgreSQL database
	    engine = create_engine('postgresql://intelibpo:2r9qWsZ/<5?,Pkp/@127.0.0.1:5432/straussdb')
	except (Exception, psycopg2.DatabaseError) as error:
	    print(error)

	df = pd.read_excel(stra_file ,converters={'Cedula':str,'Telefono1':str,'Telefono2':str})
	df.to_sql('temp_asignacion_crezcamos', engine, if_exists='replace', schema='strauss_asignacion', chunksize=1000)
	
	sql = """INSERT INTO strauss_asignacion."cargueArchivos_datapersonas"(persona_identificacion, persona_nombre, persona_tipoidentificacion, persona_asignacion_id)SELECT Cedula, "Primer Nombre" +" "+ "Primer Apellido" persoNombre , 1, %s
		FROM strauss_asignacion.temp_asignacion_crezcamos;"""%(stra_portafolio)
	with engine.connect() as connection:
		connection.execute(sql)

	# sql = """
	# 	INSERT INTO strauss_asignacion."cargueArchivos_datatelefonos"(
	# 		telefono_numero,telefono_persona_id)
	# 		SELECT t."TlfCelular", per.id
	# 			FROM strauss_asignacion."temp_asignacion_crezcamos" as t
	# 			INNER JOIN strauss_asignacion."cargueArchivos_datapersonas" per
	# 			ON t.num_documento = per.persona_identificacion

	# 		WHERE per.persona_asignacion_id = %s
	# 		AND t."TlfCelular" is not NULL 
	# 		AND t."TlfCelular" != '';

	# 	INSERT INTO strauss_asignacion."cargueArchivos_datatelefonos"(
	# 		telefono_numero,telefono_persona_id)
	# 		SELECT t."teldom1", per.id
	# 			FROM strauss_asignacion."temp_asignacion_crezcamos" as t
	# 			INNER JOIN strauss_asignacion."cargueArchivos_datapersonas" per
	# 			ON t.num_documento = per.persona_identificacion
				
	# 		WHERE per.persona_asignacion_id = %s
	# 		AND t."teldom1" is not NULL 
	# 		AND t."teldom1" != '';

	# 	INSERT INTO strauss_asignacion."cargueArchivos_datatelefonos"(
	# 		telefono_numero,telefono_persona_id)
	# 		SELECT t."TelefCom1", per.id
	# 			FROM strauss_asignacion."temp_asignacion_crezcamos" as t
	# 			INNER JOIN strauss_asignacion."cargueArchivos_datapersonas" per
	# 			ON t.num_documento = per.persona_identificacion
				
	# 		WHERE per.persona_asignacion_id = %s
	# 		AND t."TelefCom1" is not NULL 
	# 		AND t."TelefCom1" != '';
	# """%(stra_portafolio,stra_portafolio,stra_portafolio)
	# with engine.connect() as connection:
	#     connection.execute(sql)


	# sql = """
	# 	INSERT INTO strauss_asignacion."cargueArchivos_datacorreoelectronico"(
	# 	correoelectronico_correo,correoelectronico_persona_id)
	# 	SELECT t."Mail", per.id
	# 		FROM strauss_asignacion."temp_asignacion_crezcamos" as t
	# 		INNER JOIN strauss_asignacion."cargueArchivos_datapersonas" per
	# 		ON t.num_documento = per.persona_identificacion
			
	# 	WHERE per.persona_asignacion_id = %s
	# 	AND t."Mail" is not NULL 
	# 	AND t."Mail" != ''
	# """%(stra_portafolio)

	# with engine.connect() as connection:
	#     connection.execute(sql)

	# sql = """
	# 	INSERT INTO strauss_asignacion."cargueArchivos_dataubicacion"(
	# 	ubicacion_direccion,ubicacion_departamento,ubicacion_ciudad,ubicacion_barrio,ubicacion_persona_id)
	# 	SELECT t."Calle_Corresp",t."Depto_Correspondencia",t."Ciudad_Correspondencia",t."barrio", per.id
	# 		FROM strauss_asignacion."temp_asignacion_crezcamos" as t
	# 		INNER JOIN strauss_asignacion."cargueArchivos_datapersonas" per
	# 		ON t.num_documento = per.persona_identificacion
			
	# 	WHERE per.persona_asignacion_id = %s
	# """%(stra_portafolio)

	# with engine.connect() as connection:
	#     connection.execute(sql)


	# sql = """
	# 	INSERT INTO strauss_asignacion."cargueArchivos_dataubicacionempresa"(
	# 	empresa_direccion,empresa_departamento,empresa_ciudad,empresa_persona_id)
	# 	SELECT t."Calle_Com",t."Depto_Com",t."Ciudad_Com", per.id
	# 		FROM strauss_asignacion."temp_asignacion_crezcamos" as t
	# 		INNER JOIN strauss_asignacion."cargueArchivos_datapersonas" per
	# 		ON t.num_documento = per.persona_identificacion
			
	# 	WHERE per.persona_asignacion_id = %s
	# """%(stra_portafolio)

	# with engine.connect() as connection:
	#     connection.execute(sql)


	# sql = """
	# 	INSERT INTO strauss_asignacion."cargueArchivos_dataobligacion"(
	# 	obligacionpersona_id,obligacionportafolio_id,obligacionfechacreacion,obligacionsaldo_capital,obligacionseguro,obligacioncomision,
	# 	obligacionsaldo_interes_corriente,obligacionsaldo_interes_mora,obligacionsaldo_total,obligaciontipo_obligacion,
	# 	obligacionfecha_creacion_obligacion,obligacionfecha_vencimiento_obligacion,variable1,variable1_descripcion,
	# 	variable2,variable2_descripcion,variable3,variable3_descripcion,variable4,variable4_descripcion,obligacionproducto,
	# 	obligaciontipo_prducto)	
	# 	SELECT per.id,%s,'%s',t."saldo_total",'0' valSeg,'0' valComi, '0' valInteCorr, '0' valintMora ,t."saldo_total",'Administrativa' tipoObli,t."fecha_apertura",
	# 		t."fechaasigna",t."cupo",'cupo tarjeta credito' desVar1,t."dias_mora",'dias de mora' desVa2,
	# 		t."Rango",'etapa de mora' desVar3,t."habito_pago",'frecuencia de pago' desVar4,t."cuenta",
	# 		'Tarjeta Credito' tipoProd
	# 		FROM strauss_asignacion."temp_asignacion_crezcamos" as t
	# 		INNER JOIN strauss_asignacion."cargueArchivos_datapersonas" per
	# 		ON t.num_documento = per.persona_identificacion
			
	# 	WHERE per.persona_asignacion_id = %s
	# """%(stra_portafolio,datetime.now(),stra_portafolio)

	# with engine.connect() as connection:
	#     connection.execute(sql)
    
	pass





def procesadoFinalCrezcamos(stra_id,stra_file,stra_portafolio,straUsuario,strCliente,straEmpresas):

	# archivo                = '/home/pentaho/strauss/cargues/static/upload/%s'%(stra_file)
	# df                     = pd.read_excel(archivo)
	# cant_columns           = len(df.columns)
	# cant_cc                = df['Cedula'].count()
	# columns_obli           = list(df.columns.values)
	# sum_saldo_capital      = round(df['Total Mora'].sum(),2)
	# tipoProducto           = 'CREZ-CREDI'
	# tipoObligacion         = 'Administrativa'
	# df_asignacion = df.head(20)

	# def unirnombre(row):
	#     row["nombre y apellido"] = row["Primer Nombre"] + " " + row["Primer Apellido"]
	#     return row

	# df_asignacion = df_asignacion.apply(unirnombre,axis=1)


	# df_personas = df_asignacion[['Cedula','nombre y apellido']]
	# df_personas["tipo_identificacion_id"] = df_personas['Cedula'].apply(lambda x: "CC")
	# df_personas=df_personas[['Cedula','tipo_identificacion_id','nombre y apellido']]
	# df_personas.columns = ['persona_identificacion','persona_tipoidentificacion','persona_nombre']
	# df_personas['persona_nombre'] = df_personas['persona_nombre'].str.strip()
	# df_personas.head()

	# # print(df_personas.head())

	# df_personas.drop_duplicates(subset=['persona_identificacion', 'persona_tipoidentificacion'],inplace=True)
	# dict_personas = df_personas.to_dict('records')

	# contPersonas = 0
	# DataPersona.objects.update()
	# for persona in dict_personas:
	#     if DataPersona.objects.filter(persona_identificacion=persona['persona_identificacion']).exists():
	#         print("Existe persona con ID: "+ str(persona['persona_identificacion']) + ", tipo: " + str(persona['persona_tipoidentificacion']) )
	#     else:
	#         contPersonas = contPersonas + 1
	#         DataPersona.objects.create(**persona)
	#         print ('Contador:'+' '+str(contPersonas))
	# stra_cantPersonas = contPersonas




	# def inserttelefonos(
	# 	persona,
	# 	tel1,
	# 	tel2
	# 	):
	# 	contTelefonos = 0
	# 	tel1 = str(tel1).replace('nan','0')
	# 	tel2 = str(tel2).replace('nan','0')
	# 	tmp1 = int(float(tel1))
	# 	tmp2 = int(float(tel2))

	# 	if ( ((len(str(tmp1))==10) | (len(str(tmp1))=='10')) | ((len(str(tmp2))==10) | (len(str(tmp2))=='10')) ):
	# 		tip = 'Celular'
	# 	elif ( ((len(str(tmp1))==7) | (len(str(tmp1))=='7')) | ((len(str(tmp2))==7) | (len(str(tmp2))=='7')) ):
	# 		tip = 'Fijo'
	# 	else:
	# 		tip = 'No Valido'
	# 		pass

	# 	tmpCliente = 'Este telefono se obtiene de una base del cliente '+str(strCliente)+' '

	# 	if len(str(tmp1))>1:
	# 		if DataTelefonos.objects.filter(telefono_numero=tmp1,telefono_persona=persona).exists():
	# 			print('Exite Telefono 1')
	# 			contTelefonos = 0
	# 		else:
	# 			print('Ok Telefono 1')
	# 			crateTel1 = DataTelefonos.objects.create(
	# 				telefono_numero      =tmp1,
	# 				telefono_persona     =persona,
	# 				telefono_tipo        =tip
	# 			)
				
	# 			DataUbicacionInfoOrigen.objects.create(
	# 				ubicaorigen_empresa         =DataEmpresaStraus.objects.get(id=straEmpresas.id),
	# 				ubicaorigen_persona         =persona,
	# 				ubicaorigen_telefono        =DataTelefonos.objects.get(id=crateTel1.id),
	# 				ubicaorigen_email           = None,
	# 				ubicaorigen_observacion     = tmpCliente,
	# 				ubicaorigen_usuario         = User.objects.get(id=straUsuario),
	# 			)
	# 			contTelefonos = contTelefonos + 1
	# 			pass	
	# 	else:
	# 		print('Telefono 1 Invalido')
	# 		contTelefonos = 0
	# 		pass


	# 	if len(str(tmp2))>1:
	# 		if DataTelefonos.objects.filter(telefono_numero=tmp2,telefono_persona=persona).exists():
	# 			print('Exite Telefono 2')
	# 			contTelefonos = 0
	# 		else:
	# 			print('Ok Telefono 2')
	# 			crateTel2 = DataTelefonos.objects.create(
	# 				telefono_numero      =tmp2,
	# 				telefono_persona     =persona,
	# 				telefono_tipo        =tip
	# 			)
	# 			DataUbicacionInfoOrigen.objects.create(
	# 				ubicaorigen_empresa         =DataEmpresaStraus.objects.get(id=straEmpresas.id),
	# 				ubicaorigen_persona         =persona,
	# 				ubicaorigen_telefono        =DataTelefonos.objects.get(id=crateTel2.id),
	# 				ubicaorigen_email           = None,
	# 				ubicaorigen_observacion     = tmpCliente,
	# 				ubicaorigen_usuario         = User.objects.get(id=straUsuario),
	# 			)
	# 			contTelefonos = contTelefonos + 1
	# 			pass
	# 	else:
	# 		print('Telefono 2 Invalido')
	# 		pass
	# 	return contTelefonos


	# def cargue_tels_crezcamos(row):

	# 	persona = DataPersona.objects.get(persona_identificacion=row['Cedula'])
	# 	reto = inserttelefonos(
	# 		persona,
	# 		row['Telefono1'],
	# 		row['Telefono2']
	# 		)
	# 	return reto


	# cantTelefonos = df_asignacion.apply(cargue_tels_crezcamos,axis=1) 


	# def crearObligacion(
	#     producto,
	#     saldo_capital,
	#     identificacion,
	#     diasMora,
	#     oficina,
	#     zona
	#     ):
	#     algo = 1
	#     persona = DataPersona.objects.get(persona_identificacion=identificacion)
	#     DataObligacion.objects.create(
	# 		obligacionpersona                         =persona,            
	# 		obligacionportafolio                      =DataPortafolio.objects.get(id=stra_portafolio.id),
	# 		obligacionestado_obligacion               =DataEstadoobligacion.objects.get(id=1),
	# 		obligacionsaldo_capital                   =saldo_capital,
	# 		obligacionseguro                          =0,
	# 		obligacioncomision                        =0,
	# 		obligacionsaldo_interes_corriente         =0,
	# 		obligacionsaldo_interes_mora              =0,
	# 		obligacionsaldo_total                     =saldo_capital,
	# 		obligaciontipo_obligacion                 ='Administrativa',
	# 		obligacionfecha_creacion_obligacion       ='000-00-00',
	# 		obligacionfecha_vencimiento_obligacion    ='000-00-00',
	# 		variable1                                 =diasMora,
	# 	    variable1_descripcion                     ='DIAS MORA',
	# 	    variable2                                 =oficina,
	# 	    variable2_descripcion                     ='OFICINA',
	# 	    variable3                                 =zona,
	# 	    variable3_descripcion                     ='ZONA',
	# 	    obligacionproducto                        =producto,
	# 	    obligaciontipo_prducto                    ='CREZ-CREDI',
	# 	)
	#     return algo

	# def crearObligaciones(seriep):   

	#     crearObligacion(
	#         seriep["Numero Credito"],
	#         seriep["Total Mora"],
	#         seriep["Cedula"],
	#         seriep["Dias\nMora"],
	#         seriep["Oficina"],
	#         seriep["Zona"],
	#     )

	# cantObligaciones = 0
	# cantObligaciones = df_asignacion.apply(crearObligaciones,axis=1) + cantObligaciones




	# def generartoken():
	#     return get_random_string(length=16)

	# cantTokens = 0
	# for i in df_personas['persona_identificacion']:
	#     persona = DataPersona.objects.get(persona_identificacion=i)
	#     if not DataPersonaPortafolioToken.objects.filter(perportatoken_portafolio=stra_portafolio.id,perportatoken_persona=persona).exists():
	#         mitoken = generartoken()
	#         try:
	#            DataPersonaPortafolioToken.objects.get(
	#                 perportatoken_portafolio = DataPortafolio.objects.get(id=stra_portafolio.id),
	#                 perportatoken_persona = persona,
	#                 perportatoken_token = mitoken
	#             ) 
	#         except:
	#             print("Creando Token")
	#             DataPersonaPortafolioToken.objects.create(
	#                 perportatoken_portafolio = DataPortafolio.objects.get(id=stra_portafolio.id),
	#                 perportatoken_persona = persona,
	#                 perportatoken_token = mitoken
	#             )
	#     else:
	#         print('La persona:'+' '+str(persona)+'Ya tiene tokens en este portafolio')
	#         pass
	#     cantTokens = cantTokens + 1
	#     pass

	# resultados = dict(
	# 				personas               = stra_cantPersonas,
	# 				obligaciones           = len(cantObligaciones),
	# 				telefonos              = len(cantTelefonos),
	# 				correos                = 0,
	# 				tokens                 = cantTokens
	# 			)
	# DataPortafolio.objects.filter(id=stra_portafolio.id).update(portafolio_cantObligaciones=len(cantObligaciones),portafolio_cantTokens=cantTokens,portafolio_cantRegistros=cant_cc)
	# DataTrazabilidadCampanasArchivos.objects.create(
	# 	traza_usuario               = User.objects.get(id=straUsuario),
	# 	traza_portafolio            = DataPortafolio.objects.get(id=stra_portafolio.id),
	# 	traza_cantRegisBefore       = cant_cc,
	# 	traza_cantRegisLatest       = cant_cc,
	# 	traza_cantObliBefore        = len(cantObligaciones),
	# 	traza_cantObliLatest        = len(cantObligaciones),
	# 	traza_cantTokBefore         = cantTokens,
	# 	traza_cantTokLatest         = cantTokens,
	# )
	resultados = dict(
					personas               = 0,
					obligaciones           = 0,
					telefonos              = 0,
					correos                = 0,
					tokens                 = 0
				)
	return resultados




#  Update Diario

def getCrezcamosClientePreviewUdate(stra_id):
	# infoArchivo  = DataarchivosStraus.objects.filter(id=stra_id).last()

	# archivo = '/home/pentaho/strauss/cargues/static/upload/%s'%(infoArchivo.archivos_archivo)
	# portafolio = infoArchivo.archivos_portafolio

	# df_asignacion = pd.read_excel(archivo)
	# df_asignacion.head(3)
	# def unirnombre(row):
	#     row["nombre y apellido"] = row["Primer Nombre"] + " " + row["Primer Apellido"]
	#     return row

	# df_asignacion = df_asignacion.apply(unirnombre,axis=1)
	
	# df_personas = df_asignacion[['Cedula','nombre y apellido','Numero Credito','Capital Mora','Total Mora','Zona','Oficina','Area','Telefono1','Telefono2']]
	# df_personas["tipo_identificacion_id"] = df_personas['Cedula'].apply(lambda x: "CC")
	# df_personas=df_personas[['Cedula','tipo_identificacion_id','nombre y apellido','Numero Credito','Capital Mora','Total Mora','Zona','Oficina','Area','Telefono1','Telefono2']]
	# df_personas.columns = ['identificacion','tipo_identificacion_id','nombre','Numero Credito','Capital Mora','Total Mora','Zona','Oficina','Area','Telefono1','Telefono2']
	# df_personas['nombre'] = df_personas['nombre'].str.strip()
	
	# print(df_personas.head())
	# for row in df_personas.head(1).itertuples(index=False):
	# 	lista1 = row
	# for row in df_personas.head(2).itertuples(index=False):
	# 	lista2 = row
	# for row in df_personas.head(3).itertuples(index=False):
	# 	lista = row
	lista1 = 0
	lista2 = 0
	lista = 0
	return lista1,lista2,lista






def procesadoFinalCrezcamosUpdate(stra_id,stra_file,stra_portafolio,straUsuario,strCliente,straEmpresas):
	# print(datetime.now())
	# archivo                = '/home/pentaho/strauss/cargues/static/upload/%s'%(stra_file)
	# df                     = pd.read_excel(archivo)
	# cant_columns           = len(df.columns)
	# cant_cc                = df['Cedula'].count()
	# columns_obli           = list(df.columns.values)
	# sum_saldo_capital      = round(df['Total Mora'].sum(),2)
	# tipoProducto           = 'CREZ-CREDI'
	# tipoObligacion         = 'Administrativa'

	# df_asignacion = df.head(20)

	# def unirnombre(row):
	#     row["nombre y apellido"] = row["Primer Nombre"] + " " + row["Primer Apellido"]
	#     return row

	# df_asignacion = df_asignacion.apply(unirnombre,axis=1)


	# df_personas = df_asignacion[['Cedula','nombre y apellido']]
	# df_personas["tipo_identificacion_id"] = df_personas['Cedula'].apply(lambda x: "CC")
	# df_personas=df_personas[['Cedula','tipo_identificacion_id','nombre y apellido']]
	# df_personas.columns = ['persona_identificacion','persona_tipoidentificacion','persona_nombre']
	# df_personas['persona_nombre'] = df_personas['persona_nombre'].str.strip()
	# df_personas.head()

	# # print(df_personas.head())

	# df_personas.drop_duplicates(subset=['persona_identificacion', 'persona_tipoidentificacion'],inplace=True)
	# dict_personas = df_personas.to_dict('records')

	# contPersonas = 0
	# DataPersona.objects.update()
	# for persona in dict_personas:
	#     if DataPersona.objects.filter(persona_identificacion=persona['persona_identificacion']).exists():
	#         print("Existe persona con ID: "+ str(persona['persona_identificacion']) + ", tipo: " + str(persona['persona_tipoidentificacion']) )
	#     else:
	#         contPersonas = contPersonas + 1
	#         DataPersona.objects.create(**persona)
	#         #print ('Contador:'+' '+str(contPersonas))
	# stra_cantPersonas = contPersonas


	# def inserttelefonos(
	# 	persona,
	# 	tel1,
	# 	tel2
	# 	):
	# 	contTelefonos = 0
	# 	tel1 = str(tel1).replace('nan','0')
	# 	tel2 = str(tel2).replace('nan','0')
	# 	tel1 = str(tel1).replace(' ','0')
	# 	tel2 = str(tel2).replace(' ','0')
	# 	tmp1 = int(float(tel1))
	# 	tmp2 = int(float(tel2))

	# 	if ( ((len(str(tmp1))==10) | (len(str(tmp1))=='10')) | ((len(str(tmp2))==10) | (len(str(tmp2))=='10')) ):
	# 		tip = 'Celular'
	# 	elif ( ((len(str(tmp1))==7) | (len(str(tmp1))=='7')) | ((len(str(tmp2))==7) | (len(str(tmp2))=='7')) ):
	# 		tip = 'Fijo'
	# 	else:
	# 		tip = 'No Valido'
	# 		pass

	# 	tmpCliente = 'Este telefono se obtiene de una base del cliente '+str(strCliente)+' '

	# 	if len(str(tmp1))>1:
	# 		if DataTelefonos.objects.filter(telefono_numero=tmp1,telefono_persona=persona).exists():
	# 			print('Exite Telefono 1')
	# 			contTelefonos = 0
	# 		else:
	# 			print('Ok Telefono 1')
	# 			DataTelefonos.objects.update()
	# 			crateTel1 = DataTelefonos.objects.create(
	# 				telefono_numero      =tmp1,
	# 				telefono_persona     =persona,
	# 				telefono_tipo        =tip
	# 			)
	# 			DataUbicacionInfoOrigen.objects.update()
	# 			DataUbicacionInfoOrigen.objects.create(
	# 				ubicaorigen_empresa         =DataEmpresaStraus.objects.get(id=straEmpresas.id),
	# 				ubicaorigen_persona         =persona,
	# 				ubicaorigen_telefono        =DataTelefonos.objects.get(id=crateTel1.id),
	# 				ubicaorigen_email           = None,
	# 				ubicaorigen_observacion     = tmpCliente,
	# 				ubicaorigen_usuario         = User.objects.get(id=straUsuario),
	# 			)
	# 			contTelefonos = contTelefonos + 1
	# 			pass	
	# 	else:
	# 		print('Telefono 1 Invalido')
	# 		contTelefonos = 0
	# 		pass


	# 	if len(str(tmp2))>1:
	# 		if DataTelefonos.objects.filter(telefono_numero=tmp2,telefono_persona=persona).exists():
	# 			print('Exite Telefono 2')
	# 			contTelefonos = 0
	# 		else:
	# 			print('Ok Telefono 2')
	# 			DataTelefonos.objects.update()
	# 			crateTel2 = DataTelefonos.objects.create(
	# 				telefono_numero      =tmp2,
	# 				telefono_persona     =persona,
	# 				telefono_tipo        =tip
	# 			)
	# 			DataUbicacionInfoOrigen.objects.update()
	# 			DataUbicacionInfoOrigen.objects.create(
	# 				ubicaorigen_empresa         =DataEmpresaStraus.objects.get(id=straEmpresas.id),
	# 				ubicaorigen_persona         =persona,
	# 				ubicaorigen_telefono        =DataTelefonos.objects.get(id=crateTel2.id),
	# 				ubicaorigen_email           = None,
	# 				ubicaorigen_observacion     = tmpCliente,
	# 				ubicaorigen_usuario         = User.objects.get(id=straUsuario),
	# 			)
	# 			contTelefonos = contTelefonos + 1
	# 			pass
	# 	else:
	# 		print('Telefono 2 Invalido')
	# 		pass
	# 	return contTelefonos


	# def cargue_tels_crezcamos(row):

	# 	persona = DataPersona.objects.get(persona_identificacion=row['Cedula'])
	# 	reto = inserttelefonos(
	# 		persona,
	# 		row['Telefono1'],
	# 		row['Telefono2']
	# 		)
	# 	return reto


	# cantTelefonos = df_asignacion.apply(cargue_tels_crezcamos,axis=1) 
	# DataObligacion.objects.update()
	# DataObligacion.objects.filter(obligacionportafolio=DataPortafolio.objects.get(id=stra_portafolio.id)).update(obligacionestado_obligacion=DataEstadoobligacion.objects.get(id=2))
	# DataPortafolio.objects.update()
	# tmpcant_cc_before       = DataPortafolio.objects.filter(id=stra_portafolio.id).last()
	# print('ssss',tmpcant_cc_before)
	# cant_cc_before          = tmpcant_cc_before.portafolio_cantRegistros
	# cantObligacionesBefore  = tmpcant_cc_before.portafolio_cantObligaciones
	# cantTokensBefore        = tmpcant_cc_before.portafolio_cantTokens
	# fechaActBefore          = tmpcant_cc_before.portafolio_fechaactualizacion

	# def crearObligacion(
	#     producto,
	#     saldo_capital,
	#     identificacion,
	#     diasMora,
	#     oficina,
	#     zona
	#     ):
	#     algo = 1
	#     persona = DataPersona.objects.get(persona_identificacion=identificacion)
	#     DataObligacion.objects.update()
	#     DataObligacion.objects.create(
	# 		obligacionpersona                         =persona,            
	# 		obligacionportafolio                      =DataPortafolio.objects.get(id=stra_portafolio.id),
	# 		obligacionestado_obligacion               =DataEstadoobligacion.objects.get(id=1),
	# 		obligacionsaldo_capital                   =saldo_capital,
	# 		obligacionseguro                          =0,
	# 		obligacioncomision                        =0,
	# 		obligacionsaldo_interes_corriente         =0,
	# 		obligacionsaldo_interes_mora              =0,
	# 		obligacionsaldo_total                     =saldo_capital,
	# 		obligaciontipo_obligacion                 ='Administrativa',
	# 		obligacionfecha_creacion_obligacion       ='000-00-00',
	# 		obligacionfecha_vencimiento_obligacion    ='000-00-00',
	# 		variable1                                 =diasMora,
	# 	    variable1_descripcion                     ='DIAS MORA',
	# 	    variable2                                 =oficina,
	# 	    variable2_descripcion                     ='OFICINA',
	# 	    variable3                                 =zona,
	# 	    variable3_descripcion                     ='ZONA',
	# 	    obligacionproducto                        =producto,
	# 	    obligaciontipo_prducto                    ='CREZ-CREDI',
	# 	)
	#     return algo

	# def crearObligaciones(seriep):   

	#     crearObligacion(
	#         seriep["Numero Credito"],
	#         seriep["Total Mora"],
	#         seriep["Cedula"],
	#         seriep["Dias\nMora"],
	#         seriep["Oficina"],
	#         seriep["Zona"],
	#     )

	# cantObligaciones = 0
	# cantObligaciones = df_asignacion.apply(crearObligaciones,axis=1) + cantObligaciones




	# def generartoken():
	#     return get_random_string(length=16)

	# cantTokens = 0
	# DataPersonaPortafolioToken.objects.update()
	# for i in df_personas['persona_identificacion']:
	# 	persona = DataPersona.objects.get(persona_identificacion=i)
	# 	if not DataPersonaPortafolioToken.objects.filter(perportatoken_portafolio=stra_portafolio.id,perportatoken_persona=persona).exists():
	# 		mitoken = generartoken()
	# 		try:
	# 			DataPersonaPortafolioToken.objects.get(
	# 				perportatoken_portafolio = DataPortafolio.objects.get(id=stra_portafolio.id),
	# 				perportatoken_persona = persona,
	# 				perportatoken_token = mitoken
	# 			)
	# 		except:
	# 			print("Creando Token")
	# 			DataPersonaPortafolioToken.objects.create(
	# 				perportatoken_portafolio = DataPortafolio.objects.get(id=stra_portafolio.id),
	# 				perportatoken_persona = persona,
	# 				perportatoken_token = mitoken
	# 			)
	# 			cantTokens = cantTokens + 1
	# 	else:
	# 		print('La persona:'+' '+str(persona)+'Ya tiene tokens en este portafolio')
	# 		pass
	# 	pass

	resultados = dict(
					personas               = 0,
					obligaciones           = 0,
					telefonos              = 0,
					correos                = 0,
					tokens                 = 0
				)
	
	return resultados