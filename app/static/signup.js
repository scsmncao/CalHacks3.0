$(window).on('load', function(){
	$('#signup').click(function() {
		console.log("here");
		window.location.href = "/";
		firebase.auth().createUserWithEmailAndPassword(email, password).catch(function(error) {
		  // Handle Errors here.
		  var errorCode = error.code;
		  var errorMessage = error.message;
		  // ...
		});
	});
});