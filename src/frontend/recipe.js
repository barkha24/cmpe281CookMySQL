
/*
 * Fetches recipe information from the application server
 * and populate the recipe info box
 */
function recipeInfo( recipeId, userId, token ) {
   requester =  new XMLHttpRequest();
   requester.open( 'GET', 'http://cmpe281p2b-2f1e7577f6424524.elb.us-east-2.amazonaws.com/getRecipe?ownerId=' + userId + '&id=' + recipeId, true );
   requester.setRequestHeader( 'token', token );
   requester.send( null );
   document.getElementById( 'recipeName' ).innerHTML = 'Loading recipe info...';
   requester.onreadystatechange = function() {
	   console.log( requester.status );
	   console.log( 'http-response is' +  requester.response );
       try {
          info = JSON.parse( requester.response );
          console.log( 'app-error is ' + info.error );
          console.log( 'app-response is ' + info.error );
          document.getElementById( 'content' ).innerHTML = '';
          if (info.response.title != undefined) {
             document.getElementById( 'recipeName' ).innerHTML = 'Rendering recipe info...';
             if ( requester.status == 200 ) {
                console.log( 'Received an OK response' );
                document.getElementById( 'recipeName' ).innerHTML = info.response.title;
                for (var i = 0; i < info.response.content.recipeIns.length; i++ ) {
                   document.getElementById( 'content' ).innerHTML += '<div><b>Step ' + i + '</b>. ' + info.response.content.recipeIns[i].instruction + '. <i>Wait ' + info.response.content.recipeIns[i].sleep  +'</i></div>';
                }
             }
          }
      } catch(e) {
      }
   }
}
