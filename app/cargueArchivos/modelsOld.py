# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date, time, timedelta




class DataClientesStraus(models.Model):
    cliente_nombre                         = models.CharField(max_length=512, blank=True, null=True)
    cliente_direccion                      = models.CharField(max_length=512, blank=True, null=True)
    cliente_logo                           = models.CharField(max_length=512, blank=True, null=True)
    cliente_color                          = models.CharField(max_length=512, blank=True, null=True)
    cliente_telefono                       = models.CharField(max_length=512, blank=True, null=True)
    cliente_empresa                        = models.ForeignKey('DataEmpresaStraus', models.DO_NOTHING, db_column='cliente_empresa')

    

class DataEmpresaStraus(models.Model):
    empresa_direccion                      = models.CharField(max_length=512, blank=True, null=True)
    empresa_nit                            = models.CharField(max_length=512, blank=True, null=True)
    empresa_nombre                         = models.CharField(max_length=512, blank=True, null=True)
    empresa_razonsocial                    = models.CharField(max_length=512, blank=True, null=True)
    empresa_logo                           = models.CharField(max_length=512, blank=True, null=True)
    empresa_responsablenombre              = models.CharField(max_length=512, blank=True, null=True)
    empresa_responsabletelefono            = models.CharField(max_length=512, blank=True, null=True)
    empresa_telefono                       = models.CharField(max_length=512, blank=True, null=True)
    empresa_email                          = models.CharField(max_length=512, blank=True, null=True)

    

class DataPortafolio(models.Model):
    portafolio_nombre                      = models.CharField(max_length=512, blank=True, null=True)
    portafolio_contrapropuesta             = models.TextField(blank=True, null=True)
    portafolio_descuentos                  = models.TextField(blank=True, null=True)
    portafolio_responsablecorreo           = models.CharField(max_length=512, blank=True, null=True)
    portafolio_responsablenombre           = models.CharField(max_length=512, blank=True, null=True)
    portafolio_responsabletelefono         = models.CharField(max_length=512, blank=True, null=True)
    portafolio_cantObligaciones            = models.CharField(max_length=512, blank=True, null=True)
    portafolio_cantRegistros               = models.CharField(max_length=512, blank=True, null=True)
    portafolio_cantTokens                  = models.CharField(max_length=512, blank=True, null=True)
    portafolio_fechacreacion               = models.DateTimeField(default = datetime.now())
    portafolio_fechaactualizacion          = models.DateTimeField(default = datetime.now())
    portafolio_cliente                     = models.ForeignKey(DataClientesStraus, models.DO_NOTHING, db_column='portafolio_cliente')
    portafolio_usuario                     = models.ForeignKey(User, db_column = 'portafolio_usuario', on_delete=models.CASCADE)

    

class DataPortafolioarchivosStraus(models.Model):
    archivos_nombre                        = models.CharField(max_length=512, blank=True, null=True)
    archivos_observacion                   = models.TextField(blank=True, null=True)
    archivos_archivo                       = models.FileField(upload_to='archivos/clientes',blank=True, null=True)
    archivos_fechacreacion                 = models.DateTimeField(default=datetime.now())
    archivos_estado                        = models.BooleanField(default=False)
    archivos_portafolio                    = models.ForeignKey(DataPortafolio, models.DO_NOTHING, db_column='archivos_portafolio', blank=True, null=True)


class DataarchivosStraus(models.Model):
    archivos_archivo                       = models.FileField(upload_to='archivos/clientes/temporal',blank=True, null=True)
    archivos_fechacreacion                 = models.DateTimeField(default=datetime.now())
    archivos_portafolio                    = models.ForeignKey(DataPortafolio, models.DO_NOTHING, db_column='archivos_portafolio', blank=True, null=True)



