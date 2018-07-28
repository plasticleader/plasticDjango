var mapa_lp = document.getElementById("map"),lp_mp;
var lp_js = {
	ready:function () {
	    navigator.geolocation.getCurrentPosition(function(p){
	      lp_js.iniMapa(p.coords.latitude,p.coords.longitude);
	    },this.errcord,{maximumAge: 3000, timeout: 5000, enableHighAccuracy: true});
	},
	iniMapa:function(lat,lon){
		console.log(lat,lon);
		var lp_creaMap = new google.maps.LatLng(lat,lon);
      	var opt = {
        	center: lp_creaMap,
        	zoom: 10,
        	mapTypeId: google.maps.MapTypeId.ROADMAP,  
      	};
      	lp_mp = new google.maps.Map(mapa_lp, opt);
	},
};
lp_js.ready();