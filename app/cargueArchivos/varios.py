# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime




class DataClientesStraus(models.Model):
    cliente_nombre = models.CharField(max_length=512, blank=True, null=True)
    cliente_direccion = models.CharField(max_length=512, blank=True, null=True)
    cliente_logo = models.CharField(max_length=512, blank=True, null=True)
    cliente_color = models.CharField(max_length=512, blank=True, null=True)
    cliente_telefono = models.CharField(max_length=512, blank=True, null=True)
    cliente_empresa = models.ForeignKey('DataEmpresaStraus', models.DO_NOTHING, db_column='cliente_empresa')

    



class DataCorreoelectronico(models.Model):
    correoelectronico_correo = models.CharField(max_length=326, blank=True, null=True)
    correoelectronico_id = models.IntegerField(primary_key=True)
    correoelectronico_persona = models.ForeignKey('DataPersona', models.DO_NOTHING,default='')

    


class DataEmpresaStraus(models.Model):
    empresa_direccion = models.CharField(max_length=512, blank=True, null=True)
    empresa_nit = models.CharField(max_length=512, blank=True, null=True)
    empresa_nombre = models.CharField(max_length=512, blank=True, null=True)
    empresa_razonsocial = models.CharField(max_length=512, blank=True, null=True)
    empresa_logo = models.CharField(max_length=512, blank=True, null=True)
    empresa_responsablenombre = models.CharField(max_length=512, blank=True, null=True)
    empresa_responsabletelefono = models.CharField(max_length=512, blank=True, null=True)
    empresa_telefono = models.CharField(max_length=512, blank=True, null=True)
    empresa_email = models.CharField(max_length=512, blank=True, null=True)

    


class DataEstadoobligacion(models.Model):
    estadoobligacion_descripcion = models.CharField(max_length=512, blank=True, null=True)
    estadoobligacion_fechacreacion = models.CharField(max_length=512, blank=True, null=True)

    

class DataPortafolio(models.Model):
    portafolio_nombre = models.CharField(max_length=512, blank=True, null=True)
    portafolio_contrapropuesta = models.TextField(blank=True, null=True)
    portafolio_descuentos = models.TextField(blank=True, null=True)
    portafolio_responsablecorreo = models.CharField(max_length=512, blank=True, null=True)
    portafolio_responsablenombre = models.CharField(max_length=512, blank=True, null=True)
    portafolio_responsabletelefono = models.CharField(max_length=512, blank=True, null=True)
    portafolio_fechacreacion = models.DateTimeField(default = datetime.now)
    portafolio_cliente = models.ForeignKey(DataClientesStraus, models.DO_NOTHING, db_column='portafolio_cliente')

    


class DataPersona(models.Model):
    persona_fechacreacion = models.DateTimeField(default = datetime.now)
    persona_identificacion = models.CharField(max_length=30)
    persona_nombre = models.CharField(max_length=300, blank=True, null=True)
    persona_tipoidentificacion = models.CharField(max_length=10, blank=True, null=True)
    persona_id = models.IntegerField(primary_key=True)

    


