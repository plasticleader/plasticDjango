var login = {
	ready:function() {
		$('#m_login_signin_submit').click(function(event) {
			var email = $('#emailIngreso').val();
			var pass = $('#passwordIngreso').val();
			if (email=='') {
				swal("Campo Vacio","Debe ingresar un usuario","warning")
					.then((value) => {
					   $('#emailIngreso').focus();
				});
				return false;
			}else if (pass=='') {
				swal("Campo Vacio","Debe ingresar un password","warning")
					.then((value) => {
					   $('#passwordIngreso').focus();
				});
				return false;
			}else{
				$.post('../ingresoUsuario', {email:email,contrasena:pass}, function(data, textStatus, xhr) {
					if (data=='usuario') {
					swal("Usuario Invalido","Verifique el usuario ingresado","error")
						.then((value) => {
						   $('#emailIngreso').focus();
					});
					return false;
					}else if (data=='invalido') {
						swal("Información Invalida","Usuario/Password errados","error")
							.then((value) => {
							   $('#emailIngreso').focus();
						});
						return false;
					}else{
						swal("Bienvenido(a)\n"+data+"\nA Tu Acuerdo.com"," Click  para continuar.","success")
							.then((value) => {
							window.location.href = '../index';   
						});
					}
				});
				return false;
			}
		});	

		$('#btnVerificar').click(function(event) {
			$('#bodyLogin').hide();
			$('#bodyVerificar').show();
			$('#inputVericacion').val('');
			$('#inputVericacion').focus();
		});
		$('#btnVolverLogin').click(function(event) {
			$('#bodyVerificar').hide();
			$('#bodyLogin').show();
			$('#emailIngreso').val('');
			$('#passwordIngreso').val('');
			$('#emailIngreso').focus();
		});

		$('#m_verificar_signin_submit').click(function(event) {
			var identificacion = $('#inputVericacion').val();
			if (identificacion=='') {
				swal("Campo Vacio","Debe ingresar un número de identificación","warning")
					.then((value) => {
					   $('#inputVericacion').focus();
				});
				return false;
			}else{
				$.post('../validarIdentificacion', {identificacion:identificacion}, function(data, textStatus, xhr) {
					if (data=='usuario') {
					swal("Usuario Invalido","Verifique el usuario ingresado","error")
						.then((value) => {
						   $('#emailIngreso').focus();
					});
					return false;
					}else if (data=='invalido') {
						swal("Información Invalida","Usuario/Password errados","error")
							.then((value) => {
							   $('#emailIngreso').focus();
						});
						return false;
					}else{
						swal("Bienvenido(a)\n"+data+"\nA Tu acuerdo.com "," Click  para continuar.","success")
							.then((value) => {
							// window.location.href = '../index';   
						});
					}
				});
				return false;
			}
		});	
	},
	verificar:function(){

	}
};
login.ready();
