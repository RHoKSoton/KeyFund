$(document).ready(function initialize() {
	var myLatlng = new google.maps.LatLng(54.913822, -1.400493);
	var mapOptions = {
		center: myLatlng,
		zoom: 6,
		mapTypeId: google.maps.MapTypeId.ROADMAP
	};
	var map = new google.maps.Map(document.getElementById("map_canvas"), mapOptions);
	var markerArray = [];

	// To add the marker to the map, call setMap();
	$('#sex_both, #sex_male, #sex_female').change(function() {
		for (var i = 0; i < markerArray.length; i++) {
			markerArray[i].setMap(null);
		}
		
		if( $("#sex_both").is(":checked") ){
			$.get("/getData?sex=both", function(data){
				data = data.replace(/'/g, "\"")
				var obj = jQuery.parseJSON(data);
				
				count = 0;
				while (true) {
					if(obj[count] != undefined) {
						lat = obj[count].lat;
						long = obj[count].long;
						var marker_pos = new google.maps.LatLng(parseInt(lat), parseInt(long));
						++count;
						var marker = new google.maps.Marker({
							position: marker_pos,
							title: data,
							icon: 'http://maps.google.com/mapfiles/ms/icons/red-dot.png',
							map: map
						});
						markerArray.push(marker);
					} else {
						break
					}
				}
			})
		} else if( $("#sex_male").is(":checked") ){
			$.get("/getData?sex=male", function(data){
				data = data.replace(/'/g, "\"")
				var obj = jQuery.parseJSON(data);
				
				count = 0;
				while (true) {
					if(obj[count] != undefined) {
						lat = obj[count].lat;
						long = obj[count].long;
						var marker_pos = new google.maps.LatLng(parseInt(lat), parseInt(long));
						++count;
						var marker = new google.maps.Marker({
							position: marker_pos,
							title: data,
							icon: 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
							map: map
						});
						markerArray.push(marker);
					} else {
						break
					}
				}
			})
		} else if( $("#sex_female").is(":checked") ){
			$.get("/getData?sex=female", function(data){
				data = data.replace(/'/g, "\"")
				var obj = jQuery.parseJSON(data);
				
				count = 0;
				while (true) {
					if(obj[count] != undefined) {
						lat = obj[count].lat;
						long = obj[count].long;
						var marker_pos = new google.maps.LatLng(parseInt(lat), parseInt(long));
						++count;
						var marker = new google.maps.Marker({
							position: marker_pos,
							title: data,
							icon: 'http://maps.google.com/mapfiles/ms/icons/pink-dot.png',
							map: map
						});
						markerArray.push(marker);
					} else {
						break
					}
				}
			})
		} 
		
	});
});

