from  django import forms
from app.cargueArchivos.models import *
from .models import *

class LoginForm(forms.Form):
	identificacion =   forms.TextInput(attrs={'class':'form-control m-input m-input--pill','placeholder':'Ingrese usuario','autofocus':'','required':''}),
	password = forms.TextInput(attrs={'class':'form-control m-input m-input--pill','required':''}),

class TiposArchivos(forms.ModelForm):
	tt = ''

# class TiposArchivos(forms.ModelForm):
# 	# archivocarguearchivo = forms.FileField(
#  #        required         = True,
#  #        widget           = forms.ClearableFileInput(
# 	#  	    attrs        = {
# 	#  	    	'multiple': False,
# 	#  	    	'class':'form-control m-input m-input--pill'
#  # 	    	}
# 	#  	)
# 	# )
# 	class Meta:
# 		model     = DataArchivoCargue
# 		fields    = [
# 			'archivocarguearchivotipocargue',
# 			'archivocarguenombreasignacion',
# 			'archivocarguecantidadcolumnasObligatorias',
# 			'archivocarguenomcolumnas',
# 		]
# 		widgets  = {
# 			'archivocarguearchivotipocargue':              forms.Select(attrs={'class':'form-control m-input m-input--pill','required':'','autofocus':''}),
# 			'archivocarguenombreasignacion':               forms.TextInput(attrs={'class':'form-control m-input m-input--pill','required':''}),
# 			'archivocarguecantidadcolumnasObligatorias':   forms.TextInput(attrs={'class':'form-control m-input m-input--pill','required':''}),
# 			'archivocarguenomcolumnas':                    forms.Textarea(attrs={'class':'form-control m-input m-input--pill','required':''}),
# 			# 'archivocarguearchivo':   forms.FileField(required=True,widget=forms.ClearableFileInput(attrs={'multiple': True,'class':'form-control m-input m-input--pill'})),
# 		}


class empresasCreate(forms.ModelForm):
	class Meta:
		model    = DataEmpresaStraus 
		fields   = [
			'empresa_nombre',
			'empresa_razonsocial',
			'empresa_nit',
			#'empresa_ciudad',
			'empresa_direccion',
			'empresa_responsablenombre',
			'empresa_responsabletelefono',
			'empresa_telefono',
			'empresa_email',
		]
		widgets  = {
			'empresa_direccion':           forms.TextInput(attrs={'class':'form-control m-input m-input--pill','placeholder':'Direccion Empresa'}),
			'empresa_nit':				   forms.TextInput(attrs={'class':'form-control m-input m-input--pill','placeholder':'Nit Empresa','required':''}),
			'empresa_nombre':              forms.TextInput(attrs={'class':'form-control m-input m-input--pill','placeholder':'Nombre Empresa','autofocus':'','required':''}),
			'empresa_razonsocial':         forms.TextInput(attrs={'class':'form-control m-input m-input--pill','placeholder':'Razón Social'}),
			'empresa_telefono':            forms.TextInput(attrs={'class':'form-control m-input m-input--pill','placeholder':'Telefono Empresa','required':''}),
			'empresa_email':               forms.TextInput(attrs={'class':'form-control m-input m-input--pill','placeholder':'Email Empresa'}),
			'empresa_responsablenombre':   forms.TextInput(attrs={'class':'form-control m-input m-input--pill','placeholder':'Responsable','required':''}),
			'empresa_responsabletelefono': forms.TextInput(attrs={'class':'form-control m-input m-input--pill','placeholder':'Telefono Responsable'}),
			#'empresa_ciudad':              forms.Select(attrs={'class':'form-control m-input m-input--pill','required':''}),
			# 'tipocarguenombre':   forms.TextInput(attrs={'class':'form-control m-input m-input--pill','placeholder':'Nombre Tipo Cargue','autofocus':'','required':''}),
		}




class UploadArchivosFallabella(forms.ModelForm):
	archivos_archivo = forms.FileField(
        required         = True,
        widget           = forms.ClearableFileInput(
	 	    attrs        = {
	 	    	'multiple': True,
	 	    	'class':'form-control m-input m-input--pill'
 	    	}
	 	)
	)
	class Meta:
		model     = DataPortafolioarchivosStraus
		fields    = [
			'archivos_nombre',
			'archivos_archivo',
			'archivos_observacion',
		]
		widgets  = {
			'archivos_nombre':        forms.TextInput(attrs={'class':'form-control m-input m-input--pill','required':'','autofocus':''}),
			'archivos_observacion':   forms.Textarea(attrs={'class':'form-control m-input m-input--pill'}),
		}





class UploadArchivos(forms.ModelForm):
	archivos_archivo = forms.FileField(
		required         = True,
		widget           = forms.ClearableFileInput(
			attrs        = {
				'multiple': True,
				'class':'form-control m-input m-input--pill'
			}
		)
	)
	class Meta:
		model     = DataarchivosStraus
		fields    = [
			'archivos_archivo',
			'archivos_portafolio'
		]
		widgets  = {
			'archivos_portafolio':        forms.TextInput(attrs={'class':'form-control m-input m-input--pill', 'type':'hidden','required':''}),
		}










# class tipoCargue(forms.ModelForm):
# 	rrr = 0 

# class UploadArchivos(forms.ModelForm):
# 	archivocargueprocesararchivo = forms.FileField(
#         required         = True,
#         widget           = forms.ClearableFileInput(
# 	 	    attrs        = {
# 	 	    	'multiple': False,
# 	 	    	'class':'form-control m-input m-input--pill'
#  	    	}
# 	 	)
# 	)
# 	class Meta:
# 		model     = DataArchivoCargueProcesar
# 		fields    = [
# 			'archivocargueprocesararchivotipocargue',
# 			'archivocargueprocesararchivoobservacion',
# 			'archivocargueprocesararchivo',
# 		]
# 		widgets  = {
# 			'archivocargueprocesararchivotipocargue':                     forms.Select(attrs={'class':'form-control m-input m-input--pill','required':'','autofocus':''}),
# 			'archivocargueprocesararchivoobservacion':                    forms.Textarea(attrs={'class':'form-control m-input m-input--pill','required':''}),
# 		}

# class UploadArchivos(forms.ModelForm):
# 	dd = 00