$(window).on('load', function(){

	$('#signin').click(function() {
		console.log("here");
		var email = $('#email').val();
		var password = $('#password').val();
		firebase.auth().signInWithEmailAndPassword(email, password).catch(function(error) {
		  // Handle Errors here.
		  var errorCode = error.code;
		  var errorMessage = error.message;
		  // ...
		});
	});
});