class DataPersona(models.Model):
    persona_fechacreacion                  = models.DateTimeField(default = datetime.now())
    persona_identificacion                 = models.CharField(max_length=30)
    persona_nombre                         = models.CharField(max_length=300, blank=True, null=True)
    persona_tipoidentificacion             = models.CharField(max_length=10, blank=True, null=True)


class DataEstadoobligacion(models.Model): 
    estadoobligaciondescripcion            = models.CharField(max_length=100)
    estadoobligacionestado                 = models.BooleanField(default=True)

class DataTipoobligacion(models.Model): 
    tipoobligaciondescripcion              = models.CharField(max_length=100)
    tipoobligacionestado                   = models.BooleanField(default=True)




class DataObligacion(models.Model):
    obligacionpersona                      = models.ForeignKey(DataPersona, models.DO_NOTHING,blank=False, null=False)  
    obligacionportafolio                   = models.ForeignKey(DataPortafolio, models.DO_NOTHING, blank=False, null=False)      
    obligacionestado_obligacion            = models.ForeignKey(DataEstadoobligacion, models.DO_NOTHING,blank=False, null=False) 
    obligacionsaldo_capital                = models.FloatField(default=0)
    obligacionseguro                       = models.FloatField(default=0)
    obligacioncomision                     = models.FloatField(default=0)
    obligacionsaldo_interes_corriente      = models.FloatField(default=0)
    obligacionsaldo_interes_mora           = models.FloatField(default=0)
    obligacionsaldo_total                  = models.FloatField(default=0)
    obligacionfechacreacion                = models.DateTimeField(default=datetime.now())
    obligacionfecha_creacion_obligacion    = models.CharField(max_length=300,blank=True,null=True)
    obligacionfecha_vencimiento_obligacion = models.CharField(max_length=300,blank=True,null=True)
    obligacionproducto                     = models.CharField(max_length=300,blank=True,null=True)
    obligaciontipo_obligacion              = models.CharField(max_length=200,blank=True,null=True)
    obligaciontipo_prducto                 = models.CharField(max_length=200,blank=True,null=True)
    variable1                              = models.CharField(max_length=200,blank=True,null=True)
    variable1_descripcion                  = models.CharField(max_length=200,blank=True,null=True)
    variable2                              = models.CharField(max_length=200,blank=True,null=True)
    variable2_descripcion                  = models.CharField(max_length=200,blank=True,null=True)
    variable3                              = models.CharField(max_length=200,blank=True,null=True)
    variable3_descripcion                  = models.CharField(max_length=200,blank=True,null=True)
    variable4                              = models.CharField(max_length=200,blank=True,null=True)
    variable4_descripcion                  = models.CharField(max_length=200,blank=True,null=True)
    variable5                              = models.CharField(max_length=200,blank=True,null=True)
    variable5_descripcion                  = models.CharField(max_length=200,blank=True,null=True)
    variable6                              = models.CharField(max_length=200,blank=True,null=True)
    variable6_descripcion                  = models.CharField(max_length=200,blank=True,null=True)
    variable7                              = models.CharField(max_length=200,blank=True,null=True)
    variable7_descripcion                  = models.CharField(max_length=200,blank=True,null=True)
    variable8                              = models.CharField(max_length=200,blank=True,null=True)
    variable8_descripcion                  = models.CharField(max_length=200,blank=True,null=True)
    variable9                              = models.CharField(max_length=200,blank=True,null=True)
    variable9_descripcion                  = models.CharField(max_length=200,blank=True,null=True)
    variable10                             = models.CharField(max_length=200,blank=True,null=True)
    variable10_descripcion                 = models.CharField(max_length=200,blank=True,null=True)
    variable11                             = models.CharField(max_length=200,blank=True,null=True)
    variable11_descripcion                 = models.CharField(max_length=200,blank=True,null=True)
    variable12                             = models.CharField(max_length=200,blank=True,null=True)
    variable12_descripcion                 = models.CharField(max_length=200,blank=True,null=True)
    variable13                             = models.CharField(max_length=200,blank=True,null=True)
    variable13_descripcion                 = models.CharField(max_length=200,blank=True,null=True)
    variable14                             = models.CharField(max_length=200,blank=True,null=True)
    variable14_descripcion                 = models.CharField(max_length=200,blank=True,null=True)
    variable15                             = models.CharField(max_length=200,blank=True,null=True)
    variable15_descripcion                 = models.CharField(max_length=200,blank=True,null=True)
    variable16                             = models.CharField(max_length=200,blank=True,null=True)
    variable16_descripcion                 = models.CharField(max_length=200,blank=True,null=True)
    variable17                             = models.CharField(max_length=200,blank=True,null=True)
    variable17_descripcion                 = models.CharField(max_length=200,blank=True,null=True)
    variable18                             = models.CharField(max_length=200,blank=True,null=True)
    variable18_descripcion                 = models.CharField(max_length=200,blank=True,null=True)
    variable19                             = models.CharField(max_length=200,blank=True,null=True)
    variable19_descripcion                 = models.CharField(max_length=200,blank=True,null=True)
    variable20                             = models.CharField(max_length=200,blank=True,null=True)
    variable20_descripcion                 = models.CharField(max_length=200,blank=True,null=True)
    variable21                             = models.CharField(max_length=200,blank=True,null=True)
    variable21_descripcion                 = models.CharField(max_length=200,blank=True,null=True)
    variable22                             = models.CharField(max_length=200,blank=True,null=True)
    variable22_descripcion                 = models.CharField(max_length=200,blank=True,null=True)
    variable23                             = models.CharField(max_length=200,blank=True,null=True)
    variable23_descripcion                 = models.CharField(max_length=200,blank=True,null=True)
    variable24                             = models.CharField(max_length=200,blank=True,null=True)
    variable24_descripcion                 = models.CharField(max_length=200,blank=True,null=True)
    variable25                             = models.CharField(max_length=200,blank=True,null=True)
    variable25_descripcion                 = models.CharField(max_length=200,blank=True,null=True)
    variable26                             = models.CharField(max_length=200,blank=True,null=True)
    variable26_descripcion                 = models.CharField(max_length=200,blank=True,null=True)
    variable27                             = models.CharField(max_length=200,blank=True,null=True)
    variable27_descripcion                 = models.CharField(max_length=200,blank=True,null=True)
    variable28                             = models.CharField(max_length=200,blank=True,null=True)
    variable28_descripcion                 = models.CharField(max_length=200,blank=True,null=True)
    variable29                             = models.CharField(max_length=200,blank=True,null=True)
    variable29_descripcion                 = models.CharField(max_length=200,blank=True,null=True)
    variable30                             = models.CharField(max_length=200,blank=True,null=True)
    variable30_descripcion                 = models.CharField(max_length=200,blank=True,null=True)


    

    

