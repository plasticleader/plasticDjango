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


class DataArchivoCargue(models.Model):
    archivocarguenombreasignacion             = models.CharField(max_length=200)
    archivocarguecantidadcolumnasObligatorias = models.IntegerField()
    archivocarguenomcolumnas                  = models.CharField(max_length=2000)
    archivocargueestado                       = models.BooleanField(default=True)
    archivocarguefechacreacion                = models.DateTimeField(auto_now_add=True)
    #archivocarguearchivo                      = models.FileField(upload_to='static/upload/archivos', blank=False, null=True)
    archivocarguearchivotipocargue            = models.ForeignKey('DataTipoCargue', models.DO_NOTHING)
    #archivocargueusuario           = models.ForeignKey(User,on_delete=models.CASCADE, blank=False, null=False)

    class Meta:
        managed = True
        db_table = 'data_archivo_cargue'


class DataArchivoColumnas(models.Model):
    archivocolumnasarchivo                    = models.ForeignKey('DataArchivoCargue', models.DO_NOTHING)
    archivocolumnasarchivoplano               = models.FileField(upload_to='static/upload/archivos/columnas', blank=False, null=True)
    archivocolumnasestado                     = models.BooleanField(default=True)
    archivocolumnascolumnas                   = models.CharField(max_length=20000)

    class Meta:
        managed = True
        db_table = 'data_archivo_columnas'



class DataArchivoCargueProcesar(models.Model):
    archivocargueprocesarfechacreacion                = models.DateTimeField(auto_now_add=True)
    archivocargueprocesararchivo                      = models.FileField(upload_to='static/upload/archivos', blank=False, null=False)
    archivocargueprocesararchivotipocargue            = models.ForeignKey('DataTipoCargue', models.DO_NOTHING)
    archivocargueprocesararchivoobservacion           = models.CharField(max_length=20000)
    #archivocargueprocesarusuario                     = models.ForeignKey(User,on_delete=models.CASCADE, blank=False, null=False)
    archivocargueprocesarestado                       = models.BooleanField(default=False)

    class Meta:
        managed = True
        db_table = 'data_archivo_cargue_procesar'




class DataAsignacion(models.Model):
    asignacion_id = models.AutoField(primary_key=True)
    asignacion_nombre = models.CharField(max_length=100, blank=True, null=True)
    asignacion_fechacreacion = models.DateTimeField()
    asignacion_estado = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_asignacion'


