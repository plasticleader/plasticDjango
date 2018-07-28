from django.conf.urls import url, include
from .views import *
from django.contrib.auth.views import login
from django.contrib.staticfiles import views
from django.urls import re_path
from django.contrib.auth.decorators import login_required

urlpatterns = [  
    url(r'^falabella$', login_required(getFalabella), name='falabella'),
    url(r'^crearCampanasFalabella$', login_required(falabellaCampanacrear), name='falabellaCampanacrear'),
    url(r'^crezcamos$', login_required(getCrezcamos), name='crezcamos'),
    url(r'^updatecrezcamos$', login_required(getUpdateCrezcamos), name='updatecrezcamos'),
    url(r'^crearCampanasCrezcamos$', login_required(crezcamosCampanacrear), name='crezcamosCampanacrear'),
    url(r'^preProcesar$', login_required(preProcesar), name='preProcesar'),
    url(r'^procesando/(?P<id_archivo>\d+)$', login_required(ProcesarArchivo), name='procesararchivo'),
    url(r'^procesandoUpdate/(?P<id_archivo>\d+)$', login_required(ProcesarArchivoUpdate), name='procesandoUpdate'),
    url(r'^procesandoFinal/(?P<id_archivoFinal>\d+)$', login_required(ProcesarArchivoFinal), name='procesararchivofinal'),
    url(r'^procesandoUpdateFinal/(?P<id_archivoFinal>\d+)$', login_required(ProcesarArchivoFinalUpdate), name='procesandoUpdateFinal'),
    url(r'^descargaArchivo/(?P<id_archivoFinal>\d+)$', login_required(descargaArchivoCampanaSinProcesar), name='descargaArchivo'),
    url(r'^trazabilidad/(?P<id_portafolio>\d+)$', login_required(trazabilidad), name='trazabilidad'),
    url(r'^limpiar$', login_required(limpiar), name='limpiar'),



    #  Url en fase de exploración
    url(r'^listarEmpresas$', login_required(EmpresaList.as_view()), name='empresaslistar'),
    url(r'^listarArchivos$', login_required(ArchivosCargueList.as_view()), name='archivoscargueslistar'),
    url(r'^listarArchivosProcesados$',login_required(ArchivosCargueProcesar.as_view()), name='archivosprocesarlistar'),
    url(r'^crearEmpresas$', login_required(crearEmpresaCreate), name='empresacrear'),
    url(r'^tiposArchivos$', login_required(crearTiposArchivos), name='tipoarchivoscrear'),
    url(r'^archivosProcesados$', login_required(crearArchivosProcesados), name='archivosprocersadoscrear'),
    url(r'^editarTipos/(?P<id_tipo>\d+)$', login_required(editarTiposEdit), name='tipocargueseditar'),
    url(r'^deleteTipos/(?P<id_tipo>\d+)$', login_required(deleteTiposDelete), name='tipocarguesdelete'),
   

]