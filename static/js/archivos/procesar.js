var str_archivos = {
	tm:null,
	ready:function() {
		this.documentos()
	},

	documentos:function() {
		$('#btnA_procesarFinal').click(function(event) {
			// $("#loader").fadeOut();
			/*Medio segundo despues, se va poco a poco el fondo del preloader*/
			// $("#loader-wrapper").delay(500).fadeOut("slow")
			console.log('Alert');
		});
	},
	preProcesar:function (str_id_archivo) {
		$('#btn_procesar').hide('slow/400/fast', function() {
			$('#id_spiners').show();
		});
		var url  = $('#id_archivoAprocesar_'+str_id_archivo).val();
		$.ajax({
			url: url,
		    data: {id_archivo:str_id_archivo},
		    dataType: 'json',
		    success: function(result)
		    {
		       	$.each(result['columnas'], function(index, val) {
		       		if (val=='num_documento') {
		       			val = val.replace('num_documento','persona_identificacion');
		       		}else if (val=='NOMBRE') {
		       			val = val.replace('NOMBRE','persona_nombre');
		       		}else if (val=='Tipo_documento') {
		       			val = val.replace('Tipo_documento','persona_tipoidentificacion');
		       		}else {
		       			val = val;
		       		}
		       		
		       		$("#id_tr").append('<th>'+val+'</th>;');
		       	});
		       	var myObj = JSON.parse(result['valores']);
		       	$('#id_tbody').append('<tr>')
		       	$.each(myObj, function(index, val) {
		       		$.each(val, function(inde, va) {
		       			if ((va=='1') || (va==1)) {
			       			va = 'CC';
			       		}else {
			       			va = va;
			       		}
		       			$('#id_tbody').append('<td>'+va+'</td>')
       				});
       				$('#id_tbody').append('</tr>')
       				$('#id_tbody').append('<tr>')
		       	});

		       	$('#seccionIdPrincipal').hide('slow/400/fast', function() {
		       		$('#seccionIdSecundaria').show();
		       	});
		       	$('#btn_procesarFinal').html(`
		       		<a href="/procesando/`+result['id']+`" id="btnA_procesarFinal" class="btn btn-success m-btn m-btn--custom m-btn--icon m-btn--pill m-btn--air btn-block">Procesar</a>
		       	`);
	    	}
    	});
	  	
	},
	
};

str_archivos.ready();