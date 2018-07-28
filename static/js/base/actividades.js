var lp_activ = {
	ready:function () {
		// $(".modal").modal({
		// 	keyboard: false,
		// 	backdrop: false
		// });
	},
	imagen:function(r) {
		lp_global.crearVentana('Imagenes','imagenes?id='+r+'','mod_al-lg');
	},
};

lp_activ.ready();