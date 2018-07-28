var str_cargando = {
	tm:null,
	ready:function() {
		this.documentos()
	},

	documentos:function() {
		var html = `
			<div style="vertical-align:middle;font-size:3em;">
				<div class="spinner">Procesando
			        <div class="m-spinner m-spinner--brand m-spinner--lg"></div>
			        <div class="m-spinner m-spinner--primary m-spinner--lg"></div>
			        <div class="m-spinner m-spinner--success m-spinner--lg"></div>       
			        <div class="m-spinner m-spinner--info m-spinner--lg"></div>
			        <div class="m-spinner m-spinner--warning m-spinner--lg"></div>
			        <div class="m-spinner m-spinner--danger m-spinner--lg"></div>
		        </div>  
		    </div>
		`;
		swal({
		  html:html,
		  showCloseButton: true,
		  width: '80%',
		  padding: '10em',
		  showConfirmButton:false,
		  showCloseButton:false,
		});
		// // $('.btn_clickAutomatico').click();
		// $('#btn_clickAutomatico-id').trigger('click');
		$('#btn_clickAutomatico')[0].click(function(){}); 
		// $("#loader").fadeOut();
		/*Medio segundo despues, se va poco a poco el fondo del preloader*/
		// $("#loader-wrapper").delay(500).fadeOut("slow")
		// $('#btnA_procesarFinal').click(function(event) {
		// 	// $("#loader").fadeOut();
		// 	Medio segundo despues, se va poco a poco el fondo del preloader
		// 	// $("#loader-wrapper").delay(500).fadeOut("slow")
		// 	console.log('Alert');
		// });
		// document.getElementById('fondo').style.visibility = 'hidden'; http://192.168.1.198:8082/listarArchivosProcesados   http://192.168.1.198:8082/listarArchivosProcesados#!
	},
};
str_cargando.ready();