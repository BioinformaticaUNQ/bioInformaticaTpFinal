
$(function(){
	
	function initialize(){
        var m = document.getElementById("myVar").value;
        var markers = JSON.parse(m);
        console.log('askdkado:' , markers.length)
        
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
                infowindow.setContent("<div style='float:left'><img src='http://i.stack.imgur.com/g672i.png'></div><div style='float:right; padding: 10px;'></div>");
                infowindow.open(map, marker);
            }
            })(marker, i));
        }
    }
    google.maps.event.addDomListener(window, 'load', initialize());
});