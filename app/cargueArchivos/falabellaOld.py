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




def getFalabellaClientePreview(straPorta,straCliente,straFile):
	DataPortafolioarchivosStraus.objects.filter(id=straFile).update(archivos_portafolio=straPorta)
	infoArchivo  = DataPortafolioarchivosStraus.objects.filter(id=straFile).last()

	archivo = '/home/pentaho/strauss/cargues/static/upload/%s'%(infoArchivo.archivos_archivo)
	df = pd.read_excel(archivo)
	df = df[['num_documento','NOMBRE', 'Tipo_documento','fecha_apertura','fechaasigna','saldo_total','cupo','dias_mora','Rango','habito_pago','cuenta','TlfCelular','teldom1','TelefCom1','Calle_Corresp','Depto_Correspondencia','Ciudad_Correspondencia','barrio','Calle_Com','Depto_Com','Ciudad_Com','Mail']]
	for row in df.head(1).itertuples(index=False):
		lista1 = row
	for row in df.head(2).itertuples(index=False):
		lista2 = row
	for row in df.head(3).itertuples(index=False):
		lista = row
	return lista1,lista2,lista




def procesadoFinalFalabella(stra_id,stra_file,stra_portafolio,straUsuario,strCliente,straEmpresas):

	archivo = '/home/pentaho/strauss/cargues/static/upload/%s'%(stra_file)
	df = pd.read_excel(archivo)
	df = df[['num_documento','NOMBRE', 'Tipo_documento','fecha_apertura','fechaasigna','saldo_total','cupo','dias_mora','Rango','habito_pago','cuenta','TlfCelular','teldom1','TelefCom1','Calle_Corresp','Depto_Correspondencia','Ciudad_Correspondencia','barrio','Calle_Com','Depto_Com','Ciudad_Com','Mail']]
	df = df.head(20)

	cant_columns = len(df.columns)

	cant_cc = df['num_documento'].count()

	columns_obli = list(df.columns.values)

	sum_saldo_capital = round(df['saldo_total'].sum(),2)

	#df.head(3)

	df_personas = df.copy()
	df_personas.drop_duplicates(subset=["num_documento","Tipo_documento"], keep='first', inplace=True)
	tipoDoc = {1:"CC", 3:"CE"}
	df_personas["Tipo_documento"]=df_personas["Tipo_documento"].map(tipoDoc)
	#df_personas.head()
	df_personas.rename(columns={"num_documento":"persona_identificacion",
                                 "NOMBRE":"persona_nombre",
                                 "Tipo_documento":"persona_tipoidentificacion"},inplace=True)
	#df_personas.head()


	def insertPersona(row):
		if DataPersona.objects.filter(persona_identificacion=row['persona_identificacion']).exists():
			row['persona_id'] = DataPersona.objects.filter(persona_identificacion=row['persona_identificacion']).last()
			row['persona_id'] = row['persona_id']
		else:
			row['persona_id'] = DataPersona.objects.create(
				persona_identificacion       = row['persona_identificacion'],
				persona_nombre               = row['persona_nombre'],
				persona_tipoidentificacion   = row['persona_tipoidentificacion']
			)
			pass
		return row

	df_person = pd.DataFrame()
	for index, row in df_personas.iterrows():
	    df_person = df_person.append(insertPersona(row))
	df_personas = df_person
	#df_personas.head(3)

	
	def insertobligaciones(row):
		DataObligacion.objects.create(
			obligacionpersona                         =DataPersona.objects.get(id=row['persona_id'].id),            
			obligacionportafolio                      =DataPortafolio.objects.get(id=stra_portafolio.id),
			obligacionestado_obligacion               =DataEstadoobligacion.objects.get(id=1),
			obligacionsaldo_capital                   =row['saldototal'],
			obligacionseguro                          =0,
			obligacioncomision                        =0,
			obligacionsaldo_interes_corriente         =row['saldointerescorriente'],
			obligacionsaldo_interes_mora              =row['saldointeresmora'],
			obligacionsaldo_total                     =row['saldototal'],
			obligaciontipo_obligacion                 =row['tipoobligacion'],
			obligacionfecha_creacion_obligacion       =row['fechacreacionobligacion'],
			obligacionfecha_vencimiento_obligacion    =row['fecha_vencimientoobligacion'],
			variable1                                 =row['variable1'],
		    variable1_descripcion                     =row['variable1_descripcion'],
		    variable2                                 =row['variable2'],
		    variable2_descripcion                     =row['variable2_descripcion'],
		    variable3                                 =row['variable3'],
		    variable3_descripcion                     =row['variable3_descripcion'],
		    variable4                                 =row['variable4'],
		    variable4_descripcion                     =row['variable4_descripcion'],
		    obligacionproducto                        =row['cuenta'],
		    obligaciontipo_prducto                    =row['tipo_producto'],
		)
		return row


	df_obligaciones = df[['num_documento','fecha_apertura','fechaasigna','saldo_total','cupo','dias_mora','Rango','habito_pago','cuenta']].copy()
	df_obligaciones['persona_id'] = df_obligaciones['num_documento'].map(df_personas.set_index('persona_identificacion')['persona_id'])
	df_obligaciones['saldointerescorriente'] = 0
	df_obligaciones['saldointeresmora'] = 0
	df_obligaciones['tipoobligacion'] = 'Administrativa'
	df_obligaciones['tipo_producto'] = 'Tarjeta Credito'
	df_obligaciones['variable1_descripcion'] = 'cupo tarjeta credito'
	df_obligaciones['variable2_descripcion'] = 'dias de mora'
	df_obligaciones['variable3_descripcion'] = 'etapa de mora'
	df_obligaciones['variable4_descripcion'] = 'frecuencia de pago'
	df_obligaciones = df_obligaciones.drop(['num_documento'],axis=1)
	df_obligaciones = df_obligaciones.rename(columns={'fecha_apertura':'fechacreacionobligacion','fechaasigna':'fecha_vencimientoobligacion','saldo_total':'saldototal'})
	df_obligaciones = df_obligaciones.rename(columns={'cupo':'variable1','dias_mora':'variable2','Rango':'variable3','habito_pago':'variable4'})
	df_obligaciones['fechacreacionobligacion'] = df_obligaciones['fechacreacionobligacion'].apply(lambda x: str(x)[0:4]+"-"+str(x)[4:6]+"-"+str(x)[6:])
	#df_obligaciones.head()


	df_obligacion = pd.DataFrame()
	for index, row in df_obligaciones.iterrows():
		df_obligacion = df_obligacion.append(insertobligaciones(row))
	df_obligaciones = df_obligacion
	df_obligaciones.head()


	#  Demograficos

	#  Telefonos

	def inserttelefonos(row):
		tmp = int(float(row['numero']))
		if ( (len(str(tmp))==10) | (len(str(tmp))=='10') ):
			tip = 'Celular'
		elif ( (len(str(tmp))==7) | (len(str(tmp))=='7') ):
			tip = 'Fijo'
		else:
			tip = 'No Valido'
			pass
		DataTelefonos.objects.create(
			telefono_numero      =tmp,
			telefono_persona     =DataPersona.objects.get(id=row['persona_id'].id),
			telefono_tipo        =tip
		)
		return row


	df_telefonos = df[['num_documento','TlfCelular','teldom1','TelefCom1']].copy()
	df_telefonos['persona_id'] = df_telefonos['num_documento'].map(df_personas.set_index('persona_identificacion')['persona_id'])
	df_telefonos = df_telefonos.drop(['num_documento'],axis=1)
	df_telefonos = df_telefonos.melt(id_vars=['persona_id'])
	df_telefonos = df_telefonos.rename(columns={'value':'numero'})
	df_telefonos = df_telefonos.drop(['variable'],axis=1)
	# df_telefonos = df_telefonos.sort_values('persona_id')

	df_telefono = pd.DataFrame()
	for index, row in df_telefonos.iterrows():
		df_telefono = df_telefono.append(inserttelefonos(row))
	df_telefonos = df_telefono
	#df_telefonos.head()


	#  Ubicación Personal

	def insertubicaciones(row):
		DataUbicacion.objects.create(
			ubicacion_direccion                  =row['Calle_Corresp'],
			ubicacion_pais                       =row['pais'],
			ubicacion_departamento               =row['Depto_Correspondencia'],
			ubicacion_ciudad                     =row['Ciudad_Correspondencia'],
			ubicacion_barrio                     =row['barrio'],
			ubicacion_persona                    =DataPersona.objects.get(id=row['persona_id'].id)
		)
		return row


	df_ubicaciones = df[['num_documento','Calle_Corresp','Depto_Correspondencia','Ciudad_Correspondencia','barrio']].copy()
	df_ubicaciones['persona_id'] = df_ubicaciones['num_documento'].map(df_personas.set_index('persona_identificacion')['persona_id'])
	df_ubicaciones['pais'] = 'Colombia'
	df_ubicaciones = df_ubicaciones.drop(['num_documento'],axis=1)
	#df_ubicaciones.head()



	df_ubicacion = pd.DataFrame()
	for index, row in df_ubicaciones.iterrows():
		df_ubicacion = df_ubicacion.append(insertubicaciones(row))
	df_ubicaciones = df_ubicacion
	#df_ubicaciones.head()


	# Ubicacion Empresa

	def insertubicaciones_empresas(row):
		DataUbicacionEmpresa.objects.create(
			empresa_direccion=row['Calle_Com'],
			empresa_pais=row['pais'],
			empresa_departamento=row['Depto_Com'],
			empresa_ciudad=row['Ciudad_Com'],
			empresa_persona=DataPersona.objects.get(id=row['persona_id'].id),
		)
		return row


	df_ubicaciones_empresas = df[['num_documento','Calle_Com','Depto_Com','Ciudad_Com']].copy()
	df_ubicaciones_empresas['persona_id'] = df_ubicaciones_empresas['num_documento'].map(df_personas.set_index('persona_identificacion')['persona_id'])
	df_ubicaciones_empresas['pais'] = 'Colombia'
	df_ubicaciones_empresas = df_ubicaciones_empresas.drop(['num_documento'],axis=1)
	#df_ubicaciones_empresas.head()



	df_ubicacion_empresa = pd.DataFrame()
	for index, row in df_ubicaciones_empresas.iterrows():
	    df_ubicacion_empresa = df_ubicacion_empresa.append(insertubicaciones_empresas(row))
	df_ubicaciones_empresas = df_ubicacion_empresa
	#df_ubicaciones_empresas.head()


	#  Email


	def insertcorreoelectronico(row):
		DataCorreoelectronico.objects.create(
			correoelectronico_correo            = row['Mail'],
			correoelectronico_persona           = DataPersona.objects.get(id=row['persona_id'].id)
		)
		return row


	df_correoelectronico = df[['num_documento','Mail']].copy()
	df_correoelectronico['persona_id'] = df_correoelectronico['num_documento'].map(df_personas.set_index('persona_identificacion')['persona_id'])
	df_correoelectronico['pais'] = 'Colombia'
	df_correoelectronico = df_correoelectronico.drop(['num_documento'],axis=1)
	#df_correoelectronico.head()


	df_correo = pd.DataFrame()
	for index, row in df_correoelectronico.iterrows():
	    df_correo = df_correo.append(insertcorreoelectronico(row))
	df_correoelectronico = df_correo
	#df_correoelectronico.head()


	# print('Personas Insertadas'+' '+str(len(df_person)))
	# print('Obligaciones Insertadas'+' '+str(len(df_obligacion)))
	# print('Telefonos Insertadas'+' '+str(len(df_telefono)))
	# print('Email Insertadas'+' '+str(len(df_correo)))
	# print('Ubicacion Insertadas'+' '+str(len(df_ubicacion)))
	# print('UbicacionEmpresa Insertadas'+' '+str(len(df_ubicacion_empresa)))

	resultados = dict(
					personas      = len(df_person),
					obligaciones  = len(df_obligacion),
					telefonos     = len(df_telefono),
					correos       = len(df_correo),
					tokens        = 0
				)
	return resultados

