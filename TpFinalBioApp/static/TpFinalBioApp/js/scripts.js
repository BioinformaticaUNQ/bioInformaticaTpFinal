
$(function(){
	
	function initialize(){
        var m = document.getElementById("myVar").value;
        var markers = JSON.parse(m);
        if(markers.length > 0){
            var latlngbounds = new google.maps.LatLngBounds();
        }
        var quilmes = {
            lat : -34.720634,
            lng : -58.254605
        };
		var map = new google.maps.Map(document.getElementById('mapa'), {
            mapTypeId: google.maps.MapTypeId.ROADMAP,
            center : quilmes,
            zoom : 8
        });

        var infowindow = new google.maps.InfoWindow();
        var marker, i;
        for (i = 0; i < markers.length; i++) {
            marker = new google.maps.Marker({
                position: new google.maps.LatLng(markers[i]['fields'].latitud, markers[i]['fields'].longitud),
                map: map,
                draggable: false
            });
            google.maps.event.addListener(marker, 'mouseover', (function(marker, i) {
            return function() {
                infowindow.setContent("<div style='padding-bottom: 8px;'>" + markers[i]['fields'].source + "</div>" +
                                      "<div style='text-align: center; padding-bottom: 8px;background-color: #26a69a;'>" + markers[i]['fields'].bio_id + "</div>" +
                                      "<div style='text-align: center;'>" + markers[i]['fields'].date + "</div>");
                infowindow.open(map, marker);
            }
            })(marker, i));
            marker.addListener('mouseout', function() {
                infowindow.close();
            });
            latlngbounds.extend(marker.position);
        }
        if(markers.length > 0){
            map.setCenter(latlngbounds.getCenter());
            map.fitBounds(latlngbounds);
        }
        
    }
    google.maps.event.addDomListener(window, 'load', initialize());
});

$(function() {
    var acc = document.getElementsByClassName("accordion");
    var i;

    for (i = 0; i < acc.length; i++) {
        acc[i].addEventListener("click", function() {
            /* Toggle between adding and removing the "active" class,
            to highlight the button that controls the panel */
            this.classList.toggle("active");

            /* Toggle between hiding and showing the active panel */
            var panel = this.nextElementSibling;
            if (panel.style.display === "block") {
            panel.style.display = "none";
            } else {
            panel.style.display = "block";
            }
        });
    }
});