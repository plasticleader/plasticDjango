var lp_global = {
	ready:function() {
		$('#id_empresa_ciudad').html(`
			<option value="">Seleccione Una Ciudad</option>
			<option value="Bogota">Bogota</option>
			<option value="Medellin">Medellin</option>
			<option value="Cali">Cali</option>
			<option value="Barranquilla">Barranquilla</option>
			<option value="Bucaramanga">Bucaramanga</option>
			<option value="Pereira">Pereira</option>
		`);
		// window.addEventListener("load", function()
		// {

		// 	if(!window.pageYOffset)
		// 	{
		// 		lp_global.hideAddressBar();
		// 	}

		// 	window.addEventListener("orientationchange", hideAddressBar);
		// })

		$('.datetimepicker').datetimepicker({
			// format: 'yyyy-mm-dd',
			// autoclose: true,
	  //       todayBtn: true,
	  //       pickerPosition: "bottom-left"
		});

		// window.location.hash="no-back-button";
		// window.location.hash="Again-No-back-button" //chrome
		// window.onhashchange=function(){window.location.hash="no-back-button";}
	},


	// hideAddressBar:function (){
	// 	if(!window.location.hash){
	// 		if(document.height < window.outerHeight + 10){
	// 			document.body.style.height = (window.outerHeight + 50) + 'px';
	// 		}
	// 		setTimeout(function(){
	// 			window.scrollTo(0, 1);
	// 		}, 50);
	// 	}
	// },
	/**
	 * Hide the URL address bar on standard Android's browser by setting enough
	 * document height and auto scrolling to active the bar hiding feature
	 	function hideAddressBar()
	{
	  if(!window.location.hash)
	  {
	      if(document.height < window.outerHeight + 10)
	      {
	          document.body.style.height = (window.outerHeight + 50) + 'px';
	      }

	      setTimeout(function()
	      {
	      	window.scrollTo(0, 1);
	      }, 50);
	  }
	}
	 */
	crearVentana:function(header,url,tmn) {
		// ejemplo agragar tamaño con clase  
		// Pequeño = mod_al-sm
		// Grande = mod_al-lg 3134716641 // Eugenio Medez
		//
		$("#lpHeader").html(header);
		// $('#id="lpModalGeneral').removeClass('modal-dialog mod_al-sm');
		$('#lpModalGeneral').addClass('modal-dialog '+tmn+' ');


		if (url) {
			lp_global.enviarUrl("lpBody",url,false);
		}

		$(".modal").modal({
			keyboard: false,
			backdrop: false
		});
	},
	modEstado:function(pl_op,pl_estado,pl_id,pl_table) {
		if (pl_op=='B') {
			op = 'Desactivar';
			opd = 'Desactivado'
		}else{
			op ='Activar'
			opd = 'Activado'
		}

		swal({
		  title: "Confirmación... ",   
		  text: "Seguro(a) desea  "+op+" estado. ?",
		  icon: "info",
		  buttons: true,
		  dangerMode: true,
		})
		.then((willDelete) => {
		  	if (willDelete) {
			   	$.post('../global/pl_modEstado', {id:pl_id,estado:pl_estado,table:pl_table}, function(data, textStatus, xhr) {
					$("#divEstados_"+pl_id).html(data);
					swal("Confirmación!", "Estado "+opd+" Exitosamente!", "success");
				});
			}
		});
	},
	cerrarVentana: function(){
		$("#lpModalGeneral").modal('hide');
	},
	enviarUrl: function(identificador,url,funcion){
		$(identificador).load(url,funcion);
	},
	trabajando:function(r) {
		const imageURL = '../../init/static/images/trabajando.jpg'
		swal({
		  title: 'Información.!',
		  text: 'Disculpe las molestias estamos trabajando para brindarle una mejor experiencia.',
		  icon: imageURL,
		});
	},
	datoHtml:function() {
		dato = `
			<div id="ejecucionCogs">
				<svg width="40px" height="40px" viewBox="0 0 600 600" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:space="preserve" style="fill-rule:evenodd;clip-rule:evenodd;stroke-linejoin:round;stroke-miterlimit:1.41421;">
				    <rect x="-152" y="-117" width="882" height="819" fill="transparent"/>
				    <g>
				        <circle id="circle-yellow" cx="393.785" cy="409.5" r="100" fill="transparent"/>
				        <g>
				            <path class="cog-yellow" d="M378.75,310.637c-6.476,0.985 -12.839,2.603 -18.999,4.832l0.962,15.729c-5.814,2.455 -11.337,5.551 -16.466,9.229l-12.915,-9.028c-5.115,4.091 -9.817,8.675 -14.036,13.685l8.696,13.14c-3.807,5.034 -7.042,10.476 -9.644,16.226l-15.699,-1.361c-2.385,6.101 -4.165,12.421 -5.314,18.869l14.102,7.032c-0.781,6.263 -0.861,12.593 -0.24,18.874l-14.276,6.671c0.985,6.476 2.604,12.839 4.833,18.998l15.728,-0.961c2.456,5.814 5.551,11.336 9.23,16.465l-9.028,12.915c4.091,5.116 8.674,9.818 13.684,14.037l13.141,-8.697c5.033,3.807 10.475,7.042 16.225,9.645l-1.36,15.699c6.1,2.385 12.42,4.164 18.869,5.313l7.031,-14.101c6.263,0.78 12.594,0.861 18.875,0.239l6.67,14.276c6.476,-0.985 12.84,-2.603 18.999,-4.832l-0.962,-15.729c5.814,-2.455 11.337,-5.551 16.466,-9.229l12.915,9.028c5.116,-4.091 9.817,-8.675 14.036,-13.685l-8.696,-13.14c3.807,-5.034 7.042,-10.476 9.645,-16.226l15.698,1.361c2.385,-6.101 4.165,-12.421 5.314,-18.869l-14.102,-7.032c0.781,-6.263 0.861,-12.593 0.24,-18.874l14.276,-6.671c-0.985,-6.476 -2.604,-12.839 -4.833,-18.998l-15.728,0.961c-2.456,-5.814 -5.551,-11.336 -9.23,-16.465l9.028,-12.915c-4.091,-5.116 -8.674,-9.818 -13.684,-14.037l-13.14,8.697c-5.034,-3.807 -10.476,-7.042 -16.226,-9.645l1.361,-15.699c-6.101,-2.385 -12.421,-4.164 -18.87,-5.313l-7.031,14.101c-6.263,-0.78 -12.594,-0.861 -18.875,-0.239l-6.67,-14.276ZM388.854,390.117c10.698,-2.721 21.592,3.755 24.313,14.452c2.722,10.698 -3.754,21.592 -14.452,24.314c-10.697,2.721 -21.592,-3.755 -24.313,-14.452c-2.721,-10.698 3.754,-21.592 14.452,-24.314Z" fill="#fcbe06"/>
				        </g>
				        <circle id="circle-blue" cx="306.785" cy="190.5" r="100" fill="transparent"/>
				        <g>
				            <path class="cog-blue" d="M291.75,91.637c-6.476,0.985 -12.839,2.603 -18.999,4.832l0.962,15.729c-5.814,2.455 -11.337,5.551 -16.466,9.229l-12.915,-9.028c-5.115,4.091 -9.817,8.675 -14.036,13.685l8.696,13.14c-3.807,5.034 -7.042,10.476 -9.644,16.226l-15.699,-1.361c-2.385,6.101 -4.165,12.421 -5.314,18.869l14.102,7.032c-0.781,6.263 -0.861,12.593 -0.24,18.874l-14.276,6.671c0.985,6.476 2.604,12.839 4.833,18.998l15.728,-0.961c2.456,5.814 5.551,11.336 9.23,16.465l-9.028,12.915c4.091,5.116 8.674,9.818 13.684,14.037l13.141,-8.697c5.033,3.807 10.475,7.042 16.225,9.645l-1.36,15.699c6.1,2.385 12.42,4.164 18.869,5.313l7.031,-14.101c6.263,0.78 12.594,0.861 18.875,0.239l6.67,14.276c6.476,-0.985 12.84,-2.603 18.999,-4.832l-0.962,-15.729c5.814,-2.455 11.337,-5.551 16.466,-9.229l12.915,9.028c5.116,-4.091 9.817,-8.675 14.036,-13.685l-8.696,-13.14c3.807,-5.034 7.042,-10.476 9.645,-16.226l15.698,1.361c2.385,-6.101 4.165,-12.421 5.314,-18.869l-14.102,-7.032c0.781,-6.263 0.861,-12.593 0.24,-18.874l14.276,-6.671c-0.985,-6.476 -2.604,-12.839 -4.833,-18.998l-15.728,0.961c-2.456,-5.814 -5.551,-11.336 -9.23,-16.465l9.028,-12.915c-4.091,-5.116 -8.674,-9.818 -13.684,-14.037l-13.14,8.697c-5.034,-3.807 -10.476,-7.042 -16.226,-9.645l1.361,-15.699c-6.101,-2.385 -12.421,-4.164 -18.87,-5.313l-7.031,14.101c-6.263,-0.78 -12.594,-0.861 -18.875,-0.239l-6.67,-14.276ZM301.854,171.117c10.698,-2.721 21.592,3.755 24.313,14.452c2.722,10.698 -3.754,21.592 -14.452,24.314c-10.697,2.721 -21.592,-3.755 -24.313,-14.452c-2.721,-10.698 3.754,-21.592 14.452,-24.314Z" fill="#006fa2"/>
				        </g>
				        <circle id="circle-red" cx="207.352" cy="357.835" r="100" fill="transparent"/>
				        <g>
				            <path class="cog-red" d="M217.154,258.316c-6.519,-0.642 -13.085,-0.642 -19.604,0l-2.945,15.48c-6.24,0.947 -12.355,2.585 -18.233,4.886l-10.291,-11.933c-5.966,2.703 -11.652,5.986 -16.977,9.801l5.189,14.879c-4.93,3.94 -9.407,8.416 -13.347,13.347l-14.879,-5.189c-3.815,5.325 -7.098,11.011 -9.801,16.977l11.933,10.291c-2.3,5.877 -3.939,11.993 -4.886,18.233l-15.479,2.945c-0.642,6.519 -0.642,13.085 0,19.604l15.479,2.945c0.947,6.24 2.586,12.356 4.886,18.233l-11.933,10.291c2.703,5.966 5.986,11.652 9.801,16.977l14.879,-5.189c3.94,4.931 8.417,9.407 13.347,13.347l-5.189,14.879c5.325,3.815 11.011,7.098 16.977,9.801l10.291,-11.933c5.878,2.301 11.993,3.939 18.233,4.886l2.945,15.479c6.519,0.642 13.085,0.642 19.604,0l2.945,-15.479c6.24,-0.947 12.356,-2.585 18.233,-4.886l10.291,11.933c5.966,-2.703 11.653,-5.986 16.977,-9.801l-5.189,-14.879c4.931,-3.94 9.407,-8.416 13.347,-13.347l14.879,5.189c3.815,-5.325 7.098,-11.011 9.802,-16.977l-11.934,-10.291c2.301,-5.877 3.939,-11.993 4.886,-18.233l15.48,-2.945c0.642,-6.519 0.642,-13.085 0,-19.604l-15.48,-2.945c-0.947,-6.24 -2.585,-12.356 -4.886,-18.233l11.934,-10.291c-2.704,-5.966 -5.987,-11.652 -9.802,-16.977l-14.879,5.189c-3.94,-4.931 -8.416,-9.407 -13.347,-13.347l5.189,-14.879c-5.324,-3.815 -11.011,-7.098 -16.977,-9.801l-10.291,11.933c-5.877,-2.301 -11.993,-3.939 -18.233,-4.886l-2.945,-15.48ZM207.352,337.835c11.038,0 20,8.962 20,20c0,11.038 -8.962,20 -20,20c-11.038,0 -20,-8.962 -20,-20c0,-11.038 8.962,-20 20,-20Z" fill="#e5554e"/>
				        </g>
				    </g>
				</svg>
			</div>
		`;
		return dato
	},
	// mymodal: function(titulo,cuerpo,tamanio,btn_cancelar,callback_cancelar,btn_ok,callback_ok){
	// 	//console.log(titulo,cuerpo,tamanio,btn_cancelar,callback_cancelar,btn_ok,callback_ok); 
	// 	$("#modal-tn-titulo").html(titulo);
		
		
	// 	if(tamanio){
	// 		$(".modal-dialog").attr('style', 'width: 90%');
	// 	}else{
	// 		$(".modal-dialog").removeClass('modal-lg');
	// 	}

	// 	if(btn_cancelar){
	// 		$("#btn_modal_cancelar").show();
	// 	}

	// 	if(callback_cancelar){
	// 		$("#btn_modal_cancelar").unbind('click');
	// 		$("#btn_modal_cancelar").click(function(){
	// 			eval(callback_cancelar);
	// 			$('#obs').val('');
	// 			$('#oculto').hide();
	// 		});
	// 	}
	// 	if(btn_ok){
	// 		$("#btn_modal_ok").html(btn_ok).show();
	// 	}

	// 	if(callback_ok){
	// 		$("#btn_modal_ok").unbind('click');
	// 		$("#btn_modal_ok").click(function(){
	// 			eval(callback_ok);
	// 		});
	// 	}
		
	// 	if (cuerpo) {
	// 		tpl.load_ajax("#modal-tn-body",cuerpo,false);
	// 	}
	// 	$("#modal-tn").modal({
	// 		keyboard: false,
	// 		backdrop: false
	// 	});
	// },
	// mymodalClose: function(){
	// 	$("#modal-tn").modal('hide');
	// },
	// load_ajax: function(selector,url,callback){
	// 	$(selector).load(url,callback);
	// },
	valida_campo: function(campo,mensaje,focus,callback){
		if( $.trim( $('#'+campo).val() ) == '' ){
			if(window.sweetAlert){
				if(focus){
					callback += "$('#"+campo+"').focus();";
				}
				swal({
					type: 'error',
					title: 'Oops...',
					text: mensaje,
					callback: eval(callback),
				});
			}else{
				alert(mensaje);
			}
			return true;			
		}
		return false;
	},
};

lp_global.ready();