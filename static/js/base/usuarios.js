var lp_users = {
	ready:function() {
		// body...
	},
	actualizar:function(op,id) {
		if (op=='B') {
			op = 'Bloquear';
			opd = 'Bloqueado(a)'
		}else{
			op ='Activar'
			opd = 'Activado(a)'
		}


		swal({
		  title: "Confirmación... ",   
		  text: "Seguro(a) desea  "+op+" este usuario?",
		  icon: "info",
		  buttons: true,
		  dangerMode: true,
		})
		.then((willDelete) => {
		  	if (willDelete) {
			   	$.post('actualizar', {op:op,id:id}, function(data, textStatus, xhr) {
					$("#divUsers_"+id).html(data);
					swal("Confirmación!", "Usuario "+opd+" Exitosamente!", "success");
				});
			}
		});	
	},
};
lp_users.ready();