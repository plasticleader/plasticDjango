from  django import forms
from app.cargueArchivos.models import *
from .models import *


class UploadArchivosAsignacion(forms.ModelForm):
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
		model     = DataAsignacionarchivosStraus
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
			'archivos_asignacion'
		]
		widgets  = {
			'archivos_asignacion':        forms.TextInput(attrs={'class':'form-control m-input m-input--pill', 'type':'hidden','required':''}),
		}