class DataCorreoelectronico(models.Model):
    correoelectronico_correo = models.CharField(max_length=326, blank=True, null=True)
    correoelectronico_id = models.AutoField(primary_key=True)
    correoelectronico_persona = models.ForeignKey('DataPersona', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'data_correoelectronico'


class DataObligaciones(models.Model):
    obligacion_fechacreacion = models.DateTimeField()
    obligacion_fechacreacionobligacion = models.DateField()
    obligacion_fecha_vencimientoobligacion = models.DateField(blank=True, null=True)
    obligacion_saldocapital = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    obligacion_saldointerescorriente = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    obligacion_saldointeresmora = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    obligacion_saldototal = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    obligacion_variable1 = models.CharField(max_length=200, blank=True, null=True)
    obligacion_variable1_descripcion = models.CharField(max_length=200, blank=True, null=True)
    obligacion_variable2 = models.CharField(max_length=200, blank=True, null=True)
    obligacion_variable2_descripcion = models.CharField(max_length=200, blank=True, null=True)
    obligacion_variable3 = models.CharField(max_length=200, blank=True, null=True)
    obligacion_variable3_descripcion = models.CharField(max_length=200, blank=True, null=True)
    obligacion_variable4 = models.CharField(max_length=200, blank=True, null=True)
    obligacion_variable4_descripcion = models.CharField(max_length=200, blank=True, null=True)
    obligacion_variable5 = models.CharField(max_length=200, blank=True, null=True)
    obligacion_variable5_descripcion = models.CharField(max_length=200, blank=True, null=True)
    obligacion_variable6 = models.CharField(max_length=200, blank=True, null=True)
    obligacion_variable6_descripcion = models.CharField(max_length=200, blank=True, null=True)
    obligacion_variable7 = models.CharField(max_length=200, blank=True, null=True)
    obligacion_variable7_descripcion = models.CharField(max_length=200, blank=True, null=True)
    obligacion_variable8 = models.CharField(max_length=200, blank=True, null=True)
    obligacion_variable8_descripcion = models.CharField(max_length=200, blank=True, null=True)
    obligacion_variable9 = models.CharField(max_length=200, blank=True, null=True)
    obligacion_variable9_descripcion = models.CharField(max_length=200, blank=True, null=True)
    obligacion_variable10 = models.CharField(max_length=200, blank=True, null=True)
    obligacion_variable10_descripcion = models.CharField(max_length=200, blank=True, null=True)
    obligacion_variable11 = models.CharField(max_length=200, blank=True, null=True)
    obligacion_variable11_descripcion = models.CharField(max_length=200, blank=True, null=True)
    obligacion_variable12 = models.CharField(max_length=200, blank=True, null=True)
    obligacion_variable12_descripcion = models.CharField(max_length=200, blank=True, null=True)
    obligacion_variable13 = models.CharField(max_length=200, blank=True, null=True)
    obligacion_variable13_descripcion = models.CharField(max_length=200, blank=True, null=True)
    obligacion_variable14 = models.CharField(max_length=200, blank=True, null=True)
    obligacion_variable14_descripcion = models.CharField(max_length=200, blank=True, null=True)
    obligacion_variable15 = models.CharField(max_length=200, blank=True, null=True)
    obligacion_variable15_descripcion = models.CharField(max_length=200, blank=True, null=True)
    obligacion_variable16 = models.CharField(max_length=200, blank=True, null=True)
    obligacion_variable16_descripcion = models.CharField(max_length=200, blank=True, null=True)
    obligacion_variable17 = models.CharField(max_length=200, blank=True, null=True)
    obligacion_variable17_descripcion = models.CharField(max_length=200, blank=True, null=True)
    obligacion_variable18 = models.CharField(max_length=200, blank=True, null=True)
    obligacion_variable18_descripcion = models.CharField(max_length=200, blank=True, null=True)
    obligacion_variable19 = models.CharField(max_length=200, blank=True, null=True)
    obligacion_variable19_descripcion = models.CharField(max_length=200, blank=True, null=True)
    obligacion_variable20 = models.CharField(max_length=200, blank=True, null=True)
    obligacion_variable20_descripcion = models.CharField(max_length=200, blank=True, null=True)
    obligacion_variable21 = models.CharField(max_length=200, blank=True, null=True)
    obligacion_variable21_descripcion = models.CharField(max_length=200, blank=True, null=True)
    obligacion_variable22 = models.CharField(max_length=200, blank=True, null=True)
    obligacion_variable22_descripcion = models.CharField(max_length=200, blank=True, null=True)
    obligacion_variable23 = models.CharField(max_length=200, blank=True, null=True)
    obligacion_variable23_descripcion = models.CharField(max_length=200, blank=True, null=True)
    obligacion_variable24 = models.CharField(max_length=200, blank=True, null=True)
    obligacion_variable24_descripcion = models.CharField(max_length=200, blank=True, null=True)
    obligacion_variable25 = models.CharField(max_length=200, blank=True, null=True)
    obligacion_variable25_descripcion = models.CharField(max_length=200, blank=True, null=True)
    obligacion_variable26 = models.CharField(max_length=200, blank=True, null=True)
    obligacion_variable26_descripcion = models.CharField(max_length=200, blank=True, null=True)
    obligacion_variable27 = models.CharField(max_length=200, blank=True, null=True)
    obligacion_variable27_descripcion = models.CharField(max_length=200, blank=True, null=True)
    obligacion_variable28 = models.CharField(max_length=200, blank=True, null=True)
    obligacion_variable28_descripcion = models.CharField(max_length=200, blank=True, null=True)
    obligacion_variable29 = models.CharField(max_length=200, blank=True, null=True)
    obligacion_variable29_descripcion = models.CharField(max_length=200, blank=True, null=True)
    obligacion_variable30 = models.CharField(max_length=200, blank=True, null=True)
    obligacion_variable30_descripcion = models.CharField(max_length=200, blank=True, null=True)
    obligacion_estadoobligacion = models.CharField(max_length=10, blank=True, null=True)
    obligacion_persona = models.ForeignKey('DataPersona', models.DO_NOTHING, db_column='obligacion_persona')
    obligacion_tipoobligacion = models.CharField(max_length=30, blank=True, null=True)
    obligacion_producto = models.CharField(max_length=100, blank=True, null=True)
    obligacion_tipo_producto = models.CharField(max_length=50, blank=True, null=True)
    obligacion_seguro = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    obligacion_comision = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    obligacion_portafolio = models.CharField(max_length=100, blank=True, null=True)
    obligacion_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'data_obligaciones'


class DataPersona(models.Model):
    persona_fechacreacion = models.DateTimeField(blank=True, null=True)
    persona_identificacion = models.CharField(max_length=30)
    persona_nombre = models.CharField(max_length=300, blank=True, null=True)
    persona_tipoidentificacion = models.CharField(max_length=10, blank=True, null=True)
    persona_id = models.AutoField(primary_key=True)
    persona_asignacion = models.ForeignKey(DataAsignacion, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_persona'


class DataProducto(models.Model):
    producto_identificacion = models.CharField(max_length=30, blank=True, null=True)
    producto_persona_identifiacion = models.CharField(max_length=30, blank=True, null=True)
    producto_fechaasignacion = models.DateTimeField(blank=True, null=True)
    producto_persona = models.ForeignKey(DataPersona, models.DO_NOTHING, blank=True, null=True)
    producto_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'data_producto'


class DataTelefonos(models.Model):
    telefono_numero = models.CharField(max_length=20, blank=True, null=True)
    telefono_pais = models.CharField(max_length=50, blank=True, null=True)
    telefono_departamento = models.CharField(max_length=50, blank=True, null=True)
    telefono_ciudad = models.CharField(max_length=50, blank=True, null=True)
    telefono_persona = models.ForeignKey(DataPersona, models.DO_NOTHING)
    telefono_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'data_telefonos'



class DataTipoCargue(models.Model):
    tipocarguenombre = models.CharField(max_length=200, blank=True, null=True)
    tipocargueempresa = models.CharField(max_length=200, blank=True, null=True)
    tipocarguefechacreacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return u"%s" % (self.tipocarguenombre)


    class Meta:
        managed = True
        db_table = 'data_tipo_cargue'


class DataUbicacion(models.Model):
    ubicacion_direccion = models.CharField(max_length=200, blank=True, null=True)
    ubicacion_pais = models.CharField(max_length=50, blank=True, null=True)
    ubicacion_departamento = models.CharField(max_length=50, blank=True, null=True)
    ubicacion_ciudad = models.CharField(max_length=50, blank=True, null=True)
    ubicacion_localidad = models.CharField(max_length=50, blank=True, null=True)
    ubicacion_barrio = models.CharField(max_length=100, blank=True, null=True)
    ubicacion_persona = models.ForeignKey(DataPersona, models.DO_NOTHING)
    ubicacion_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'data_ubicacion'


class DataUbicacionEmpresa(models.Model):
    empresa_direccion = models.CharField(max_length=200, blank=True, null=True)
    empresa_pais = models.CharField(max_length=50, blank=True, null=True)
    empresa_departamento = models.CharField(max_length=50, blank=True, null=True)
    empresa_ciudad = models.CharField(max_length=50, blank=True, null=True)
    empresa_localidad = models.CharField(max_length=50, blank=True, null=True)
    empresa_barrio = models.CharField(max_length=100, blank=True, null=True)
    empresa_persona = models.ForeignKey(DataPersona, models.DO_NOTHING)
    empresa_id = models.AutoField(primary_key=True)
    empresa_nombre = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_ubicacion_empresa'





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
    empresa_fechacreacion = models.DateTimeField(default = datetime.now)


    # def __str__(self):
    #     return u"%s" % (self.empresa_nombre)

    class Meta:
        managed = True
        db_table = 'data_empresa_straus'


class DataClientesStraus(models.Model):
    cliente_empresa = models.ForeignKey(DataEmpresaStraus, db_column = 'cliente_empresa', on_delete=models.CASCADE)
    cliente_nombre = models.CharField(max_length=512, blank=True, null=True)
    cliente_direccion = models.CharField(max_length=512, blank=True, null=True)
    cliente_logo = models.CharField(max_length=512, blank=True, null=True)
    cliente_color = models.CharField(max_length=512, blank=True, null=True)
    cliente_telefono = models.CharField(max_length=512, blank=True, null=True)
    cliente_fechacreacion = models.DateTimeField(default = datetime.now)

    # def __str__(self):
    #     return u"%s" % (self.cliente_nombre)

    class Meta:
        managed = True
        db_table = 'data_clientes_straus'





class DataPortafolio(models.Model):
    portafolio_cliente = models.ForeignKey(DataClientesStraus, models.DO_NOTHING, db_column='portafolio_cliente', blank=True, null=True)
    portafolio_nombre = models.CharField(max_length=512, blank=True, null=True)
    portafolio_contrapropuesta = models.TextField(blank=True, null=True)
    portafolio_descuentos = models.TextField(blank=True, null=True)
    portafolio_responsablecorreo = models.CharField(max_length=512, blank=True, null=True)
    portafolio_responsablenombre = models.CharField(max_length=512, blank=True, null=True)
    portafolio_responsabletelefono = models.CharField(max_length=512, blank=True, null=True)
    portafolio_fechacreacion = models.DateTimeField(default = datetime.now)

    class Meta:
        managed = True
        db_table = 'data_portafolio'


class DataPortafolioarchivosStraus(models.Model):
    archivos_portafolio = models.ForeignKey(DataPortafolio, models.DO_NOTHING, db_column='archivos_portafolio', blank=True, null=True)
    archivos_nombre = models.CharField(max_length=512, blank=True, null=True)
    archivos_observacion = models.TextField(blank=True, null=True)
    # archivos_usuario = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='archivos_usuario', blank=True, null=True)
    archivos_archivo =models.FileField(db_column ='archivos_archivo',upload_to='static/upload/archivos', blank=False, null=False)
    archivos_fechacreacion = models.DateTimeField(default = datetime.now)
    archivos_estado = models.BooleanField(default=False)

    class Meta:
        managed = True
        db_table = 'data_portafolioarchivos_straus'