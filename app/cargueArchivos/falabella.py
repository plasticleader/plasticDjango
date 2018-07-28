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
import psycopg2
from sqlalchemy import create_engine
from datetime import datetime, date, time, timedelta




def getFalabellaClientePreview(straPorta,straCliente,straFile,straUsuario,straNombre):
	DataAsignacionarchivosStraus.objects.filter(id=straFile).update(archivos_asignacion=straPorta)
	infoArchivo  = DataAsignacionarchivosStraus.objects.filter(id=straFile).last()

	archivo = '/home/pentaho/strauss/cargues/static/upload/%s'%(infoArchivo.archivos_archivo)
	df = pd.read_excel(archivo)
	df = df[['num_documento','NOMBRE', 'Tipo_documento','fecha_apertura','fechaasigna','saldo_total','cupo','dias_mora','Rango','habito_pago','cuenta','TlfCelular','teldom1','TelefCom1','Calle_Corresp','Depto_Correspondencia','Ciudad_Correspondencia','barrio','Calle_Com','Depto_Com','Ciudad_Com','Mail']]
	resultados = procesadoFinal(straFile,archivo,straPorta,straUsuario,'Falabella',straNombre)
	for row in df.head(1).itertuples(index=False):
		lista1 = row
	for row in df.head(2).itertuples(index=False):
		lista2 = row
	for row in df.head(3).itertuples(index=False):
		lista = row
	return lista1,lista2,lista,resultados



def procesadoFinal(stra_id,stra_file,stra_portafolio,straUsuario,strCliente,straNombre):
	try:
	    # connect to the PostgreSQL database
	    engine = create_engine('postgresql://intelibpo:2r9qWsZ/<5?,Pkp/@127.0.0.1:5432/straussdb')
	except (Exception, psycopg2.DatabaseError) as error:
	    print(error)
	df = pd.read_excel(stra_file ,converters={'num_documento':str,'TlfCelular':str,'teldom1':str,'TelefCom1':str})
	df.to_sql('temp_asignacion_temp_asignacion_falabella', engine, if_exists='replace', schema='strauss_asignaciones', chunksize=1000)




	sql = """INSERT INTO strauss_asignaciones."cargueArchivos_datapersonas"(persona_identificacion, persona_nombre, persona_tipoidentificacion, persona_asignacion)
		SELECT t."num_documento", t."NOMBRE",'CC' tipCC, '%s'
		FROM strauss_asignaciones."temp_asignacion_temp_asignacion_falabella" as t
	"""%(straNombre)
	with engine.connect() as connection:
		connection.execute(sql)

	sql = """
		INSERT INTO strauss_asignaciones."cargueArchivos_datatelefonos"(
			telefono_numero,telefono_persona)
			SELECT t."TlfCelular", t."num_documento"
				FROM strauss_asignaciones."temp_asignacion_temp_asignacion_falabella" as t
			WHERE  
			t."TlfCelular" is not NULL 
			AND t."TlfCelular" != '';

		INSERT INTO strauss_asignaciones."cargueArchivos_datatelefonos"(
			telefono_numero,telefono_persona)
			SELECT t."teldom1", t."num_documento"
				FROM strauss_asignaciones."temp_asignacion_temp_asignacion_falabella" as t
			WHERE t."teldom1" is not NULL 
			AND t."teldom1" != '';

		INSERT INTO strauss_asignaciones."cargueArchivos_datatelefonos"(
			telefono_numero,telefono_persona)
			SELECT t."TelefCom1", t."num_documento"
				FROM strauss_asignaciones."temp_asignacion_temp_asignacion_falabella" as t
			WHERE t."TelefCom1" is not NULL 
			AND t."TelefCom1" != '';
	"""
	with engine.connect() as connection:
	    connection.execute(sql)


	sql = """
		INSERT INTO strauss_asignaciones."cargueArchivos_datacorreoelectronico"(
		correoelectronico_correo,correoelectronico_persona)
		SELECT t."Mail", t."num_documento"
			FROM strauss_asignaciones."temp_asignacion_temp_asignacion_falabella" as t
		WHERE t."Mail" is not NULL 
		AND t."Mail" != ''
	"""
	with engine.connect() as connection:
	    connection.execute(sql)

	sql = """
		INSERT INTO strauss_asignaciones."cargueArchivos_dataubicacion"(
		ubicacion_direccion,ubicacion_departamento,ubicacion_ciudad,ubicacion_barrio,ubicacion_persona)
		SELECT t."Calle_Corresp",t."Depto_Correspondencia",t."Ciudad_Correspondencia",t."barrio", t."num_documento"
			FROM strauss_asignaciones."temp_asignacion_temp_asignacion_falabella" as t
	"""
	with engine.connect() as connection:
	    connection.execute(sql)


	sql = """
		INSERT INTO strauss_asignaciones."cargueArchivos_dataubicacionempresa"(
		empresa_direccion,empresa_departamento,empresa_ciudad,empresa_persona)
		SELECT t."Calle_Com",t."Depto_Com",t."Ciudad_Com", t."num_documento"
			FROM strauss_asignaciones."temp_asignacion_temp_asignacion_falabella" as t
	"""
	with engine.connect() as connection:
	    connection.execute(sql)


	sql = """
		INSERT INTO strauss_asignaciones."cargueArchivos_dataobligacion"(
		obligacionpersona,obligacionportafolio,obligacionfechacreacion,obligacionsaldo_capital,obligacionseguro,obligacioncomision,
		obligacionsaldo_interes_corriente,obligacionsaldo_interes_mora,obligacionsaldo_total,obligaciontipo_obligacion,
		obligacionfecha_creacion_obligacion,obligacionfecha_vencimiento_obligacion,variable1,variable1_descripcion,
		variable2,variable2_descripcion,variable3,variable3_descripcion,variable4,variable4_descripcion,obligacionproducto,
		obligaciontipo_prducto)	
		SELECT t."num_documento",'%s','%s',t."saldo_total",'0' valSeg,'0' valComi, '0' valInteCorr, '0' valintMora ,t."saldo_total",'Administrativa' tipoObli,t."fecha_apertura",
			t."fechaasigna",t."cupo",'cupo tarjeta credito' desVar1,t."dias_mora",'dias de mora' desVa2,
			t."Rango",'etapa de mora' desVar3,t."habito_pago",'frecuencia de pago' desVar4,t."cuenta",
			'Tarjeta Credito' tipoProd
			FROM strauss_asignaciones."temp_asignacion_temp_asignacion_falabella" as t
	"""%(straNombre,datetime.now())

	with engine.connect() as connection:
	    connection.execute(sql)

	return stra_portafolio





def procesadoFinalFalabella(stra_id,stra_file,stra_portafolio,straUsuario,strCliente):

	
	resultados = dict(
					personas      = len(df_person),
					obligaciones  = len(df_obligacion),
					telefonos     = len(df_telefono),
					correos       = len(df_correo),
					tokens        = 0
				)
	return resultados