class Obligacion(models.Model):
    fecha_creacion                  = models.DateTimeField(db_column = 'obligacion_fechacreacion', default = datetime.now) # en el sistema
    fecha_creacion_obligacion       = models.DateField(db_column = 'obligacion_fechacreacionobligacion', blank=True, null=True)
    fecha_vencimiento_obligacion    = models.DateField(db_column = 'obligacion_fecha_vencimientoobligacion', blank=True, null=True)
    producto                        = models.CharField(db_column = 'obligacion_producto', max_length = 300)
    persona                         = models.ForeignKey(DataPersona, db_column = 'obligacion_persona', on_delete=models.CASCADE) # persona duena de la obligacion
    portafolio                      = models.ForeignKey(Data_Portafolio, db_column = 'obligacion_portafolio', on_delete=models.CASCADE) # persona duena de la obligacion
    saldo_capital                   = models.FloatField(db_column = 'obligacion_saldocapital')
    saldo_interes_corriente         = models.FloatField(db_column = 'obligacion_saldointerescorriente')
    saldo_interes_mora              = models.FloatField(db_column = 'obligacion_saldointeresmora')
    seguro                          = models.FloatField(db_column = 'obligacion_seguro')
    comision                        = models.FloatField(db_column = 'obligacion_comision')
    saldo_total                     = models.FloatField(db_column = 'obligacion_saldototal')
    estado_obligacion               = models.ForeignKey(DataEstadoobligacion, db_column = 'obligacion_estadoobligacion', on_delete=models.CASCADE)
    variable1                       = models.CharField(db_column = 'obligacion_variable1', max_length = 200,  blank=True, null=True)
    variable1_descripcion           = models.CharField(db_column = 'obligacion_variable1_descripcion', max_length = 200,  blank=True, null=True)
    variable2                       = models.CharField(db_column = 'obligacion_variable2', max_length = 200,  blank=True, null=True)
    variable2_descripcion           = models.CharField(db_column = 'obligacion_variable2_descripcion', max_length = 200,  blank=True, null=True)
    variable3                       = models.CharField(db_column = 'obligacion_variable3', max_length = 200,  blank=True, null=True)
    variable3_descripcion           = models.CharField(db_column = 'obligacion_variable3_descripcion', max_length = 200,  blank=True, null=True)
    variable4                       = models.CharField(db_column = 'obligacion_variable4', max_length = 200,  blank=True, null=True)
    variable4_descripcion           = models.CharField(db_column = 'obligacion_variable4_descripcion', max_length = 200,  blank=True, null=True)
    variable5                       = models.CharField(db_column = 'obligacion_variable5', max_length = 200,  blank=True, null=True)
    variable5_descripcion           = models.CharField(db_column = 'obligacion_variable5_descripcion', max_length = 200,  blank=True, null=True)
    variable6                       = models.CharField(db_column = 'obligacion_variable6', max_length = 200,  blank=True, null=True)
    variable6_descripcion           = models.CharField(db_column = 'obligacion_variable6_descripcion', max_length = 200,  blank=True, null=True)
    variable7                       = models.CharField(db_column = 'obligacion_variable7', max_length = 200,  blank=True, null=True)
    variable7_descripcion           = models.CharField(db_column = 'obligacion_variable7_descripcion', max_length = 200,  blank=True, null=True)
    variable8                       = models.CharField(db_column = 'obligacion_variable8', max_length = 200,  blank=True, null=True)
    variable8_descripcion           = models.CharField(db_column = 'obligacion_variable8_descripcion', max_length = 200,  blank=True, null=True)
    variable9                       = models.CharField(db_column = 'obligacion_variable9', max_length = 200,  blank=True, null=True)
    variable9_descripcion           = models.CharField(db_column = 'obligacion_variable9_descripcion', max_length = 200,  blank=True, null=True)
    variable10                      = models.CharField(db_column = 'obligacion_variable10', max_length = 200,  blank=True, null=True)
    variable10_descripcion          = models.CharField(db_column = 'obligacion_variable10_descripcion', max_length = 200,  blank=True, null=True)
    variable11                      = models.CharField(db_column = 'obligacion_variable11', max_length = 200,  blank=True, null=True)
    variable11_descripcion          = models.CharField(db_column = 'obligacion_variable11_descripcion', max_length = 200,  blank=True, null=True)
    variable12                      = models.CharField(db_column = 'obligacion_variable12', max_length = 200,  blank=True, null=True)
    variable12_descripcion          = models.CharField(db_column = 'obligacion_variable12_descripcion', max_length = 200,  blank=True, null=True)
    variable13                      = models.CharField(db_column = 'obligacion_variable13', max_length = 200,  blank=True, null=True)
    variable13_descripcion          = models.CharField(db_column = 'obligacion_variable13_descripcion', max_length = 200,  blank=True, null=True)
    variable14                      = models.CharField(db_column = 'obligacion_variable14', max_length = 200,  blank=True, null=True)
    variable14_descripcion          = models.CharField(db_column = 'obligacion_variable14_descripcion', max_length = 200,  blank=True, null=True)
    variable15                      = models.CharField(db_column = 'obligacion_variable15', max_length = 200,  blank=True, null=True)
    variable15_descripcion          = models.CharField(db_column = 'obligacion_variable15_descripcion', max_length = 200,  blank=True, null=True)
    variable16                      = models.CharField(db_column = 'obligacion_variable16', max_length = 200,  blank=True, null=True)
    variable16_descripcion          = models.CharField(db_column = 'obligacion_variable16_descripcion', max_length = 200,  blank=True, null=True)
    variable17                      = models.CharField(db_column = 'obligacion_variable17', max_length = 200,  blank=True, null=True)
    variable17_descripcion          = models.CharField(db_column = 'obligacion_variable17_descripcion', max_length = 200,  blank=True, null=True)
    variable18                      = models.CharField(db_column = 'obligacion_variable18', max_length = 200,  blank=True, null=True)
    variable18_descripcion          = models.CharField(db_column = 'obligacion_variable18_descripcion', max_length = 200,  blank=True, null=True)
    variable19                      = models.CharField(db_column = 'obligacion_variable19', max_length = 200,  blank=True, null=True)
    variable19_descripcion          = models.CharField(db_column = 'obligacion_variable19_descripcion', max_length = 200,  blank=True, null=True)
    variable20                      = models.CharField(db_column = 'obligacion_variable20', max_length = 200,  blank=True, null=True)
    variable20_descripcion          = models.CharField(db_column = 'obligacion_variable20_descripcion', max_length = 200,  blank=True, null=True)
    variable21                      = models.CharField(db_column = 'obligacion_variable21', max_length = 200,  blank=True, null=True)
    variable21_descripcion          = models.CharField(db_column = 'obligacion_variable21_descripcion', max_length = 200,  blank=True, null=True)
    variable22                      = models.CharField(db_column = 'obligacion_variable22', max_length = 200,  blank=True, null=True)
    variable22_descripcion          = models.CharField(db_column = 'obligacion_variable22_descripcion', max_length = 200,  blank=True, null=True)
    variable23                      = models.CharField(db_column = 'obligacion_variable23', max_length = 200,  blank=True, null=True)
    variable23_descripcion          = models.CharField(db_column = 'obligacion_variable23_descripcion', max_length = 200,  blank=True, null=True)
    variable24                      = models.CharField(db_column = 'obligacion_variable24', max_length = 200,  blank=True, null=True)
    variable24_descripcion          = models.CharField(db_column = 'obligacion_variable24_descripcion', max_length = 200,  blank=True, null=True)
    variable25                      = models.CharField(db_column = 'obligacion_variable25', max_length = 200,  blank=True, null=True)
    variable25_descripcion          = models.CharField(db_column = 'obligacion_variable25_descripcion', max_length = 200,  blank=True, null=True)
    variable26                      = models.CharField(db_column = 'obligacion_variable26', max_length = 200,  blank=True, null=True)
    variable26_descripcion          = models.CharField(db_column = 'obligacion_variable26_descripcion', max_length = 200,  blank=True, null=True)
    variable27                      = models.CharField(db_column = 'obligacion_variable27', max_length = 200,  blank=True, null=True)
    variable27_descripcion          = models.CharField(db_column = 'obligacion_variable27_descripcion', max_length = 200,  blank=True, null=True)
    variable28                      = models.CharField(db_column = 'obligacion_variable28', max_length = 200,  blank=True, null=True)
    variable28_descripcion          = models.CharField(db_column = 'obligacion_variable28_descripcion', max_length = 200,  blank=True, null=True)
    variable29                      = models.CharField(db_column = 'obligacion_variable29', max_length = 200,  blank=True, null=True)
    variable29_descripcion          = models.CharField(db_column = 'obligacion_variable29_descripcion', max_length = 200,  blank=True, null=True)
    variable30                      = models.CharField(db_column = 'obligacion_variable30', max_length = 200,  blank=True, null=True)
    variable30_descripcion          = models.CharField(db_column = 'obligacion_variable30_descripcion', max_length = 200,  blank=True, null=True)


    def __unicode__(self):
        return u"%s" % (self.id)

    





