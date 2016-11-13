$(window).on('load', function(){

	var database = firebase.database();

	$('#signup').click(function() {
		console.log("here");
		var email = $('#email').val();
		var password = $('#password').val();
		firebase.auth().createUserWithEmailAndPassword(email, password).catch(function(error) {
		  // Handle Errors here.
		  var errorCode = error.code;
		  var errorMessage = error.message;
		  console.log(errorMessage);
		  // ...
		});
		writeUserData(email);
	});

	function writeUserData(email) {
		firebase.database().ref('users/' + email.split("@")[0]).set({
			'green_points': 0
		});
	}
});