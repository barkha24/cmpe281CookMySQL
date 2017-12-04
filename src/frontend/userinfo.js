/*
 * Fetches user information from the application server
 * and populate the user info box
 */
function userInfo( userId, token, callback ) {
   requester =  new XMLHttpRequest();
   requester.open( 'GET', 'http://cmpe281p2b-2f1e7577f6424524.elb.us-east-2.amazonaws.com/userInfo?userId=' + userId, true );
   requester.setRequestHeader( 'token', token );
   requester.send( null );
   document.getElementById( 'name' ).innerHTML = 'Loading user info...';
   requester.onreadystatechange = function() {
	   console.log( requester.status );
	   console.log( 'http-response is' +  requester.response );
       try {
          info = JSON.parse( requester.response );
          console.log( 'app-error is ' + info.error );
          console.log( 'app-response is ' + info.error );
          if (info.response.firstname != undefined) {
             document.getElementById( 'name' ).innerHTML = 'Rendering user info...';
             if ( requester.status == 200 ) {
                console.log( 'Received an OK response' );
             }
             document.getElementById( 'name' ).innerHTML = info.response.firstname + ' ' + info.response.lastname;
             document.getElementById( 'mobile' ).innerHTML = info.response.mobile;
             document.getElementById( 'username' ).innerHTML = info.response.username;
             callback( userId, token );
          }
      } catch(e) {
      }
   }
}
