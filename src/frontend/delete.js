/*
 * Java script for deleting recipes
 * Once the delete call is finished
 * redirect to add recipe page
 */
function deleteRecipe( userId, recipeTitle, token ) {
   requester =  new XMLHttpRequest();
   requester.open( 'POST', 'http://dock2.hyunwookshin.com:8084/fileDelete', true );
   requester.setRequestHeader( 'token', token );
   var data = new FormData();
   data.append( 'fileName', recipeTitle );
   data.append( 'ownerId', userId );
   requester.send( data );
   requester.onreadystatechange = function() {
	   console.log( requester.status );
	   console.log( 'http-response is' +  requester.response );
       window.location= 'add-recipe.php?userId=' + userId +"&token=" + token ;
   }
}
