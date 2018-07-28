var ejecutar = {
	ready:function() {
		this.documentos();
	},
	documentos:function(){},
	ejecutar:function(pl_id,pl_opc,pl_nombre) {
		swal({
		  title: "Confirmación.?",
		  text: "Seguro(a) desea ejecutar este portafolio",
		  icon: "info",
		  buttons: true,
		  dangerMode: true,
		})
		.then((willDelete) => {
		  if (willDelete) {
		    swal("Por favor no recargue o cierre la pagian hasta finalizar la ejecución.", {
		      icon: "success",
		      timer: 5000,
		    });
		    $('#divEjecutar_'+pl_id+'').html('');
				//$('#divEjecutar_'+pl_id+'').html(lp_global.datoHtml());
				var datoHtml  =
		    `
		      <div class="m-spinner m-spinner--brand m-spinner--sm"></div>
		      <div class="m-spinner m-spinner--primary m-spinner--sm"></div>
		      <div class="m-spinner m-spinner--success m-spinner--sm"></div>
		      <div class="m-spinner m-spinner--info m-spinner--sm"></div>
		      <div class="m-spinner m-spinner--warning m-spinner--sm"></div>
		      <div class="m-spinner m-spinner--danger m-spinner--sm"></div>
		    `;
		    $('#divEjecutar_'+pl_id+'  ').html(datoHtml);
		    $.ajax({
		    	url: 'inicioEjecucion',
		    	type: 'GET',
		    	data: {idArchivo:pl_id,opc:pl_opc},
		    })
		    .done(function(data) {
		    	console.log(data);
		    });
		  } else {
		    swal("Cancelado","Ha cancelado la ejecución","info");
		  }
		});

	},
	masInfo:function(){
		lp_global.crearVentana('Mostarndo','ejecucion','mod_al-sm');
	},
	procesarArchivo:function(pl_id,pl_opc,pl_nombre) {
    // alert(pl_id);
    $('#divEjecutar_'+pl_id+'  ').html('');
    var datoHtml  =
    `
      <div class="m-spinner m-spinner--brand m-spinner--sm"></div>
      <div class="m-spinner m-spinner--primary m-spinner--sm"></div>
      <div class="m-spinner m-spinner--success m-spinner--sm"></div>
      <div class="m-spinner m-spinner--info m-spinner--sm"></div>
      <div class="m-spinner m-spinner--warning m-spinner--sm"></div>
      <div class="m-spinner m-spinner--danger m-spinner--sm"></div>
    `;
    $('#divEjecutar_'+pl_id+'  ').html(datoHtml);
    $.post('inicioEjecucion', {idArchivo:pl_id,opc:pl_opc}, function(data, textStatus, xhr) {
      if (data>0) {
      /*  var datoHtml =
        `
          <a href="#"  title="Descárga archivo `+pl_nombre+` procesado" onclick="ejecutar.descargarArchivo(`+data+`)" class="btn btn-outline-success m-btn m-btn--icon m-btn--icon-only m-btn--custom m-btn--outline-2x m-btn--pill m-btn--air">
            <i class="flaticon-download"></i>
          </a>
        `;
        $('#divEjecutar_'+pl_id+'  ').html(datoHtml);*/
				window.location.href = '';
      }else{
       alert('Grave');
      }
    });
  },
	descargarArchivo:function(pl_idArchivo){
		  $.get('descargaArchivo', {idArchivo:pl_idArchivo}, function(data, textStatus, xhr) {
				if (data=='ok') {
					alert('todo bn');
				}else{
					alert('algo mal');
				}
			});
	},
};
ejecutar.ready();
