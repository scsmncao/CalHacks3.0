// Initialize Firebase
var config = {
  apiKey: "AIzaSyB7p1kN4iedzTUsW02wApELcVyOI5kBFlo",
  authDomain: "ecotravel-1fdee.firebaseapp.com",
  databaseURL: "https://ecotravel-1fdee.firebaseio.com",
  storageBucket: "ecotravel-1fdee.appspot.com",
  messagingSenderId: "649843695207"
};
firebase.initializeApp(config);

$(window).on('load', function(){

  var map;

  var departure;
  var destination;

  function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
      zoom: 3,
      center: {lat: 37.0902, lng: -119.417931},
      mapTypeId: 'terrain',
      disableDefaultUI: true
    });
  }
  initMap();

  function placeMarker(departure, destination) {

    var geocoder = new google.maps.Geocoder();

    geocoder.geocode({'address': departure}, function(results, status) {
      if (status === 'OK') {
        map.setCenter(results[0].geometry.location);
        var marker = new google.maps.Marker({
          map: map,
          position: results[0].geometry.location,
          icon: '../static/images/plane.png'
        });
        departureCoord = results[0].geometry.location;
        geocoder.geocode({'address': destination}, function(results, status) {
          if (status === 'OK') {
            map.setCenter(results[0].geometry.location);
            var marker = new google.maps.Marker({
              map: map,
              position: results[0].geometry.location,
              icon: '../static/images/plane.png'
            });
            drawPath(departureCoord, results[0].geometry.location)
          } else {
            alert('Geocode was not successful for the following reason: ' + status);
          }
        });
      } else {
        alert('Geocode was not successful for the following reason: ' + status);
      }
    });

    // var marker = new google.maps.Marker({
    //       position: myLatLng,
    //       map: map,
    //       title: 'Hello World!'
    //     });
  }

  function drawPath(departure, destination) {
    console.log(departure);
    var flightPlanCoordinates = [
      departure,
      destination
    ];
    var flightPath = new google.maps.Polyline({
      path: flightPlanCoordinates,
      geodesic: true,
      strokeColor: '#000000',
      strokeOpacity: 1.0,
      strokeWeight: 5
    });

    flightPath.setMap(map);
  }


  $("#from").keyup(function() {
    var search = $("#from").val()
    console.log(search);
    if (search != "") {
      $.ajax({
        url: "https://api.sandbox.amadeus.com/v1.2/airports/autocomplete?apikey=R26ZAzuBsJnmMFFX2RVh0qEK2PpDLgPx&term=" + search,
        success: function(result) {
          console.log(result);
          var codes = []
          for (var i = 0; i < result.length; i++) {
            console.log(result[i]['value'])
            if (i > 5) {
              break;
            }
            codes.push({label: result[i]['label'], value:result[i]['value']});
          }
          console.log(codes);
          $('#from').autocomplete({
            source: codes
          });
        }
      });
    }
  });

  $("#to").keyup(function() {
    var search = $("#to").val()
    console.log(search);
    if (search != "") {
      $.ajax({
        url: "https://api.sandbox.amadeus.com/v1.2/airports/autocomplete?apikey=R26ZAzuBsJnmMFFX2RVh0qEK2PpDLgPx&term=" + search,
        success: function(result) {
          console.log(result);
          var codes = []
          for (var i = 0; i < result.length; i++) {
            console.log(result[i]['value'])
            if (i > 5) {
              break;
            }
            codes.push({label: result[i]['label'], value:result[i]['value']});
          }
          console.log(codes);
          $('#to').autocomplete({
            source: codes
          });
        }
      });
    }
  });

  $( "#departure" ).datepicker({
    autoclose: true,
    todayHighlight: true,
    orientation: "bottom"
  });

  $( "#return" ).datepicker({
    autoclose: true,
    todayHighlight: true,
    orientation: "bottom"
  });

  $('.people').selectpicker({
    dropupAuto: false
  });

  $('#search').click(function() {
    var link = "/results?";
    link += "from=" + $('#from').val();
    link += "&to=" + $('#to').val();
    link += "&departure_date=" + $('#departure').val();
    link += "&return_date=" + $('#return').val();
    link += "&adults=" + $('.adults').find(":selected").text();
    link += "&children=" + $('.children').find(":selected").text();
    link += "&infants=" + $('.infants').find(":selected").text();
    window.location.href = link;
  });

  // $('#from').focusout(function() {
  //   placeMarker($('#from').val(), "departure");
  // });

  $('#to').focusout(function() {
    placeMarker($('#from').val(), $('#to').val());
  });

});