// Initialize Firebase
var config = {
  apiKey: "AIzaSyB7p1kN4iedzTUsW02wApELcVyOI5kBFlo",
  authDomain: "ecotravel-1fdee.firebaseapp.com",
  databaseURL: "https://ecotravel-1fdee.firebaseio.com",
  storageBucket: "ecotravel-1fdee.appspot.com",
  messagingSenderId: "649843695207"
};
firebase.initializeApp(config);

function sign_out() {
	firebase.auth().signOut().then(function() {
	  // Sign-out successful.
	}, function(error) {
	  // An error happened.
	});
	window.location.href = '/';
}

$(window).on('load', function(){
	firebase.auth().onAuthStateChanged(function(user) {
	  if (user) {
	    $('.nav').append('<li><a class="page-scroll" href="profile">' + user.email + '</a></li><li><a class="page-scroll" href="javascript:sign_out();">Sign Out</a></li>');
	  } else {
	   	$('.nav').append('<li><a class="page-scroll" href="signin">Sign In</a></li><li><a class="page-scroll" href="signup">Sign Up</a></li>');
	  }
	});

});