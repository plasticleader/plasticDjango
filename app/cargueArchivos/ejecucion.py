import psycopg2
from sqlalchemy import create_engine
from datetime import datetime, date, time, timedelta


def ejecucionInicial(id_Asignacion):
	print(id_Asignacion)
	try:
	    # connect to the PostgreSQL database
	    engine = create_engine('postgresql://intelibpo:2r9qWsZ/<5?,Pkp/@127.0.0.1:5432/straussdb')
	except (Exception, psycopg2.DatabaseError) as error:
	    print(error)


	sql = """
		insert into strauss.data_empresa_straus(empresa_nombre)
		select distinct asignacion_empresa from strauss_asignaciones."cargueArchivos_dataasignacion"
		where
		asignacion_cliente not  in (select distinct e.empresa_nombre from strauss.data_empresa_straus e);


		insert into strauss.data_clientes_straus(cliente_nombre, cliente_direccion,cliente_logo,cliente_color,cliente_telefono,cliente_empresa)
		select f.asignacion_cliente,'','','','',em.id
		from strauss_asignaciones."cargueArchivos_dataasignacion" f
		inner join strauss.data_empresa_straus em on em.empresa_nombre = f.asignacion_empresa
		where
		concat(f.asignacion_cliente,'-',f.asignacion_empresa) not in (select distinct concat(c.cliente_nombre,'-',e.empresa_nombre) 
		from strauss.data_clientes_straus c 
		inner join strauss.data_empresa_straus e on c.cliente_empresa = e.id);


		insert into strauss.data_personas(personas_identificacion, personas_tipo_identificacion, persona_nombre)
		select op.persona_identificacion, op.persona_tipoidentificacion, op.persona_nombre
		from strauss_asignaciones."cargueArchivos_datapersonas" op
		where
		op.persona_identificacion not in (select distinct personas_identificacion from strauss.data_personas)
		order by op.persona_nombre;


		insert into strauss.data_portafolio(portafolio_cliente,portafolio_nombre,portafolio_contrapropuesta,portafolio_descuentos, 
		portafolio_fechacreacion,portafolio_asignacion,portafolio_responsable)
		select  c.id, a.asignacion_nombre, a.asignacion_contrapropuesta, a.asignacion_descuentos, a.asignacion_fechacreacion, a.id,1
		from strauss_asignaciones."cargueArchivos_dataasignacion" a
		inner join strauss.data_clientes_straus c on a.asignacion_cliente = c.cliente_nombre
		where
		a.asignacion_nombre not in (select distinct portafolio_nombre from strauss.data_portafolio p);

		drop table if exists strauss.temp_obligacion_a;
		select
		o.obligacionsaldo_capital, 
		o.obligacionfecha_creacion_obligacion, 
		o.obligacionseguro, 
		o.obligacioncomision, 
		o.obligacionsaldo_interes_corriente, 
		o.obligacionsaldo_interes_mora, 
		o.obligacionsaldo_total, 
		o.obligacionfechacreacion, 
		o.obligacionfecha_vencimiento_obligacion, 
		o.obligacionproducto, 
		o.obligaciontipo_obligacion, 
		o.obligaciontipo_prducto, 
		o.variable1, 
		o.variable1_descripcion, 
		o.variable2, 
		o.variable2_descripcion, 
		o.variable3, 
		o.variable3_descripcion, 
		o.variable4, 
		o.variable4_descripcion,
		o.obligacionportafolio,
		per.persona_id,
		1
		into strauss.temp_obligacion_a
		from strauss_asignaciones."cargueArchivos_dataobligacion" as o
		inner join strauss.data_personas as per on per.personas_identificacion= o.obligacionpersona;

		drop table if exists strauss.temp_potafolio_b;
		select
		o.*,
		p.id
		into strauss.temp_potafolio_b     
		from strauss.temp_obligacion_a as o
		inner join strauss.data_portafolio as p on (p.portafolio_nombre=o.obligacionportafolio);

		INSERT INTO strauss.data_obligacion(
			obligacion_saldocapital, 
			obligacion_fechacreacionobligacion, 
			obligacion_seguro, 
			obligacion_comision, 
			obligacion_saldointerescorriente, 
			obligacion_saldointeresmora, 
			obligacion_saldototal, 
			obligacion_fechacreacion, 
			obligacion_fecha_vencimientoobligacion, 
			obligacion_producto, 
			obligacion_tipoobligacion,
			obligacion_tipo_producto,
			obligacion_variable1, 
			obligacion_variable1_descripcion, 
			obligacion_variable2, 
			obligacion_variable2_descripcion, 
			obligacion_variable3, 
			obligacion_variable3_descripcion, 
			obligacion_variable4, 
			obligacion_variable4_descripcion,
			obligacion_persona, 
			obligacion_portafolio,
			obligacion_estadoobligacion
		)
		select
			o.obligacionsaldo_capital, 
			o.obligacionfecha_creacion_obligacion, 
			o.obligacionseguro, 
			o.obligacioncomision, 
			o.obligacionsaldo_interes_corriente, 
			o.obligacionsaldo_interes_mora, 
			o.obligacionsaldo_total, 
			o.obligacionfechacreacion, 
			o.obligacionfecha_vencimiento_obligacion, 
			o.obligacionproducto, 
			o.obligaciontipo_obligacion, 
			o.obligaciontipo_prducto,
			o.variable1, 
			o.variable1_descripcion, 
			o.variable2, 
			o.variable2_descripcion, 
			o.variable3, 
			o.variable3_descripcion, 
			o.variable4, 
			o.variable4_descripcion,
			o.persona_id,
			o.id,
			1 estadoObligacion
			from strauss.temp_potafolio_b as o;
	"""

	with engine.connect() as connection:
	  connection.execute(sql)
	pass