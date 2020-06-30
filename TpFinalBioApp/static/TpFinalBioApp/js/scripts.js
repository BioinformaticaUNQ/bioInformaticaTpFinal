
$(function(){
	
	function initialize(){
        var markers = JSON.stringify(document.getElementById("myVar").value);
        console.log(markers);
        var quilmes = {
            lat : -34.720634,
            lng : -58.254605
        };
		var map = new google.maps.Map(document.getElementById('mapa'), {
            mapTypeControl : false,
            center : quilmes,
            zoom : 12
        });

        var infowindow = new google.maps.InfoWindow();
        var marker, i;
        for (i = 0; i < markers.size; i++) {  
            marker = new google.maps.Marker({
                position: new google.maps.LatLng(markers[i][1], markers[i][2]),
                map: map,
                draggable: false
            });
            google.maps.event.addListener(marker, 'click', (function(marker, i) {
            return function() {
                infowindow.setContent(markers[i][0]);
                infowindow.open(map, marker);
            }
            })(marker, i));
        }
    }
    google.maps.event.addDomListener(window, 'load', initialize());
});