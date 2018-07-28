# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User


class AuthGroup(models.Model):
    name = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'
        unique_together = (('name', 'name'),)


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission', 'group', 'permission'), ('id', 'id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename', 'content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'
        unique_together = (('username', 'username'),)


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('id', 'id'), ('user', 'group', 'user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('id', 'id'), ('user', 'permission', 'user', 'permission'),)


class DataAcuerdopago(models.Model):
    cobro_fecha = models.CharField(max_length=512, blank=True, null=True)
    cobro_inicio = models.CharField(max_length=512, blank=True, null=True)
    cobro_proximo = models.CharField(max_length=512, blank=True, null=True)
    cobro_vencimiento = models.CharField(max_length=512, blank=True, null=True)
    cuotas_a_cobrar = models.CharField(max_length=512, blank=True, null=True)
    cuotas_atrasadas = models.CharField(max_length=512, blank=True, null=True)
    cuotas_pactadas = models.CharField(max_length=512, blank=True, null=True)
    cuotas_pagadas = models.CharField(max_length=512, blank=True, null=True)
    cuotas_parciales = models.CharField(max_length=512, blank=True, null=True)
    estado = models.CharField(max_length=1, blank=True, null=True)
    fecha_ultimo_pago = models.CharField(max_length=512, blank=True, null=True)
    nota = models.CharField(max_length=512, blank=True, null=True)
    saldo_anterior = models.CharField(max_length=512, blank=True, null=True)
    saldo_capital = models.CharField(max_length=512, blank=True, null=True)
    saldo_cuota_parcial = models.CharField(max_length=512, blank=True, null=True)
    saldo_total = models.CharField(max_length=512, blank=True, null=True)
    valor_cuota = models.CharField(max_length=512, blank=True, null=True)
    valor_acuerdo = models.CharField(max_length=512, blank=True, null=True)
    valor_predeterminado = models.CharField(max_length=512, blank=True, null=True)
    valor_ultimo_pago = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_acuerdopago'


class DataArchivos(models.Model):
    archivos_nombre = models.CharField(max_length=512, blank=True, null=True)
    archivos_archivo = models.CharField(max_length=512, blank=True, null=True)
    archivos_observacion = models.TextField(blank=True, null=True)
    archivos_fechacreacion = models.CharField(max_length=512, blank=True, null=True)
    archivos_estado = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'data_archivos'


class DataArchivosprocesados(models.Model):
    archivos_sin_proceso = models.ForeignKey(DataArchivos, models.DO_NOTHING, db_column='archivos_sin_proceso', blank=True, null=True)
    archivos_nombre = models.CharField(max_length=512, blank=True, null=True)
    archivos_archivo = models.CharField(max_length=512, blank=True, null=True)
    archivos_fechacreacion = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'data_archivosprocesados'



class DataEmpresa(models.Model):
    # empresa_ciudad = models.CharField(max_length=512, blank=True, null=True)
    empresa_direccion = models.CharField(max_length=512, blank=True, null=True)
    empresa_nit = models.CharField(max_length=512, blank=True, null=True)
    empresa_nombre = models.CharField(max_length=512, blank=True, null=True)
    empresa_razonsocial = models.CharField(max_length=512, blank=True, null=True)
    empresa_logo = models.CharField(max_length=512, blank=True, null=True)
    empresa_responsablenombre = models.CharField(max_length=512, blank=True, null=True)
    empresa_responsabletelefono = models.CharField(max_length=512, blank=True, null=True)
    empresa_telefono = models.CharField(max_length=512, blank=True, null=True)
    empresa_email = models.CharField(max_length=512, blank=True, null=True)
    empresa_fechacreacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return u"%s" % (self.empresa_nombre)

    class Meta:
        managed = True
        db_table = 'data_empresa'



class DataClientes(models.Model):
    cliente_empresa = models.ForeignKey(DataEmpresa, models.DO_NOTHING, db_column='cliente_empresa', blank=True, null=True)
    cliente_nombre = models.CharField(max_length=512, blank=True, null=True)
    cliente_direccion = models.CharField(max_length=512, blank=True, null=True)
    cliente_logo = models.CharField(max_length=512, blank=True, null=True)
    cliente_color = models.CharField(max_length=512, blank=True, null=True)
    cliente_telefono = models.CharField(max_length=512, blank=True, null=True)
    cliente_fechacreacion = models.CharField(max_length=512, blank=True, null=True)


    def __str__(self):
        return u"%s" % (self.cliente_nombre)


    class Meta:
        managed = True
        db_table = 'data_clientes'


class DataCorreoelectronico(models.Model):
    correoelectronico_correo = models.CharField(max_length=326, blank=True, null=True)
    correoelectronico_id = models.IntegerField(primary_key=True)
    correoelectronico_persona = models.ForeignKey('DataPersona', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'data_correoelectronico'




class DataEstadoobligacion(models.Model):
    estadoobligacion_descripcion = models.CharField(max_length=512, blank=True, null=True)
    estadoobligacion_fechacreacion = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_estadoobligacion'


class DataInteraccion(models.Model):
    interaccion_fecha_interaccion = models.DateField(blank=True, null=True)
    interaccion_id = models.AutoField(primary_key=True)
    interaccion_intento = models.CharField(max_length=5, blank=True, null=True)
    interaccion_email = models.TextField(blank=True, null=True)
    interaccion_telefono = models.CharField(max_length=20, blank=True, null=True)
    interaccion_empresa = models.CharField(max_length=100, blank=True, null=True)
    interaccion_hora_inicio = models.TimeField(blank=True, null=True)
    interaccion_hora_fin = models.TimeField(blank=True, null=True)
    interaccion_identificacion = models.CharField(max_length=60, blank=True, null=True)
    interaccion_resultado = models.CharField(max_length=100, blank=True, null=True)
    interaccion_id_campana = models.CharField(max_length=50, blank=True, null=True)
    interaccion_accion = models.CharField(max_length=100, blank=True, null=True)
    interaccion_cliente = models.CharField(max_length=50, blank=True, null=True)
    interaccion_nombre = models.CharField(max_length=255, blank=True, null=True)
    interaccion_canal = models.CharField(max_length=20, blank=True, null=True)
    interaccion_identificacion_ktl = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_interaccion'


class DataInteraccionpersona(models.Model):
    interaccionpersona_fechacreacion = models.CharField(max_length=512, blank=True, null=True)
    interaccionpersona_fechainteraccion = models.CharField(max_length=512, blank=True, null=True)
    interaccionpersona_nota = models.CharField(max_length=512, blank=True, null=True)
    interaccionpersona_obligacion = models.ForeignKey('DataObligacion', models.DO_NOTHING, db_column='interaccionpersona_obligacion', blank=True, null=True)
    interaccionpersona_persona = models.ForeignKey('DataPersonas', models.DO_NOTHING, db_column='interaccionpersona_persona', blank=True, null=True)
    interaccionpersona_personaportafoliotoken = models.CharField(max_length=512, blank=True, null=True)
    interaccionpersona_tipointeraccion = models.ForeignKey('DataTipointeraccion', models.DO_NOTHING, db_column='interaccionpersona_tipointeraccion', blank=True, null=True)
    interaccionpersonallamada = models.ForeignKey('DataInteraccionpersonallamada', models.DO_NOTHING, db_column='interaccionpersonallamada', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_interaccionpersona'


class DataInteraccionpersonallamada(models.Model):
    interaccionpersonallamada_horainicio = models.CharField(max_length=512, blank=True, null=True)
    interaccionpersonallamada_horacontestacion = models.CharField(max_length=512, blank=True, null=True)
    interaccionpersonallamada_horafin = models.CharField(max_length=512, blank=True, null=True)
    interaccionpersonallamada_intento = models.CharField(max_length=512, blank=True, null=True)
    interaccionpersonallamada_idresultado = models.CharField(max_length=512, blank=True, null=True)
    interaccionpersonallamada_efecto = models.CharField(max_length=512, blank=True, null=True)
    interaccionpersonallamada_idcampana = models.CharField(max_length=512, blank=True, null=True)
    interaccionpersonallamada_campana = models.CharField(max_length=512, blank=True, null=True)
    interaccionpersonallamada_identificacion = models.CharField(max_length=512, blank=True, null=True)
    interaccionpersonallamada_telefono = models.CharField(max_length=512, blank=True, null=True)
    interaccionpersonallamada_token = models.ForeignKey('DataPersonas', models.DO_NOTHING, db_column='interaccionpersonallamada_token', blank=True, null=True)
    interaccionpersonallamada_fechacreacion = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_interaccionpersonallamada'


# class DataObligacion(models.Model):
#     obligacion_fechacreacion = models.CharField(max_length=512, blank=True, null=True)
#     obligacion_fechacreacionobligacion = models.CharField(max_length=512, blank=True, null=True)
#     obligacion_fecha_vencimientoobligacion = models.CharField(max_length=512, blank=True, null=True)
#     obligacion_tipo_producto = models.ForeignKey('DataTipoproducto', models.DO_NOTHING, db_column='obligacion_tipo_producto', blank=True, null=True)
#     obligacion_producto = models.CharField(max_length=512, blank=True, null=True)
#     obligacion_persona = models.ForeignKey('DataPersonas', models.DO_NOTHING, db_column='obligacion_persona', blank=True, null=True)
#     obligacion_portafolio = models.ForeignKey('DataPortafolio', models.DO_NOTHING, db_column='obligacion_portafolio', blank=True, null=True)
#     obligacion_saldocapital = models.FloatField(blank=True, null=True)
#     obligacion_saldointerescorriente = models.FloatField(blank=True, null=True)
#     obligacion_saldointeresmora = models.FloatField(blank=True, null=True)
#     obligacion_seguro = models.FloatField(blank=True, null=True)
#     obligacion_comision = models.FloatField(blank=True, null=True)
#     obligacion_saldototal = models.FloatField(blank=True, null=True)
#     obligacion_tipoobligacion = models.ForeignKey('DataTipoobligacion', models.DO_NOTHING, db_column='obligacion_tipoobligacion', blank=True, null=True)
#     obligacion_estadoobligacion = models.CharField(max_length=1, blank=True, null=True)
#     obligacion_variable1 = models.CharField(max_length=512, blank=True, null=True)
#     obligacion_variable1_descripcion = models.CharField(max_length=512, blank=True, null=True)
#     obligacion_variable2 = models.CharField(max_length=512, blank=True, null=True)
#     obligacion_variable2_descripcion = models.CharField(max_length=512, blank=True, null=True)
#     obligacion_variable3 = models.CharField(max_length=512, blank=True, null=True)
#     obligacion_variable3_descripcion = models.CharField(max_length=512, blank=True, null=True)
#     obligacion_variable4 = models.CharField(max_length=512, blank=True, null=True)
#     obligacion_variable4_descripcion = models.CharField(max_length=512, blank=True, null=True)
#     obligacion_variable5 = models.CharField(max_length=512, blank=True, null=True)
#     obligacion_variable5_descripcion = models.CharField(max_length=512, blank=True, null=True)
#     obligacion_variable6 = models.CharField(max_length=512, blank=True, null=True)
#     obligacion_variable6_descripcion = models.CharField(max_length=512, blank=True, null=True)
#     obligacion_variable7 = models.CharField(max_length=512, blank=True, null=True)
#     obligacion_variable7_descripcion = models.CharField(max_length=512, blank=True, null=True)
#     obligacion_variable8 = models.CharField(max_length=512, blank=True, null=True)
#     obligacion_variable8_descripcion = models.CharField(max_length=512, blank=True, null=True)
#     obligacion_variable9 = models.CharField(max_length=512, blank=True, null=True)
#     obligacion_variable9_descripcion = models.CharField(max_length=512, blank=True, null=True)
#     obligacion_variable10 = models.CharField(max_length=512, blank=True, null=True)
#     obligacion_variable10_descripcion = models.CharField(max_length=512, blank=True, null=True)
#     obligacion_variable11 = models.CharField(max_length=512, blank=True, null=True)
#     obligacion_variable11_descripcion = models.CharField(max_length=512, blank=True, null=True)
#     obligacion_variable12 = models.CharField(max_length=512, blank=True, null=True)
#     obligacion_variable12_descripcion = models.CharField(max_length=512, blank=True, null=True)
#     obligacion_variable13 = models.CharField(max_length=512, blank=True, null=True)
#     obligacion_variable13_descripcion = models.CharField(max_length=512, blank=True, null=True)
#     obligacion_variable14 = models.CharField(max_length=512, blank=True, null=True)
#     obligacion_variable14_descripcion = models.CharField(max_length=512, blank=True, null=True)
#     obligacion_variable15 = models.CharField(max_length=512, blank=True, null=True)
#     obligacion_variable15_descripcion = models.CharField(max_length=512, blank=True, null=True)
#     obligacion_variable16 = models.CharField(max_length=512, blank=True, null=True)
#     obligacion_variable16_descripcion = models.CharField(max_length=512, blank=True, null=True)
#     obligacion_variable17 = models.CharField(max_length=512, blank=True, null=True)
#     obligacion_variable17_descripcion = models.CharField(max_length=512, blank=True, null=True)
#     obligacion_variable18 = models.CharField(max_length=512, blank=True, null=True)
#     obligacion_variable18_descripcion = models.CharField(max_length=512, blank=True, null=True)
#     obligacion_variable19 = models.CharField(max_length=512, blank=True, null=True)
#     obligacion_variable19_descripcion = models.CharField(max_length=512, blank=True, null=True)
#     obligacion_variable20 = models.CharField(max_length=512, blank=True, null=True)
#     obligacion_variable20_descripcion = models.CharField(max_length=512, blank=True, null=True)
#     obligacion_variable21 = models.CharField(max_length=512, blank=True, null=True)
#     obligacion_variable21_descripcion = models.CharField(max_length=512, blank=True, null=True)
#     obligacion_variable22 = models.CharField(max_length=512, blank=True, null=True)
#     obligacion_variable22_descripcion = models.CharField(max_length=512, blank=True, null=True)
#     obligacion_variable23 = models.CharField(max_length=512, blank=True, null=True)
#     obligacion_variable23_descripcion = models.CharField(max_length=512, blank=True, null=True)
#     obligacion_variable24 = models.CharField(max_length=512, blank=True, null=True)
#     obligacion_variable24_descripcion = models.CharField(max_length=512, blank=True, null=True)
#     obligacion_variable25 = models.CharField(max_length=512, blank=True, null=True)
#     obligacion_variable25_descripcion = models.CharField(max_length=512, blank=True, null=True)
#     obligacion_variable26 = models.CharField(max_length=512, blank=True, null=True)
#     obligacion_variable26_descripcion = models.CharField(max_length=512, blank=True, null=True)
#     obligacion_variable27 = models.CharField(max_length=512, blank=True, null=True)
#     obligacion_variable27_descripcion = models.CharField(max_length=512, blank=True, null=True)
#     obligacion_variable28 = models.CharField(max_length=512, blank=True, null=True)
#     obligacion_variable28_descripcion = models.CharField(max_length=512, blank=True, null=True)
#     obligacion_variable29 = models.CharField(max_length=512, blank=True, null=True)
#     obligacion_variable29_descripcion = models.CharField(max_length=512, blank=True, null=True)
#     obligacion_variable30 = models.CharField(max_length=512, blank=True, null=True)
#     obligacion_variable30_descripcion = models.CharField(max_length=512, blank=True, null=True)
#     obligacion_estadoobligacion = models.CharField(max_length=10, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'data_obligacion'


# class DataObligacionoferta(models.Model):
#     obligacionoferta_descuentosaldocapital = models.CharField(max_length=512, blank=True, null=True)
#     obligacionoferta_descuentosaldointerescorriente = models.CharField(max_length=512, blank=True, null=True)
#     obligacionoferta_descuentosaldointeresmora = models.CharField(max_length=512, blank=True, null=True)
#     obligacionoferta_estado = models.CharField(max_length=1, blank=True, null=True)
#     obligacionoferta_seguro = models.CharField(max_length=512, blank=True, null=True)
#     obligacionoferta_comision = models.CharField(max_length=512, blank=True, null=True)
#     obligacionoferta_fechacreacion = models.CharField(max_length=512, blank=True, null=True)
#     obligacionoferta_nota = models.CharField(max_length=512, blank=True, null=True)
#     obligacionoferta_numerocuotas = models.CharField(max_length=512, blank=True, null=True)
#     obligacionoferta_obligacion = models.ForeignKey(DataObligacion, models.DO_NOTHING, db_column='obligacionoferta_obligacion', blank=True, null=True)
#     obligacionoferta_ordenoferta = models.CharField(max_length=512, blank=True, null=True)
#     obligacionoferta_interaccionpersona = models.ForeignKey(DataInteraccionpersona, models.DO_NOTHING, db_column='obligacionoferta_interaccionpersona', blank=True, null=True)
#     obligacionoferta_porcentajedescuentosaldocapital = models.CharField(max_length=512, blank=True, null=True)
#     obligacionoferta_porcentajedescuentosaldointeres_corriente = models.CharField(max_length=512, blank=True, null=True)
#     obligacionoferta_porcentajedescuentosaldointeres_mora = models.CharField(max_length=512, blank=True, null=True)
#     obligacionoferta_propuestodescuentosaldocapital = models.CharField(max_length=512, blank=True, null=True)
#     obligacionoferta_propuestodescuentosaldointerescorriente = models.CharField(max_length=512, blank=True, null=True)
#     obligacionoferta_propuestodescuentosaldointeresmora = models.CharField(max_length=512, blank=True, null=True)
#     obligacionoferta_numerocuotaspropuestas = models.CharField(max_length=512, blank=True, null=True)
#     obligacionoferta_propuestoporcentajedescuentosaldocapital = models.CharField(max_length=512, blank=True, null=True)
#     obligacionoferta_propuestoporcentajedescuentosaldointeresco = models.CharField(max_length=512, blank=True, null=True)
#     obligacionoferta_propuestoporcentajedescuentosaldointeresmo = models.CharField(max_length=512, blank=True, null=True)
#     obligacionoferta_propuestosaldocapital = models.CharField(max_length=512, blank=True, null=True)
#     obligacionoferta_propuestosaldointerescorriente = models.CharField(max_length=512, blank=True, null=True)
#     obligacionoferta_propuestosaldointeresmora = models.CharField(max_length=512, blank=True, null=True)
#     obligacionoferta_propuestototalsaldocapital = models.CharField(max_length=512, blank=True, null=True)
#     obligacionoferta_propuestototalsaldointerescorriente = models.CharField(max_length=512, blank=True, null=True)
#     obligacionoferta_propuestototalsaldointeresmora = models.CharField(max_length=512, blank=True, null=True)
#     obligacionoferta_propuestototalsaldos = models.CharField(max_length=512, blank=True, null=True)
#     obligacionoferta_saldocapital = models.CharField(max_length=512, blank=True, null=True)
#     obligacionoferta_saldointerescorriente = models.CharField(max_length=512, blank=True, null=True)
#     obligacionoferta_saldointeresmora = models.CharField(max_length=512, blank=True, null=True)
#     obligacionoferta_soporte = models.CharField(max_length=512, blank=True, null=True)
#     obligacionoferta_tipoobligacionoferta = models.ForeignKey('DataTipoobligacionoferta', models.DO_NOTHING, db_column='obligacionoferta_tipoobligacionoferta', blank=True, null=True)
#     obligacionoferta_totalsaldocapital = models.CharField(max_length=512, blank=True, null=True)
#     obligacionoferta_totalsaldointerescorriente = models.CharField(max_length=512, blank=True, null=True)
#     obligacionoferta_totalsaldointeresmora = models.CharField(max_length=512, blank=True, null=True)
#     obligacionoferta_totalsaldos = models.CharField(max_length=512, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'data_obligacionoferta'

class DataObligacion(models.Model):
    obligacion_fechacreacion = models.DateTimeField(auto_now_add=True)
    obligacion_fechacreacionobligacion = models.CharField(max_length=512, blank=True, null=True)
    obligacion_fecha_vencimientoobligacion = models.CharField(max_length=512, blank=True, null=True)
    obligacion_tipo_producto = models.ForeignKey('DataTipoproducto', models.DO_NOTHING, db_column='obligacion_tipo_producto', blank=True, null=True)
    obligacion_producto = models.CharField(max_length=512, blank=True, null=True)
    obligacion_persona = models.ForeignKey('DataPersonas', models.DO_NOTHING, db_column='obligacion_persona', blank=True, null=True)
    obligacion_portafolio = models.ForeignKey('DataPortafolio', models.DO_NOTHING, db_column='obligacion_portafolio', blank=True, null=True)
    obligacion_saldocapital = models.FloatField(blank=True, null=True)
    obligacion_saldointerescorriente = models.FloatField(blank=True, null=True)
    obligacion_saldointeresmora = models.FloatField(blank=True, null=True)
    obligacion_seguro = models.FloatField(blank=True, null=True)
    obligacion_comision = models.FloatField(blank=True, null=True)
    obligacion_saldototal = models.FloatField(blank=True, null=True)
    obligacion_tipoobligacion = models.ForeignKey('DataTipoobligacion', models.DO_NOTHING, db_column='obligacion_tipoobligacion', blank=True, null=True)
    obligacion_estadoobligacion = models.ForeignKey('DataEstadoobligacion', models.DO_NOTHING, db_column='obligacion_estadoobligacion', blank=True, null=True)
    obligacion_variable1 = models.CharField(max_length=512, blank=True, null=True)
    obligacion_variable1_descripcion = models.CharField(max_length=512, blank=True, null=True)
    obligacion_variable2 = models.CharField(max_length=512, blank=True, null=True)
    obligacion_variable2_descripcion = models.CharField(max_length=512, blank=True, null=True)
    obligacion_variable3 = models.CharField(max_length=512, blank=True, null=True)
    obligacion_variable3_descripcion = models.CharField(max_length=512, blank=True, null=True)
    obligacion_variable4 = models.CharField(max_length=512, blank=True, null=True)
    obligacion_variable4_descripcion = models.CharField(max_length=512, blank=True, null=True)
    obligacion_variable5 = models.CharField(max_length=512, blank=True, null=True)
    obligacion_variable5_descripcion = models.CharField(max_length=512, blank=True, null=True)
    obligacion_variable6 = models.CharField(max_length=512, blank=True, null=True)
    obligacion_variable6_descripcion = models.CharField(max_length=512, blank=True, null=True)
    obligacion_variable7 = models.CharField(max_length=512, blank=True, null=True)
    obligacion_variable7_descripcion = models.CharField(max_length=512, blank=True, null=True)
    obligacion_variable8 = models.CharField(max_length=512, blank=True, null=True)
    obligacion_variable8_descripcion = models.CharField(max_length=512, blank=True, null=True)
    obligacion_variable9 = models.CharField(max_length=512, blank=True, null=True)
    obligacion_variable9_descripcion = models.CharField(max_length=512, blank=True, null=True)
    obligacion_variable10 = models.CharField(max_length=512, blank=True, null=True)
    obligacion_variable10_descripcion = models.CharField(max_length=512, blank=True, null=True)
    obligacion_variable11 = models.CharField(max_length=512, blank=True, null=True)
    obligacion_variable11_descripcion = models.CharField(max_length=512, blank=True, null=True)
    obligacion_variable12 = models.CharField(max_length=512, blank=True, null=True)
    obligacion_variable12_descripcion = models.CharField(max_length=512, blank=True, null=True)
    obligacion_variable13 = models.CharField(max_length=512, blank=True, null=True)
    obligacion_variable13_descripcion = models.CharField(max_length=512, blank=True, null=True)
    obligacion_variable14 = models.CharField(max_length=512, blank=True, null=True)
    obligacion_variable14_descripcion = models.CharField(max_length=512, blank=True, null=True)
    obligacion_variable15 = models.CharField(max_length=512, blank=True, null=True)
    obligacion_variable15_descripcion = models.CharField(max_length=512, blank=True, null=True)
    obligacion_variable16 = models.CharField(max_length=512, blank=True, null=True)
    obligacion_variable16_descripcion = models.CharField(max_length=512, blank=True, null=True)
    obligacion_variable17 = models.CharField(max_length=512, blank=True, null=True)
    obligacion_variable17_descripcion = models.CharField(max_length=512, blank=True, null=True)
    obligacion_variable18 = models.CharField(max_length=512, blank=True, null=True)
    obligacion_variable18_descripcion = models.CharField(max_length=512, blank=True, null=True)
    obligacion_variable19 = models.CharField(max_length=512, blank=True, null=True)
    obligacion_variable19_descripcion = models.CharField(max_length=512, blank=True, null=True)
    obligacion_variable20 = models.CharField(max_length=512, blank=True, null=True)
    obligacion_variable20_descripcion = models.CharField(max_length=512, blank=True, null=True)
    obligacion_variable21 = models.CharField(max_length=512, blank=True, null=True)
    obligacion_variable21_descripcion = models.CharField(max_length=512, blank=True, null=True)
    obligacion_variable22 = models.CharField(max_length=512, blank=True, null=True)
    obligacion_variable22_descripcion = models.CharField(max_length=512, blank=True, null=True)
    obligacion_variable23 = models.CharField(max_length=512, blank=True, null=True)
    obligacion_variable23_descripcion = models.CharField(max_length=512, blank=True, null=True)
    obligacion_variable24 = models.CharField(max_length=512, blank=True, null=True)
    obligacion_variable24_descripcion = models.CharField(max_length=512, blank=True, null=True)
    obligacion_variable25 = models.CharField(max_length=512, blank=True, null=True)
    obligacion_variable25_descripcion = models.CharField(max_length=512, blank=True, null=True)
    obligacion_variable26 = models.CharField(max_length=512, blank=True, null=True)
    obligacion_variable26_descripcion = models.CharField(max_length=512, blank=True, null=True)
    obligacion_variable27 = models.CharField(max_length=512, blank=True, null=True)
    obligacion_variable27_descripcion = models.CharField(max_length=512, blank=True, null=True)
    obligacion_variable28 = models.CharField(max_length=512, blank=True, null=True)
    obligacion_variable28_descripcion = models.CharField(max_length=512, blank=True, null=True)
    obligacion_variable29 = models.CharField(max_length=512, blank=True, null=True)
    obligacion_variable29_descripcion = models.CharField(max_length=512, blank=True, null=True)
    obligacion_variable30 = models.CharField(max_length=512, blank=True, null=True)
    obligacion_variable30_descripcion = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'data_obligacion'


class DataObligacionoferta(models.Model):
    obligacionoferta_descuentosaldocapital = models.CharField(max_length=512, blank=True, null=True)
    obligacionoferta_descuentosaldointerescorriente = models.CharField(max_length=512, blank=True, null=True)
    obligacionoferta_descuentosaldointeresmora = models.CharField(max_length=512, blank=True, null=True)
    obligacionoferta_estado = models.BooleanField(default=True)
    obligacionoferta_seguro = models.CharField(max_length=512, blank=True, null=True)
    obligacionoferta_comision = models.CharField(max_length=512, blank=True, null=True)
    obligacionoferta_fechacreacion = models.DateTimeField(auto_now_add=True)
    obligacionoferta_nota = models.CharField(max_length=512, blank=True, null=True)
    obligacionoferta_numerocuotas = models.CharField(max_length=512, blank=True, null=True)
    obligacionoferta_obligacion = models.ForeignKey(DataObligacion, models.DO_NOTHING, db_column='obligacionoferta_obligacion', blank=True, null=True)
    obligacionoferta_ordenoferta = models.CharField(max_length=512, blank=True, null=True)
    obligacionoferta_interaccionpersona = models.ForeignKey(DataInteraccionpersona, models.DO_NOTHING, db_column='obligacionoferta_interaccionpersona', blank=True, null=True)
    obligacionoferta_porcentajedescuentosaldocapital = models.CharField(max_length=512, blank=True, null=True)
    obligacionoferta_porcentajedescuentosaldointeres_corriente = models.CharField(max_length=512, blank=True, null=True)
    obligacionoferta_porcentajedescuentosaldointeres_mora = models.CharField(max_length=512, blank=True, null=True)
    obligacionoferta_propuestodescuentosaldocapital = models.CharField(max_length=512, blank=True, null=True)
    obligacionoferta_propuestodescuentosaldointerescorriente = models.CharField(max_length=512, blank=True, null=True)
    obligacionoferta_propuestodescuentosaldointeresmora = models.CharField(max_length=512, blank=True, null=True)
    obligacionoferta_numerocuotaspropuestas = models.CharField(max_length=512, blank=True, null=True)
    obligacionoferta_propuestoporcentajedescuentosaldocapital = models.CharField(max_length=512, blank=True, null=True)
    obligacionoferta_propuestoporcentajedescuentosaldointeresco = models.CharField(max_length=512, blank=True, null=True)
    obligacionoferta_propuestoporcentajedescuentosaldointeresmo = models.CharField(max_length=512, blank=True, null=True)
    obligacionoferta_propuestosaldocapital = models.CharField(max_length=512, blank=True, null=True)
    obligacionoferta_propuestosaldointerescorriente = models.CharField(max_length=512, blank=True, null=True)
    obligacionoferta_propuestosaldointeresmora = models.CharField(max_length=512, blank=True, null=True)
    obligacionoferta_propuestototalsaldocapital = models.CharField(max_length=512, blank=True, null=True)
    obligacionoferta_propuestototalsaldointerescorriente = models.CharField(max_length=512, blank=True, null=True)
    obligacionoferta_propuestototalsaldointeresmora = models.CharField(max_length=512, blank=True, null=True)
    obligacionoferta_propuestototalsaldos = models.CharField(max_length=512, blank=True, null=True)
    obligacionoferta_saldocapital = models.CharField(max_length=512, blank=True, null=True)
    obligacionoferta_saldointerescorriente = models.CharField(max_length=512, blank=True, null=True)
    obligacionoferta_saldointeresmora = models.CharField(max_length=512, blank=True, null=True)
    obligacionoferta_soporte = models.CharField(max_length=512, blank=True, null=True)
    obligacionoferta_tipoobligacionoferta = models.ForeignKey('DataTipoobligacionoferta', models.DO_NOTHING, db_column='obligacionoferta_tipoobligacionoferta', blank=True, null=True)
    obligacionoferta_totalsaldocapital = models.CharField(max_length=512, blank=True, null=True)
    obligacionoferta_totalsaldointerescorriente = models.CharField(max_length=512, blank=True, null=True)
    obligacionoferta_totalsaldointeresmora = models.CharField(max_length=512, blank=True, null=True)
    obligacionoferta_totalsaldos = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'data_obligacionoferta'


class DataObligacionofertaacuerdopago(models.Model):
    acuerdo_pago = models.ForeignKey(DataAcuerdopago, models.DO_NOTHING, db_column='acuerdo_pago', blank=True, null=True)
    insertacerdo = models.ForeignKey(DataObligacionoferta, models.DO_NOTHING, db_column='insertacerdo', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_obligacionofertaacuerdopago'


class DataPerfilcobranza(models.Model):
    perfilcobranza_cliente = models.ForeignKey(DataClientes, models.DO_NOTHING, db_column='perfilcobranza_cliente', blank=True, null=True)
    perfilcobranza_nombre = models.CharField(max_length=512, blank=True, null=True)
    perfilcobranza_descripcion = models.CharField(max_length=512, blank=True, null=True)
    perfilcobranza_diasmaximoobligacion = models.CharField(max_length=512, blank=True, null=True)
    perfilcobranza_diasminimoobligacion = models.CharField(max_length=512, blank=True, null=True)
    perfilcobranza_valormaximoobligacion = models.CharField(max_length=512, blank=True, null=True)
    perfilcobranza_valorminimoobligacion = models.CharField(max_length=512, blank=True, null=True)
    perfilcobranza_valormaximointeresesmora = models.CharField(max_length=512, blank=True, null=True)
    perfilcobranza_valorminimointeresesmora = models.CharField(max_length=512, blank=True, null=True)
    perfilcobranza_usuario = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='perfilcobranza_usuario', blank=True, null=True)
    perfilcobranza_fechacreacion = models.CharField(max_length=512, blank=True, null=True)

    def __str__(self):
        return u"%s" % (self.perfilcobranza_nombre)

    class Meta:
        managed = True
        db_table = 'data_perfilcobranza'

class DataPortafolio(models.Model):
    portafolio_cliente = models.ForeignKey(DataClientes, models.DO_NOTHING, db_column='portafolio_cliente', blank=True, null=True)
    portafolio_nombre = models.CharField(max_length=512, blank=True, null=True)
    portafolio_contrapropuesta = models.TextField(blank=True, null=True)
    portafolio_descuentos = models.TextField(blank=True, null=True)
    portafolio_responsablecorreo = models.CharField(max_length=512, blank=True, null=True)
    portafolio_responsablenombre = models.CharField(max_length=512, blank=True, null=True)
    portafolio_responsabletelefono = models.CharField(max_length=512, blank=True, null=True)
    portafolio_fechacreacion = models.CharField(max_length=512, blank=True, null=True)

    def __str__(self):
        return u"%s" % (self.perfilcobranza_nombre)

    class Meta:
        managed = True
        db_table = 'data_portafolio'

class DataPersona(models.Model):
    persona_fechacreacion = models.DateTimeField(blank=True, null=True)
    persona_identificacion = models.CharField(max_length=30)
    persona_nombre = models.CharField(max_length=300, blank=True, null=True)
    persona_tipoidentificacion = models.CharField(max_length=10, blank=True, null=True)
    persona_id = models.IntegerField(primary_key=True)
    persona_asignacion = models.ForeignKey(DataPortafolio, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_persona'


class DataPersonaperfilcobranza(models.Model):
    personaperfilcobranza_nota = models.TextField(blank=True, null=True)
    personaperfilcobranza_perfilcobranza = models.ForeignKey(DataPerfilcobranza, models.DO_NOTHING, db_column='personaperfilcobranza_perfilcobranza', blank=True, null=True)
    personaperfilcobranza_persona = models.ForeignKey(DataPersona, models.DO_NOTHING, db_column='personaperfilcobranza_persona', blank=True, null=True)
    personaperfilcobranza_fechacreacion = models.CharField(max_length=512, blank=True, null=True)
    personaperfilcobranza_portafolio = models.ForeignKey(DataPortafolio, models.DO_NOTHING, db_column='personaperfilcobranza_portafolio', blank=True, null=True)
    estado = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_personaperfilcobranza'


class DataPersonas(models.Model):
    persona_fechacreacion = models.CharField(max_length=512, blank=True, null=True)
    persona_identificacion = models.CharField(max_length=512, blank=True, null=True)
    persona_nombre = models.CharField(max_length=512, blank=True, null=True)
    persona_tipoidentificacion = models.ForeignKey('DataTipoidentificacion', models.DO_NOTHING, db_column='persona_tipoidentificacion', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_personas'


class DataPersonatelefono(models.Model):
    personatelefono_ciudad = models.CharField(max_length=100, blank=True, null=True)
    personatelefono_id = models.IntegerField()
    personatelefono_telefono = models.CharField(max_length=100, blank=True, null=True)
    personatelefono_cliente = models.ForeignKey(DataClientes, models.DO_NOTHING, db_column='personatelefono_cliente', blank=True, null=True)
    personatelefono_persona = models.ForeignKey(DataPersonas, models.DO_NOTHING, db_column='personatelefono_persona', blank=True, null=True)
    personatelefono_tipotelefono = models.ForeignKey('DataTipotelefono', models.DO_NOTHING, db_column='personatelefono_tipotelefono', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_personatelefono'




class DataPortafolioarchivos(models.Model):
    archivos_portafolio = models.ForeignKey(DataPortafolio, models.DO_NOTHING, db_column='archivos_portafolio', blank=True, null=True)
    archivos_nombre = models.CharField(max_length=512, blank=True, null=True)
    archivos_observacion = models.TextField(blank=True, null=True)
    archivos_usuario = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='archivos_usuario', blank=True, null=True)
    archivos_archivo = models.CharField(max_length=512, blank=True, null=True)
    archivos_fechacreacion = models.CharField(max_length=512, blank=True, null=True)
    archivos_estado = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_portafolioarchivos'


class DataProducto(models.Model):
    producto_identificacion = models.CharField(max_length=30, blank=True, null=True)
    producto_persona_identifiacion = models.CharField(max_length=30, blank=True, null=True)
    producto_fechaasignacion = models.DateTimeField(blank=True, null=True)
    producto_persona = models.ForeignKey(DataPersona, models.DO_NOTHING, blank=True, null=True)
    producto_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'data_producto'


class DataReglasnegociacion(models.Model):
    reglasnegociacion_portafolio = models.ForeignKey(DataPortafolio, models.DO_NOTHING, db_column='reglasnegociacion_portafolio', blank=True, null=True)
    reglasnegociacion_nombre = models.CharField(max_length=512, blank=True, null=True)
    reglasnegociacion_diasmoramaximo = models.IntegerField(blank=True, null=True)
    reglasnegociacion_diasmoraminimo = models.IntegerField(blank=True, null=True)
    reglasnegociacion_numerocuotasmaximo = models.IntegerField(blank=True, null=True)
    reglasnegociacion_numerocuotasminimo = models.IntegerField(blank=True, null=True)
    reglasnegocioacion_saldocapitalmaximo = models.FloatField(blank=True, null=True)
    reglasnegocioacion_saldocapitalminimo = models.FloatField(blank=True, null=True)
    reglasnegocioacion_saldointeresmoramaximo = models.FloatField(blank=True, null=True)
    reglasnegocioacion_saldointeresmoraminimo = models.FloatField(blank=True, null=True)
    reglasnegocioacion_saldototalmaximo = models.FloatField(blank=True, null=True)
    reglasnegocioacion_saldototalminimo = models.FloatField(blank=True, null=True)
    reglasnegocioacion_saldointerescorrientemaximo = models.FloatField(blank=True, null=True)
    reglasnegocioacion_saldointerescorrienteminimo = models.FloatField(blank=True, null=True)
    reglasnegocioacion_descuentosaldocapitalmaximo = models.FloatField(blank=True, null=True)
    reglasnegocioacion_descuentosaldocapitalminimo = models.FloatField(blank=True, null=True)
    reglasnegocioacion_descuentosaldointerescorrientemaximo = models.FloatField(blank=True, null=True)
    reglasnegocioacion_descuentosaldointerescorrienteminimo = models.FloatField(blank=True, null=True)
    reglasnegocioacion_descuentosaldointeresmoramaximo = models.FloatField(blank=True, null=True)
    reglasnegocioacion_descuentosaldointeresmoraminimo = models.FloatField(blank=True, null=True)
    reglasnegocioacion_descuentosaldototalmaximo = models.FloatField(blank=True, null=True)
    reglasnegocioacion_descuentosaldototalminimo = models.FloatField(blank=True, null=True)
    reglasnegociacion_vigencia = models.DateField(blank=True, null=True)
    estado = models.CharField(max_length=1, blank=True, null=True)
    reglasnegociacion_usuario = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='reglasnegociacion_usuario', blank=True, null=True)
    reglasnegociacion_fechacreacion = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_reglasnegociacion'





class DataTipodireccion(models.Model):
    tipodireccion_descripcion = models.CharField(max_length=512, blank=True, null=True)
    tipodireccion_fechacreacion = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_tipodireccion'


class DataTipoidentificacion(models.Model):
    tipoidentificacion_descripcion = models.CharField(max_length=512, blank=True, null=True)
    tipoidentificacion_fechacreacion = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_tipoidentificacion'


class DataTipointeraccion(models.Model):
    tipointeraccion_codigo = models.CharField(max_length=512, blank=True, null=True)
    tipointeraccion_descripcion = models.CharField(max_length=512, blank=True, null=True)
    tipointeraccion_fechacreacion = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_tipointeraccion'


class DataTipoobligacion(models.Model):
    tipoobligacion_nombre = models.CharField(max_length=512, blank=True, null=True)
    tipoobligacion_descripcion = models.CharField(max_length=512, blank=True, null=True)
    estado = models.CharField(max_length=1, blank=True, null=True)
    tipoobligacion_fechacreacion = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_tipoobligacion'


class DataTipoobligacionoferta(models.Model):
    tipodoobligacionoferta_nombre = models.CharField(max_length=512, blank=True, null=True)
    tipodoobligacionoferta_descripcion = models.CharField(max_length=512, blank=True, null=True)
    tipodoobligacionoferta_usuario = models.ForeignKey(DataPersonas, models.DO_NOTHING, db_column='tipodoobligacionoferta_usuario', blank=True, null=True)
    estado = models.CharField(max_length=1, blank=True, null=True)
    tipodoobligacionoferta_fechacreacion = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_tipoobligacionoferta'


class DataTipoproducto(models.Model):
    tipoproducto_nombre = models.CharField(max_length=512, blank=True, null=True)
    tipoproducto_descripcion = models.CharField(max_length=512, blank=True, null=True)
    tipoproducto_usuario = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='tipoproducto_usuario', blank=True, null=True)
    estado = models.CharField(max_length=1, blank=True, null=True)
    tipoproducto_fechacreacion = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_tipoproducto'


class DataTipotelefono(models.Model):
    tipotelefono_id = models.CharField(unique=True, max_length=20)
    tipotelefono_descripcion = models.TextField(blank=True, null=True)
    tipotelefono_fechacreacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_tipotelefono'


class DataUbicacion(models.Model):
    ubicacion_direccion = models.CharField(max_length=200, blank=True, null=True)
    ubicacion_pais = models.CharField(max_length=50, blank=True, null=True)
    ubicacion_departamento = models.CharField(max_length=50, blank=True, null=True)
    ubicacion_ciudad = models.CharField(max_length=50, blank=True, null=True)
    ubicacion_localidad = models.CharField(max_length=50, blank=True, null=True)
    ubicacion_barrio = models.CharField(max_length=100, blank=True, null=True)
    ubicacion_persona = models.ForeignKey(DataPersona, models.DO_NOTHING)
    ubicacion_id = models.IntegerField(primary_key=True)

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
    empresa_id = models.IntegerField(primary_key=True)
    empresa_nombre = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_ubicacion_empresa'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'
        unique_together = (('id', 'id'),)


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model', 'app_label', 'model'), ('id', 'id'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'
        unique_together = (('id', 'id'),)


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
        unique_together = (('session_key', 'session_key'),)


class TableA(models.Model):
    interaccionpersona_personaportafoliotoken = models.CharField(max_length=20, blank=True, null=True)
    interaccionpersona_fechainteraccion = models.DateTimeField(blank=True, null=True)
    interaccionpersona_tipointeraccion = models.CharField(max_length=10, blank=True, null=True)
    personaportafoliotoken_persona = models.IntegerField(blank=True, null=True)
    personaportafoliotoken_portafolio = models.IntegerField(blank=True, null=True)
    persona_identificacion = models.CharField(max_length=100, blank=True, null=True)
    persona_nombre = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'table_a'


class TableB(models.Model):
    tipointeraccion_descripcion = models.CharField(max_length=100, blank=True, null=True)
    tipointeraccion_id = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'table_b'


class TableC(models.Model):
    portafolio_id = models.IntegerField(blank=True, null=True)
    cliente_nombre = models.CharField(max_length=100, blank=True, null=True)
    empresa_nombre = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'table_c'


class TableD(models.Model):
    interaccion_fecha_interaccion = models.DateTimeField(blank=True, null=True)
    interaccion_hora_inicio = models.TextField(blank=True, null=True)
    interaccion_hora_fin = models.TextField(blank=True, null=True)
    interaccion_resultado = models.CharField(max_length=100, blank=True, null=True)
    interaccion_accion = models.CharField(max_length=100, blank=True, null=True)
    interaccion_nombre = models.CharField(max_length=300, blank=True, null=True)
    interaccion_identificacion = models.CharField(max_length=100, blank=True, null=True)
    interaccion_id_campana = models.IntegerField(blank=True, null=True)
    interaccion_cliente = models.CharField(max_length=100, blank=True, null=True)
    interaccion_empresa = models.CharField(max_length=100, blank=True, null=True)
    interaccion_canal = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'table_d'