class DataPortafolioarchivosStraus(models.Model):
    archivos_nombre = models.CharField(max_length=512, blank=True, null=True)
    archivos_observacion = models.TextField(blank=True, null=True)
    archivos_archivo = models.CharField(max_length=100)
    archivos_fechacreacion = models.DateTimeField(default = datetime.now)
    archivos_estado = models.BooleanField()
    archivos_portafolio = models.ForeignKey(DataPortafolio, models.DO_NOTHING, db_column='archivos_portafolio', blank=True, null=True)

    


class DataProducto(models.Model):
    producto_identificacion = models.CharField(max_length=30, blank=True, null=True)
    producto_persona_identifiacion = models.CharField(max_length=30, blank=True, null=True)
    producto_fechaasignacion = models.DateTimeField(blank=True, null=True)
    producto_persona = models.ForeignKey(DataPersona, models.DO_NOTHING, blank=True, null=True)
    producto_id = models.IntegerField(primary_key=True)

    


class DataTelefonos(models.Model):
    telefono_numero = models.CharField(max_length=20, blank=True, null=True)
    telefono_pais = models.CharField(max_length=50, blank=True, null=True)
    telefono_departamento = models.CharField(max_length=50, blank=True, null=True)
    telefono_ciudad = models.CharField(max_length=50, blank=True, null=True)
    telefono_persona = models.ForeignKey(DataPersona, models.DO_NOTHING,default='')
    telefono_id = models.IntegerField(primary_key=True)

    





class DataUbicacion(models.Model):
    ubicacion_direccion = models.CharField(max_length=200, blank=True, null=True)
    ubicacion_pais = models.CharField(max_length=50, blank=True, null=True)
    ubicacion_departamento = models.CharField(max_length=50, blank=True, null=True)
    ubicacion_ciudad = models.CharField(max_length=50, blank=True, null=True)
    ubicacion_localidad = models.CharField(max_length=50, blank=True, null=True)
    ubicacion_barrio = models.CharField(max_length=100, blank=True, null=True)
    ubicacion_persona = models.ForeignKey(DataPersona, models.DO_NOTHING,default='')
    ubicacion_id = models.IntegerField(primary_key=True)

    


