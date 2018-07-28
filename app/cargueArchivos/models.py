from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date, time, timedelta


class DataAsignacion(models.Model):
    asignacion_nombre                       = models.CharField(max_length=512, blank=True, null=True)
    asignacion_fechacreacion                = models.DateTimeField(default=datetime.now())
    asignacion_empresa					    = models.CharField(max_length=512, blank=True, null=True)
    asignacion_cliente                      = models.CharField(max_length=512, blank=True, null=True)
    asignacion_contrapropuesta              = models.CharField(max_length=512, blank=True, null=True)
    asignacion_descuentos                   = models.CharField(max_length=512, blank=True, null=True)
		


class DataPersonas(models.Model):
	persona_identificacion                 = models.CharField(max_length=512, blank=True, null=True)
	persona_nombre                         = models.CharField(max_length=512, blank=True, null=True)
	persona_tipoidentificacion             = models.CharField(max_length=512, blank=True, null=True)
	persona_asignacion                     = models.CharField(max_length=512, blank=True, null=True)



class DataAsignacionarchivosStraus(models.Model):
    archivos_nombre                        = models.CharField(max_length=512, blank=True, null=True)
    archivos_observacion                   = models.TextField(blank=True, null=True)
    archivos_archivo                       = models.FileField(upload_to='archivos/clientes',blank=True, null=True)
    archivos_fechacreacion                 = models.DateTimeField(default=datetime.now())
    archivos_estado                        = models.BooleanField(default=False)
    archivos_asignacion                    = models.ForeignKey(DataAsignacion,on_delete=models.CASCADE,blank=True, null=True)



class DataarchivosStraus(models.Model):
    archivos_archivo                       = models.FileField(upload_to='archivos/clientes/temporal',blank=True, null=True)
    archivos_fechacreacion                 = models.DateTimeField(default=datetime.now())
    archivos_asignacion                    = models.ForeignKey(DataAsignacion,on_delete=models.CASCADE)



class DataProducto(models.Model):
    producto_identificacion               = models.CharField(max_length=30, blank=True, null=True)
    producto_persona_identifiacion        = models.CharField(max_length=30, blank=True, null=True)
    producto_fechaasignacion              = models.DateTimeField(default=datetime.now())
    producto_persona                      = models.CharField(max_length=30, blank=True, null=True)

    


class DataTelefonos(models.Model):
    telefono_numero                       = models.CharField(max_length=20,blank=True,null=True)
    telefono_pais                         = models.CharField(max_length=50,blank=True,null=True)
    telefono_departamento                 = models.CharField(max_length=50,blank=True,null=True)
    telefono_ciudad                       = models.CharField(max_length=50,blank=True,null=True)
    telefono_persona                      = models.CharField(max_length=30, blank=True, null=True)

    


class DataCorreoelectronico(models.Model):
    correoelectronico_correo              = models.CharField(max_length=326,blank=True,null=True)
    correoelectronico_persona             = models.CharField(max_length=30, blank=True, null=True)




class DataUbicacion(models.Model):
    ubicacion_direccion                   = models.CharField(max_length=200, blank=True, null=True)
    ubicacion_pais                        = models.CharField(max_length=50, blank=True, null=True)
    ubicacion_departamento                = models.CharField(max_length=50, blank=True, null=True)
    ubicacion_ciudad                      = models.CharField(max_length=50, blank=True, null=True)
    ubicacion_localidad                   = models.CharField(max_length=50, blank=True, null=True)
    ubicacion_barrio                      = models.CharField(max_length=100, blank=True, null=True)
    ubicacion_persona                     = models.CharField(max_length=30, blank=True, null=True)

    



class DataUbicacionEmpresa(models.Model):
    empresa_direccion                    = models.CharField(max_length=200, blank=True, null=True)
    empresa_pais                         = models.CharField(max_length=50, blank=True, null=True)
    empresa_departamento                 = models.CharField(max_length=50, blank=True, null=True)
    empresa_ciudad                       = models.CharField(max_length=50, blank=True, null=True)
    empresa_localidad                    = models.CharField(max_length=50, blank=True, null=True)
    empresa_barrio                       = models.CharField(max_length=100, blank=True, null=True)
    empresa_persona                      = models.CharField(max_length=30, blank=True, null=True)
    empresa_nombre                       = models.CharField(max_length=200, blank=True, null=True)


 
 
class DataUbicacionInfoOrigen(models.Model):
    ubicaorigen_cliente					 = models.CharField(max_length=512, blank=True, null=True)
    ubicaorigen_persona                  = models.CharField(max_length=30, blank=True, null=True)
    ubicaorigen_telefono                 = models.ForeignKey(DataTelefonos,on_delete=models.CASCADE,blank=True,null=True)
    ubicaorigen_email                    = models.ForeignKey(DataCorreoelectronico,on_delete=models.CASCADE,blank=True,null=True)
    ubicaorigen_fechaacreacion           = models.DateTimeField(default=datetime.now())
    ubicaorigen_observacion              = models.CharField(max_length=100,blank=True,null=True)
    ubicaorigen_usuario                  = models.ForeignKey(User,on_delete=models.CASCADE)



class DataObligacion(models.Model):
    obligacionpersona                      = models.CharField(max_length=30, blank=True, null=True)  
    obligacionportafolio                   = models.CharField(max_length=30, blank=True, null=True)
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



