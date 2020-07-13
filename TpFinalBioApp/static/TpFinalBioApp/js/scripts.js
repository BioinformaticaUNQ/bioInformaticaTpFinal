
$(function(){
	
	function initialize(){
        var m = document.getElementById("myVar").value;
        var markers = JSON.parse(m);
        var latlngbounds = new google.maps.LatLngBounds();
        var quilmes = {
            lat : -34.720634,
            lng : -58.254605
        };
		var map = new google.maps.Map(document.getElementById('mapa'), {
            mapTypeId: google.maps.MapTypeId.ROADMAP,
            center : quilmes,
            zoom : 12
        });

        var infowindow = new google.maps.InfoWindow();
        var marker, i;
        for (i = 0; i < markers.length; i++) {
            console.log(markers[i]['fields'])
            marker = new google.maps.Marker({
                position: new google.maps.LatLng(markers[i]['fields'].latitud, markers[i]['fields'].longitud),
                map: map,
                draggable: false
            });
            google.maps.event.addListener(marker, 'click', (function(marker, i) {
            return function() {
                infowindow.setContent("hola");
                infowindow.open(map, marker);
            }
            })(marker, i));
            latlngbounds.extend(marker.position);
        }
        var bounds = new google.maps.LatLngBounds();
        map.setCenter(latlngbounds.getCenter());
        map.fitBounds(latlngbounds);
    }
    google.maps.event.addDomListener(window, 'load', initialize());
});