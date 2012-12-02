$(document).ready(function initialize() {
	var myLatlng = new google.maps.LatLng(50.9241468414, -1.39086340051);
	var mapOptions = {
		center: myLatlng,
		zoom: 13,
		mapTypeId: google.maps.MapTypeId.ROADMAP
	};
	var map = new google.maps.Map(document.getElementById("map_canvas"), mapOptions);
	

	// To add the marker to the map, call setMap();
	$('#sex_both, #sex_male, #sex_female').change(function() {
		if( $("#sex_both").is(":checked") ){
			$.get("/getData?sex=both", function(data){
				var marker1 = new google.maps.Marker({
					position: myLatlng,
					title: data,
					icon: 'http://maps.google.com/mapfiles/ms/icons/yellow-dot.png',
					map: map
				});
			})
		} else if( $("#sex_male").is(":checked") ){
			$.get("/getData?sex=male", function(data){
				
				var marker1 = new google.maps.Marker({
					position: myLatlng,
					title: data,
					icon: 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
					map: map
				});
			})
		} else if( $("#sex_female").is(":checked") ){
			$.get("/getData?sex=female", function(data){
				var marker1 = new google.maps.Marker({
					position: myLatlng,
					title: data,
					icon: 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
					map: map
				});
			})
		} 
		
	});
});

