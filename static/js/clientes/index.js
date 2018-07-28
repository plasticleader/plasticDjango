var str_cargando = {
	ready:function() {
		this.documentos()
	},
	documentos:function() {},
	ejecutar:function (strs_nombre) {
		var html = `
			<h5>Ya éxite una campaña con el nombre: `+strs_nombre+`</h5>
			<a href="/crearCampanasFalabella">Intentalo de nuevo con otro nombre</a>
		`;
		swal({
		  type: 'error',
		  title: 'Oops... algo va mal',
		  html:html,
		  width: '80%',
		  padding: '10em',
		  showConfirmButton:false,
		  showCloseButton:false,
		  allowOutsideClick:false,
		  allowEscapeKey:false,
		});
	},
};
str_cargando.ready();