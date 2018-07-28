from .models import *
from django.contrib.auth.models import User


def getValidate(straNombre,straCliente,straUsuario,straEmpresa):

	porta = DataAsignacion.objects.filter(
		asignacion_cliente=straCliente,
		asignacion_empresa=straEmpresa,
		asignacion_nombre=straNombre,
	).count()
	if ( (porta==0) | (porta=='0')):
		cretaPorta = DataAsignacion.objects.create(
			asignacion_cliente=straCliente,
			asignacion_empresa=straEmpresa,
			asignacion_nombre=straNombre,
			asignacion_contrapropuesta=0,
			asignacion_descuentos=0,
		)
		cretaPortaFinal = int(cretaPorta.id)
	else:
		cretaPortaFinal = str('Exite')
		pass
	return cretaPortaFinal


def datosUsu(stras_id_usu):
	datoUsu = User.objects.filter(id=stras_id_usu).last()
	usuLogeado = {
		'nombre'  : str(datoUsu.first_name)+' '+str(datoUsu.last_name),
		'email'   : datoUsu.email,
		'usuario' : datoUsu.username,
	}
	return usuLogeado
