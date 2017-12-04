/*
 * Java script for deleting recipes
 * Once the delete call is finished
 * redirect to add recipe page
 */
function deleteRecipe( userId, recipeTitle, token ) {
   requester =  new XMLHttpRequest();
   requester.open( 'POST', 'http://cmpe281p2b-2f1e7577f6424524.elb.us-east-2.amazonaws.com/fileDelete', true );
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