class DataProducto(models.Model):
    producto_identificacion               = models.CharField(max_length=30, blank=True, null=True)
    producto_persona_identifiacion        = models.CharField(max_length=30, blank=True, null=True)
    producto_fechaasignacion              = models.DateTimeField(default=datetime.now())
    producto_persona                      = models.ForeignKey(DataPersona, models.DO_NOTHING, blank=True, null=True)

    


class DataTelefonos(models.Model):
    telefono_numero                       = models.CharField(max_length=20,blank=True,null=True)
    telefono_pais                         = models.CharField(max_length=50,blank=True,null=True)
    telefono_departamento                 = models.CharField(max_length=50,blank=True,null=True)
    telefono_ciudad                       = models.CharField(max_length=50,blank=True,null=True)
    telefono_tipo                         = models.CharField(max_length=50,blank=True,null=True)
    telefono_persona                      = models.ForeignKey(DataPersona, models.DO_NOTHING)

    


class DataCorreoelectronico(models.Model):
    correoelectronico_correo              = models.CharField(max_length=326,blank=True,null=True)
    correoelectronico_persona             = models.ForeignKey(DataPersona, models.DO_NOTHING)




class DataUbicacion(models.Model):
    ubicacion_direccion                   = models.CharField(max_length=200, blank=True, null=True)
    ubicacion_pais                        = models.CharField(max_length=50, blank=True, null=True)
    ubicacion_departamento                = models.CharField(max_length=50, blank=True, null=True)
    ubicacion_ciudad                      = models.CharField(max_length=50, blank=True, null=True)
    ubicacion_localidad                   = models.CharField(max_length=50, blank=True, null=True)
    ubicacion_barrio                      = models.CharField(max_length=100, blank=True, null=True)
    ubicacion_persona                     = models.ForeignKey(DataPersona, models.DO_NOTHING)

    



