var map;
function initMap() {
	var churchLocationGA = {lat: 36.027355, lng: -78.890249},
		centerPoint = {lat: 36.031079, lng: -78.891170};

	map = new google.maps.Map(document.getElementById('googleMap'), {
		'center' : centerPoint,
		'zoom' : 12,
		'mapTypeId' : google.maps.MapTypeId.ROADMAP,
		'draggable' : false,
		'scrollwheel' : false
	});

	var popupContentGA = 'Deeperlife Bible Church Gwinnett<br>';
	    popupContentGA += '990 Lakes Parkway<br>';
			popupContentGA += 'Lawrenceville<br>';
	    popupContentGA += 'GA 30043';


	var infowindowGA = new google.maps.InfoWindow({
			content: popupContentGA });

	var markerGA = new google.maps.Marker({
			'position': churchLocationGA,
			'map': map,
			'title': 'Deeperlife Bible Church Gwinnett, GA'
		});

	markerGA.addListener('click', function() {
		infowindowGA.open(map, markerGA);
	});
}

function geocodeAddress(address) {
	var geocoder = new google.maps.Geocoder();

	geocoder.geocode({'address': address}, function(results, status) {
		if (status === google.maps.GeocoderStatus.OK) {
			console.log('Geocoded address: ', results[0].geometry.location.toString());
		} else {
			alert('Geocode was not successful for the following reason: ' + status);
		}
	});
}