class DataUbicacionEmpresa(models.Model):
    empresa_direccion = models.CharField(max_length=200, blank=True, null=True)
    empresa_pais = models.CharField(max_length=50, blank=True, null=True)
    empresa_departamento = models.CharField(max_length=50, blank=True, null=True)
    empresa_ciudad = models.CharField(max_length=50, blank=True, null=True)
    empresa_localidad = models.CharField(max_length=50, blank=True, null=True)
    empresa_barrio = models.CharField(max_length=100, blank=True, null=True)
    empresa_persona = models.ForeignKey(DataPersona, models.DO_NOTHING,default='')
    empresa_id = models.IntegerField(primary_key=True)
    empresa_nombre = models.CharField(max_length=200, blank=True, null=True)

    


empre = DataEmpresa.objects.create(
    empresa_direccion='Calle 93 # 45 - 16',
    empresa_nit='1020304050',
    empresa_nombre='Falabella',
    empresa_razonsocial='Falabella',
    empresa_logo='',
    empresa_responsablenombre='Falabella',
    empresa_responsabletelefono='1234567',
    empresa_telefono='1234567890',
    empresa_email='falabella@falabella.com.co'
)




DataEmpresa.objects.all()

clie = DataClientes.objects.create(
    cliente_empresa=empre.id,
    cliente_nombre='Falabella',
    cliente_direccion='Calle 93 # 45 - 16',
    cliente_logo='',
    cliente_color='orange',
    cliente_telefono='1234567',
)







CREATE TABLE strauss_asignacion.data_empresa_straus
(
    id integer NOT NULL,
    empresa_direccion character varying(512) COLLATE pg_catalog."default",
    empresa_nit character varying(512) COLLATE pg_catalog."default",
    empresa_nombre character varying(512) COLLATE pg_catalog."default",
    empresa_razonsocial character varying(512) COLLATE pg_catalog."default",
    empresa_logo character varying(512) COLLATE pg_catalog."default",
    empresa_responsablenombre character varying(512) COLLATE pg_catalog."default",
    empresa_responsabletelefono character varying(512) COLLATE pg_catalog."default",
    empresa_telefono character varying(512) COLLATE pg_catalog."default",
    empresa_email character varying(512) COLLATE pg_catalog."default",
    CONSTRAINT data_empresa_straus_pkey PRIMARY KEY (id)
)



CREATE TABLE strauss_asignacion.data_clientes_straus
(
    id integer NOT NULL,
    cliente_nombre character varying(512) COLLATE pg_catalog."default",
    cliente_direccion character varying(512) COLLATE pg_catalog."default",
    cliente_logo character varying(512) COLLATE pg_catalog."default",
    cliente_color character varying(512) COLLATE pg_catalog."default",
    cliente_telefono character varying(512) COLLATE pg_catalog."default",
    cliente_empresa integer NOT NULL,
        REFERENCES strauss_asignacion.data_empresa_straus (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        DEFERRABLE INITIALLY DEFERRED
)



CREATE TABLE strauss_asignacion.data_portafolio
(
    id integer NOT NULL,
    portafolio_nombre character varying(512) COLLATE pg_catalog."default",
    portafolio_contrapropuesta text COLLATE pg_catalog."default",
    portafolio_descuentos text COLLATE pg_catalog."default",
    portafolio_responsablecorreo character varying(512) COLLATE pg_catalog."default",
    portafolio_responsablenombre character varying(512) COLLATE pg_catalog."default",
    portafolio_responsabletelefono character varying(512) COLLATE pg_catalog."default",
    portafolio_fechacreacion character varying(512) COLLATE pg_catalog."default",
    portafolio_cliente integer NOT NULL
        REFERENCES strauss_asignacion.data_clientes_straus (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        DEFERRABLE INITIALLY DEFERRED
)



CREATE TABLE strauss.data_portafolioarchivos_straus
(
    id integer NOT NULL DEFAULT ,
    archivos_nombre character varying(512) COLLATE pg_catalog."default",
    archivos_observacion text COLLATE pg_catalog."default",
    archivos_archivo character varying(100) COLLATE pg_catalog."default" NOT NULL,
    archivos_fechacreacion character varying(512) COLLATE pg_catalog."default",
    archivos_estado boolean NOT NULL,
    archivos_portafolio integer,
    CONSTRAINT data_portafolioarchivos_straus_pkey PRIMARY KEY (id),
        REFERENCES strauss.data_portafolio (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        DEFERRABLE INITIALLY DEFERRED
)

