var lp_usersFinal = {
	token:null,
	fecha:null,
	cuotas:null,
	ready:function() {
		// $('#m_datepicker').datetimepicker();
		// lp_usersFinal.fecha = $('#fechaPago').pickadate().pickadate('picker');
		// $('.datepicker').pickadate();
	},
	noAceptar:function(tu_token,tu_cuotas){
		lp_usersFinal.token = tu_token;
		lp_usersFinal.cuotas = tu_cuotas;
		$('#contenedorResumenOferta').hide('slow/200/fast', function() {
			if (lp_usersFinal.cuotas>1) {
				$('#noaceptaOfertaMasCuota').show('slow',function(){});
			}else{
				$('#noaceptaOfertaUnaCuota').show('slow',function(){});
			}
		});
	},
	enviatContraOferta:function(){
		var fechaPago = $('#fechaPago').val();
		var observacionOne = $('#observacionesNoPagoOne').val();
		var observacionTwo = $('#observacionesNoPagoTwo').val();
		var envioCuota = $("#demo_cuotas").html();
		var envioValor = $("#demo").html();
		// swal('Cuota',''+envioCuota+'');
		// swal('Valor',''+envioValor+'');
		if (lp_usersFinal.cuotas>1) {
			swal('Valor');
			if (envioCuota==1) {
				var fechaPagoTwo = $('#fechaPagoTwo').val();
				if(lp_global.valida_campo('fechaPagoTwo','Debe seleccionar una fecha',true,'')){return false;}
			}else{
				var fechaPagoTwo = ''
			}
			$.ajax({
				url: 'noAceptaOfertaTwo',
				type: 'GET',
				data: {cuota:envioCuota,obs:observacionTwo,token:lp_usersFinal.token,valor:envioValor,fecha:fechaPagoTwo},
			})
			.done(function(data) {
				console.log(data);
			});
		}else{
		// swal('Coutas');
			if(lp_global.valida_campo('fechaPago','Debe seleccionar una fecha',true,'')){return false;}
			swal({
			  title: 'Confirmación..!',
			  text: "Seguro desea enviar esta propuesta, con pago para esta fecha "+fechaPago+" ?",
			  showCancelButton: true,
			  confirmButtonColor: '#3085d6',
			  cancelButtonColor: '#d33',
			  confirmButtonText: 'Si enviar',
			  showLoaderOnConfirm: true,
			}).then((result) => {
			  	if (result.value) {
				  	$.ajax({
						url: 'noAceptaOfertaOne',
						type: 'GET',
						data: {fecha:fechaPago,obs:observacionOne,token:lp_usersFinal.token},
					})
					.done(function(data) {
						swal({
						  title: 'Felicidades',
						  text: 'Su propuesta sera analizada.\n Muy pronto recibira información de su propuesta.',
						  imageUrl: 'https://unsplash.it/400/200',
						  imageWidth: 400,
						  imageHeight: 200,
						  imageAlt: 'Custom image',
						  animation: false
						});
					});
				}
			})
			// const ipAPI = 'https://api.ipify.org?format=json'
			// swal.queue([{
			//   title: 'Your public IP',
			//   confirmButtonText: 'Show my public IP',
			//   text:
			//     'Your public IP will be received ' +
			//     'via AJAX request',
			//   showLoaderOnConfirm: true,
			//   preConfirm: () => {
			//     return fetch(ipAPI)
			//       .then(response => response.json())
			//       .then(data => swal.insertQueueStep(data.ip))
			//       .catch(() => {
			//         swal.insertQueueStep({
			//           type: 'error',
			//           title: 'Unable to get your public IP'
			//         })
			//       })
			//   }
			// }])
		}
	},
	cancelar:function() {
		window.location.href="";
	},
};

lp_usersFinal.ready();