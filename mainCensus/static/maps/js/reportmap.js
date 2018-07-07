	var mymap = L.map('address').setView([-0.3976933016545059,36.96074903011323], 13);

	var marker = new L.Marker([-0.3976933016545059,36.96074903011323]);

	marker.bindPopup('This is where we are located').openPopup();
	marker.addTo(mymap)

	L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox.streets',
    accessToken: 'pk.eyJ1IjoiaXJ1bmd1YXl1YiIsImEiOiJjamZ4cWk3cjIxbWp5MnJxcXkyazh2NXRnIn0.7BFq1ew_8pN519OPTbGRMQ'}).addTo(mymap);

     // Geolocation Section
	 mymap.locate({setView: true,maxZoom:20});
	 function onLocationFound(e){
	 	var radius = e.accuracy / 2
	 	console.log(radius);
	 	alert(e.latlng);
	 	L.Marker(e.latlng).addTo(mymap).bindPopup('You are within ' + radius + 'meters from this point').openPopup();
	 	L.circle(e.latlng,radius).addTo(mymap);
	 }
	 mymap.on('locationfound',onLocationFound);
	 function onLocationError(e){
	 	alert(e.message);
	 }
	 mymap.on('locationerror',onLocationError);


	 // 
	 	<script type="text/javascript">
			function layer(map,options){
				
				// L.marker([-0.023, 37.5]).addTo(map);
				var osm = new L.TileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png');
                var opentopomap = new L.TileLayer('http://{s}.tile.opentopomap.org/{z}/{x}/{y}.png');
                var arcon = new L.tileLayer('http://server.arcgisonline.com/ArcGis/rest/services/World_Imagery/Mapserver/tile/{z}/{y}/{x}');
				var datasets = new L.GeoJSON.AJAX("{% url 'incidentdata' %}",{
					 onEachFeature: function layerpopup(feature,layer){
	                    layer.bindPopup(feature.properties.description.toString())
	                            }
				});

				datasets.addTo(map);
				var baseLayers = {
                        'OSM':osm
                        }
                var groupedOverlays = {
                        "layers": {
                        	"Incident Posts":datasets,
                        	"OpenTopoMap":opentopomap,
                        	"Imagery": arcon
                        		
                       	}
                    };
                 L.control.groupedLayers(baseLayers,groupedOverlays).addTo(map);
                 L.Control.geocoder().addTo(map);

                 L.Routing.control({
                    waypoints:[
                        L.latLng(-0.23,36.87),
                        L.latLng(0.23,37.64)
                        	],
                        	routeWhileDragging:true,
                        	geocoder:L.Control.Geocoder.nominatim()
                    }).addTo(map);

			}
		</script>


		// 	<script type="text/javascript" src="{%static 'js/incident.js' %}"></script>
	<script type="text/javascript" src="{%static 'js/form.js' %}"></script>
	<script type="text/javascript" src="{%static 'maps/reportmap.js' %}"></script>
	<script type="text/javascript" src="{%static 'js/jquery-3.2.1.min.js' %}"></script>
	<script type="text/javascript" src="{%static 'js/bootstrap.js' %}"></script>
	<script  src="{%static 'js/leaflet.ajax.min.js' %}"></script>
	<script type="text/javascript" src="{%static 'js/leaflet.groupedlayercontrol.min.js' %}"></script>
	<script type="text/javascript" src="{%static 'routing/leaflet-routing-machine.js' %}"></script>
	<script type="text/javascript" src="{%static 'leaflet/Control.Geocoder.js' %}"></script>
	<script src="{%static 'js/modernizr-2.6.2.min.js' %}"></script>
	<script src="{%static 'js/jquery.min.js' %}"></script>
	<script src="{%static 'js/jquery.easing.1.3.js' %}"></script>
	<script src="{%static 'js/jquery.waypoints.min.js' %}"></script>
	<script src="{%static 'js/jquery.stellar.min.js' %}"></script>
	<script src="{%static 'js/jquery.flexslider-min.js' %}"></script>
	<script src="{%static 'js/main.js' %}"></script>
	<script type="text/javascript" src="{%static 'js/wow.min.js' %}"></script>
       	<script>
              new WOW().init();
    	</script>

  <link rel="stylesheet" type="text/css" href="{%static 'css/index.css' %}">
	<link rel="stylesheet" type="text/css" href="{%static 'css/usalama.css' %}">
	<link rel="stylesheet" type="text/css" href="{%static 'css/main.css' %}">
	<link rel="stylesheet" href="{%static 'css/style.css' %}">
	<link rel="stylesheet" type="text/css" href="{%static 'css/bootstrap.css' %}">
	<link rel="stylesheet" type="text/css" href="{%static 'hchart/css/highcharts.css' %}">
	<link rel="stylesheet" type="text/css" href="{%static 'font-awesome/css/font-awesome.min.css' %}">
	<link rel="stylesheet" type="text/css" href="{%static 'css/animate.min.css' %}">
	<link rel="stylesheet" type="text/css" href="{%static 'routing/leaflet-routing-machine.css' %}">
	<link rel="stylesheet" type="text/css" href="{%static 'css/leaflet.groupedlayercontrol.min.css' %}">
	<link rel="stylesheet" type="text/css" href="{%static 'leaflet/Control.Geocoder.css' %}">
	<!-- slider -->
	<link rel="shortcut icon" href="favicon.ico">
	<link rel="stylesheet" href="{%static 'css/animate.css' %}">
	<link rel="stylesheet" href="{%static 'css/flexslider.css' %}">
	<link rel="stylesheet" href="{%static 'css/icomoon.css' %}">