/*
 * Fetches recipes informations for the user
 * And add dynamic handles for view, name, delete
 */
function getRecipes( userId, token ) {
   requester =  new XMLHttpRequest();
   requester.open( 'GET', 'http://dock2.hyunwookshin.com:8084/getRecipes?ownerId=' + userId, true );
   requester.setRequestHeader( 'token', token );
   requester.send( null );
   requester.onreadystatechange = function() {
       try {
          console.log( requester.status );
          console.log( 'response :' +  requester.response );
          info = JSON.parse( requester.response );
          console.log( 'app-error is ' + info.error );
          console.log( 'app-response is ' + info.response.length );
          console.log( 'error is ' + info.error );
          if ( requester.status == 200 ) {
             console.log( 'Received an OK response' );
          }
          for (var i = 0; i <  info.response.length; i++ ) {
             console.log( 'Recipe:' + info.response[i] );
             document.getElementById( 'row' + i.toString() ).style.display = "";
             document.getElementById( 'name' + i.toString() ).innerHTML = info.response[i].title;
             document.getElementById( 'view' + i.toString() ).setAttribute(
                   'onclick', "window.location= 'view-recipe.php?recipeId=" + info.response[i].id + "&userId=" + userId + "&token=" + token+ "'");
             document.getElementById( 'delete' + i.toString() ).setAttribute(

                   'onclick', "deleteRecipe('" + userId + "','" + info.response[i].title + "','" +  token + "');");
             document.getElementById( 'play' + i.toString() ).style.display = "";
          }
       } catch(e) {
          console.log( e );
       }
   }
}
