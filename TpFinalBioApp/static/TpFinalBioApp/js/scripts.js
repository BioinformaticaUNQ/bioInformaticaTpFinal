
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
            
            marker = new google.maps.Marker({
                position: new google.maps.LatLng(markers[i].latitude, markers[i].longitude),
                map: map,
                draggable: false
            });
            google.maps.event.addListener(marker, 'click', (function(marker, i) {
            return function() {
                infowindow.setContent("<div style='padding-bottom: 12px;'>" + markers[i].titulo + "</div><div ><img style='display:block;margin: auto;' src=" + markers[i].arbol + "></div>");
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