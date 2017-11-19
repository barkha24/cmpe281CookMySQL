var RecipeDb = require( './RecipeDb' );
var Recipe = require( './Recipe' );
var User = require( './User' );


function createRecipe( db, account, title, callback ) {
   db.insertRecipe( account.id, title, function( err ) {
      if ( err ) {
         callback( err, null );
      }
      recipe = new Recipe;
      recipe.instance( db.con, account.id, title, function( err, instance ) {
         if ( err ) {
            callback( err, null );
         }
         recipe.print( instance );
         callback( instance, account );
      });
   });
}

function createRecipeByName( db, username, title, callback ) {
   user = new User();
   user.instance( db.con, username, function( err, account ) {
      if ( err ) {
         callback( err, null );
      }
      user.print( account );
      createRecipe( db, account, title, callback );
   });
}

function deleteRecipeAndUser( con, recipeInstance, account, callback ) {
   recipe = new Recipe();
   // Delete recipe first!
   recipe.delete( recipeInstance, con, function( err ) {
      if ( err ) {
         callback( err );
      }
      user = new User();
      user.delete( account, con, function( err ) {
         callback( err );
      });
   });
}

function example() {
   var db = new RecipeDb();
   db.insertUser( 'james.brown', function( err ) {
      if ( err ) {
         throw(err);
      }
      createRecipeByName( db, 'james.brown', 'Noodle Soup',
         function( recipeInstance, account ) {
           // Recipe and account created
            deleteRecipeAndUser( db.con, recipeInstance, account,
              function( err ) {
                 // Recipe and account deleted
                 if ( err ) {
                    throw(err);
                 }
                 db.disconnect();
              });
         });
   });
}

example();