class DataUbicacionEmpresa(models.Model):
    empresa_direccion                    = models.CharField(max_length=200, blank=True, null=True)
    empresa_pais                         = models.CharField(max_length=50, blank=True, null=True)
    empresa_departamento                 = models.CharField(max_length=50, blank=True, null=True)
    empresa_ciudad                       = models.CharField(max_length=50, blank=True, null=True)
    empresa_localidad                    = models.CharField(max_length=50, blank=True, null=True)
    empresa_barrio                       = models.CharField(max_length=100, blank=True, null=True)
    empresa_persona                      = models.ForeignKey(DataPersona, models.DO_NOTHING)
    empresa_nombre                       = models.CharField(max_length=200, blank=True, null=True)


 
 
class DataUbicacionInfoOrigen(models.Model):
    ubicaorigen_empresa                  = models.ForeignKey(DataEmpresaStraus, models.DO_NOTHING)
    ubicaorigen_persona                  = models.ForeignKey(DataPersona, models.DO_NOTHING)
    ubicaorigen_telefono                 = models.ForeignKey(DataTelefonos, models.DO_NOTHING,blank=True,null=True)
    ubicaorigen_email                    = models.ForeignKey(DataCorreoelectronico, models.DO_NOTHING,blank=True,null=True)
    ubicaorigen_fechaacreacion           = models.DateTimeField(default=datetime.now())
    ubicaorigen_observacion              = models.CharField(max_length=100,blank=True,null=True)
    ubicaorigen_usuario                  = models.ForeignKey(User, db_column = 'ubicacion_usuario', on_delete=models.CASCADE)



    

class DataPersonaPortafolioToken(models.Model):
    perportatoken_estado                = models.BooleanField(default=True)
    perportatoken_fechacreacion         = models.DateTimeField(auto_now_add=True)
    perportatoken_persona               = models.ForeignKey(DataPersona,on_delete=models.CASCADE)
    perportatoken_portafolio            = models.ForeignKey(DataPortafolio,on_delete=models.CASCADE)
    perportatoken_token                 = models.CharField(max_length=20)

    

class DataTrazabilidadCampanasArchivos(models.Model):
    traza_usuario                       = models.ForeignKey(User,on_delete=models.CASCADE)
    traza_portafolio                    = models.ForeignKey(DataPortafolio,on_delete=models.CASCADE)
    traza_cantRegisBefore               = models.CharField(max_length=20)
    traza_cantRegisLatest               = models.CharField(max_length=20)
    traza_cantObliBefore                = models.CharField(max_length=512, blank=True, null=True)
    traza_cantObliLatest                = models.CharField(max_length=512, blank=True, null=True)
    traza_cantTokBefore                 = models.CharField(max_length=512, blank=True, null=True)
    traza_cantTokLatest                 = models.CharField(max_length=512, blank=True, null=True)
    traza_fecactBefore                  = models.CharField(max_length=512, blank=True, null=True,default=datetime.now())
    traza_fecactLatest                  = models.DateTimeField(default=datetime.now())
    traza_fechacreacion                 = models.DateTimeField(default=datetime.now())
    
        