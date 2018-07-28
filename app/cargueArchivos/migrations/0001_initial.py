# Generated by Django 2.0.7 on 2018-07-28 01:20

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DataarchivosStraus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archivos_archivo', models.FileField(blank=True, null=True, upload_to='archivos/clientes/temporal')),
                ('archivos_fechacreacion', models.DateTimeField(default=datetime.datetime(2018, 7, 27, 20, 20, 38, 346066))),
            ],
        ),
        migrations.CreateModel(
            name='DataAsignacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asignacion_nombre', models.CharField(blank=True, max_length=512, null=True)),
                ('asignacion_fechacreacion', models.DateTimeField(default=datetime.datetime(2018, 7, 27, 20, 20, 38, 344215))),
                ('asignacion_empresa', models.CharField(blank=True, max_length=512, null=True)),
                ('asignacion_cliente', models.CharField(blank=True, max_length=512, null=True)),
                ('asignacion_contrapropuesta', models.CharField(blank=True, max_length=512, null=True)),
                ('asignacion_descuentos', models.CharField(blank=True, max_length=512, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DataAsignacionarchivosStraus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archivos_nombre', models.CharField(blank=True, max_length=512, null=True)),
                ('archivos_observacion', models.TextField(blank=True, null=True)),
                ('archivos_archivo', models.FileField(blank=True, null=True, upload_to='archivos/clientes')),
                ('archivos_fechacreacion', models.DateTimeField(default=datetime.datetime(2018, 7, 27, 20, 20, 38, 345490))),
                ('archivos_estado', models.BooleanField(default=False)),
                ('archivos_asignacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cargueArchivos.DataAsignacion')),
            ],
        ),
        migrations.CreateModel(
            name='DataCorreoelectronico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correoelectronico_correo', models.CharField(blank=True, max_length=326, null=True)),
                ('correoelectronico_persona', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DataObligacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obligacionpersona', models.CharField(blank=True, max_length=30, null=True)),
                ('obligacionportafolio', models.CharField(blank=True, max_length=30, null=True)),
                ('obligacionsaldo_capital', models.FloatField(default=0)),
                ('obligacionseguro', models.FloatField(default=0)),
                ('obligacioncomision', models.FloatField(default=0)),
                ('obligacionsaldo_interes_corriente', models.FloatField(default=0)),
                ('obligacionsaldo_interes_mora', models.FloatField(default=0)),
                ('obligacionsaldo_total', models.FloatField(default=0)),
                ('obligacionfechacreacion', models.DateTimeField(default=datetime.datetime(2018, 7, 27, 20, 20, 38, 349588))),
                ('obligacionfecha_creacion_obligacion', models.CharField(blank=True, max_length=300, null=True)),
                ('obligacionfecha_vencimiento_obligacion', models.CharField(blank=True, max_length=300, null=True)),
                ('obligacionproducto', models.CharField(blank=True, max_length=300, null=True)),
                ('obligaciontipo_obligacion', models.CharField(blank=True, max_length=200, null=True)),
                ('obligaciontipo_prducto', models.CharField(blank=True, max_length=200, null=True)),
                ('variable1', models.CharField(blank=True, max_length=200, null=True)),
                ('variable1_descripcion', models.CharField(blank=True, max_length=200, null=True)),
                ('variable2', models.CharField(blank=True, max_length=200, null=True)),
                ('variable2_descripcion', models.CharField(blank=True, max_length=200, null=True)),
                ('variable3', models.CharField(blank=True, max_length=200, null=True)),
                ('variable3_descripcion', models.CharField(blank=True, max_length=200, null=True)),
                ('variable4', models.CharField(blank=True, max_length=200, null=True)),
                ('variable4_descripcion', models.CharField(blank=True, max_length=200, null=True)),
                ('variable5', models.CharField(blank=True, max_length=200, null=True)),
                ('variable5_descripcion', models.CharField(blank=True, max_length=200, null=True)),
                ('variable6', models.CharField(blank=True, max_length=200, null=True)),
                ('variable6_descripcion', models.CharField(blank=True, max_length=200, null=True)),
                ('variable7', models.CharField(blank=True, max_length=200, null=True)),
                ('variable7_descripcion', models.CharField(blank=True, max_length=200, null=True)),
                ('variable8', models.CharField(blank=True, max_length=200, null=True)),
                ('variable8_descripcion', models.CharField(blank=True, max_length=200, null=True)),
                ('variable9', models.CharField(blank=True, max_length=200, null=True)),
                ('variable9_descripcion', models.CharField(blank=True, max_length=200, null=True)),
                ('variable10', models.CharField(blank=True, max_length=200, null=True)),
                ('variable10_descripcion', models.CharField(blank=True, max_length=200, null=True)),
                ('variable11', models.CharField(blank=True, max_length=200, null=True)),
                ('variable11_descripcion', models.CharField(blank=True, max_length=200, null=True)),
                ('variable12', models.CharField(blank=True, max_length=200, null=True)),
                ('variable12_descripcion', models.CharField(blank=True, max_length=200, null=True)),
                ('variable13', models.CharField(blank=True, max_length=200, null=True)),
                ('variable13_descripcion', models.CharField(blank=True, max_length=200, null=True)),
                ('variable14', models.CharField(blank=True, max_length=200, null=True)),
                ('variable14_descripcion', models.CharField(blank=True, max_length=200, null=True)),
                ('variable15', models.CharField(blank=True, max_length=200, null=True)),
                ('variable15_descripcion', models.CharField(blank=True, max_length=200, null=True)),
                ('variable16', models.CharField(blank=True, max_length=200, null=True)),
                ('variable16_descripcion', models.CharField(blank=True, max_length=200, null=True)),
                ('variable17', models.CharField(blank=True, max_length=200, null=True)),
                ('variable17_descripcion', models.CharField(blank=True, max_length=200, null=True)),
                ('variable18', models.CharField(blank=True, max_length=200, null=True)),
                ('variable18_descripcion', models.CharField(blank=True, max_length=200, null=True)),
                ('variable19', models.CharField(blank=True, max_length=200, null=True)),
                ('variable19_descripcion', models.CharField(blank=True, max_length=200, null=True)),
                ('variable20', models.CharField(blank=True, max_length=200, null=True)),
                ('variable20_descripcion', models.CharField(blank=True, max_length=200, null=True)),
                ('variable21', models.CharField(blank=True, max_length=200, null=True)),
                ('variable21_descripcion', models.CharField(blank=True, max_length=200, null=True)),
                ('variable22', models.CharField(blank=True, max_length=200, null=True)),
                ('variable22_descripcion', models.CharField(blank=True, max_length=200, null=True)),
                ('variable23', models.CharField(blank=True, max_length=200, null=True)),
                ('variable23_descripcion', models.CharField(blank=True, max_length=200, null=True)),
                ('variable24', models.CharField(blank=True, max_length=200, null=True)),
                ('variable24_descripcion', models.CharField(blank=True, max_length=200, null=True)),
                ('variable25', models.CharField(blank=True, max_length=200, null=True)),
                ('variable25_descripcion', models.CharField(blank=True, max_length=200, null=True)),
                ('variable26', models.CharField(blank=True, max_length=200, null=True)),
                ('variable26_descripcion', models.CharField(blank=True, max_length=200, null=True)),
                ('variable27', models.CharField(blank=True, max_length=200, null=True)),
                ('variable27_descripcion', models.CharField(blank=True, max_length=200, null=True)),
                ('variable28', models.CharField(blank=True, max_length=200, null=True)),
                ('variable28_descripcion', models.CharField(blank=True, max_length=200, null=True)),
                ('variable29', models.CharField(blank=True, max_length=200, null=True)),
                ('variable29_descripcion', models.CharField(blank=True, max_length=200, null=True)),
                ('variable30', models.CharField(blank=True, max_length=200, null=True)),
                ('variable30_descripcion', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DataPersonas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('persona_identificacion', models.CharField(blank=True, max_length=512, null=True)),
                ('persona_nombre', models.CharField(blank=True, max_length=512, null=True)),
                ('persona_tipoidentificacion', models.CharField(blank=True, max_length=512, null=True)),
                ('persona_asignacion', models.CharField(blank=True, max_length=512, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DataProducto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto_identificacion', models.CharField(blank=True, max_length=30, null=True)),
                ('producto_persona_identifiacion', models.CharField(blank=True, max_length=30, null=True)),
                ('producto_fechaasignacion', models.DateTimeField(default=datetime.datetime(2018, 7, 27, 20, 20, 38, 346606))),
                ('producto_persona', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DataTelefonos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefono_numero', models.CharField(blank=True, max_length=20, null=True)),
                ('telefono_pais', models.CharField(blank=True, max_length=50, null=True)),
                ('telefono_departamento', models.CharField(blank=True, max_length=50, null=True)),
                ('telefono_ciudad', models.CharField(blank=True, max_length=50, null=True)),
                ('telefono_persona', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DataUbicacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ubicacion_direccion', models.CharField(blank=True, max_length=200, null=True)),
                ('ubicacion_pais', models.CharField(blank=True, max_length=50, null=True)),
                ('ubicacion_departamento', models.CharField(blank=True, max_length=50, null=True)),
                ('ubicacion_ciudad', models.CharField(blank=True, max_length=50, null=True)),
                ('ubicacion_localidad', models.CharField(blank=True, max_length=50, null=True)),
                ('ubicacion_barrio', models.CharField(blank=True, max_length=100, null=True)),
                ('ubicacion_persona', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DataUbicacionEmpresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa_direccion', models.CharField(blank=True, max_length=200, null=True)),
                ('empresa_pais', models.CharField(blank=True, max_length=50, null=True)),
                ('empresa_departamento', models.CharField(blank=True, max_length=50, null=True)),
                ('empresa_ciudad', models.CharField(blank=True, max_length=50, null=True)),
                ('empresa_localidad', models.CharField(blank=True, max_length=50, null=True)),
                ('empresa_barrio', models.CharField(blank=True, max_length=100, null=True)),
                ('empresa_persona', models.CharField(blank=True, max_length=30, null=True)),
                ('empresa_nombre', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DataUbicacionInfoOrigen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ubicaorigen_cliente', models.CharField(blank=True, max_length=512, null=True)),
                ('ubicaorigen_persona', models.CharField(blank=True, max_length=30, null=True)),
                ('ubicaorigen_fechaacreacion', models.DateTimeField(default=datetime.datetime(2018, 7, 27, 20, 20, 38, 348918))),
                ('ubicaorigen_observacion', models.CharField(blank=True, max_length=100, null=True)),
                ('ubicaorigen_email', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cargueArchivos.DataCorreoelectronico')),
                ('ubicaorigen_telefono', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cargueArchivos.DataTelefonos')),
                ('ubicaorigen_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='dataarchivosstraus',
            name='archivos_asignacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cargueArchivos.DataAsignacion'),
        ),
    ]
