function uploadFile( ownerId, token ) {
   requester =  new XMLHttpRequest();
   var data = new FormData();
   requester.open( 'POST', 'http://cmpe281p2b-2f1e7577f6424524.elb.us-east-2.amazonaws.com/fileUpload', true );
   requester.setRequestHeader( 'token', token );
   data.append( 'ownerId', ownerId );
   data.append( 'file', document.getElementById("file").files[0] );
   data.append( 'recipeTitle', document.getElementById("recipeTitle").value );
   requester.send( data );
   requester.onreadystatechange = function() {
	   console.log( requester.status );
	   console.log( 'response :' +  requester.response );
	   if ( requester.status == 200 ) {
		  console.log( 'Received an OK response' );
		  info = JSON.parse( requester.response );
		  console.log( 'error is ' + info.error );
		  console.log( 'result is ' + info.result );
	   }
	   console.log( 'Returning to main page' );
	   window.location.href = "http://dock2.hyunwookshin.com:8044/add-recipe.php?userId=" + ownerId + "&token=" + token;
   }
}
