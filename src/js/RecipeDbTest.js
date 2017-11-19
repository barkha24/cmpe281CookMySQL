var assert = require( 'assert' );
var RecipeDb = require( './RecipeDb' );
var Recipe = require( './Recipe' );
var User = require( './User' );
var async = require( 'async' );

function testUser() {
   /*
    * test User module
    */
   console.log( 'Test #1' );
   console.log( 'Staring database connection...' );
   var db = new RecipeDb();
   console.log( 'Creating a new user bobby' );
   db.insertUser( 'bobby', function( err ) {
      if ( err ) {
         throw(err);
      }
      user = new User();
      user.instance( db.con, 'bobby', function( err, account ) {
         if ( err ) {
            throw(err);
         }
         user.print( account );
         console.log( 'Deleting the new user' );
         user.delete( account, db.con, function( err ) {
            if ( err ) {
               throw(err);
            }
            console.log( 'Verifying that the user object is not accessible' );
            try {
               user.print( account );
               throw new Error( 'Exception not thrown' );
            } catch(err) {} 
            console.log( 'Closing database connection...' );
            db.disconnect();
         });
      });
   });
}

function accountCompare( account1, account2) {
   console.log( 'Verify that the id is the same ' + account1.id.toString() );
   assert.equal( account1.id, account2.id );
}

function testUserRename() {
   /*
    * More detailed testing of User module.
    * Renames the User
    */
   console.log( 'Test #2' );
   console.log( 'Staring database connection...' );
   var db = new RecipeDb();
   console.log( 'Create a user charles' );
   db.insertUser( 'charles', function( err ) {
      if ( err ) {
         throw(err);
      }
      user = new User();
      user.instance( db.con, 'charles', function( err, account ) {
         if (err){
            throw(err);
         }
         console.log( 'Rename user to Charlie' );
         user.print( account );
         user.usernameIs( account, 'Charlie' )
         console.log( 'Update changes to database' );
         user.save( account, db.con, function( err ) {
            if (err){
               throw(err);
            }
            console.log( 'Fetch this user' );
            user.instance( db.con, 'Charlie', function( err, copy ) {
               if (err) {
                  throw(err);
               }
               accountCompare( account, copy );
               console.log( 'Delete the user' );
               user.delete( account, db.con, function( err ) {
                  if (err) {
                     throw(err);
                  }
                  console.log( 'Closing database connection...' );
                  db.disconnect();
               });
            });
         });
      });
   });
}

function testRecipes() {
   /*
    * Test Recipe Module, try creating some recipes
    * and map it to a test user.
    */
   console.log( 'Test #3' );
   console.log( 'Staring database connection...' );
   var db = new RecipeDb();
   console.log( 'Creating a new user Karl' );
   db.insertUser( 'Karl', function( err ) {
      if ( err ) {
         throw( err );
      }
      var titles = [];
      user = new User();
      user.instance( db.con, 'Karl', function( err, account ) {
         if (err) {
            throw( err );
         }
         for ( var i = 0; i < 10; i++ ) {
            titles.push( 'recipe' + i.toString() );
         }
         async.each(titles, function( title, callback ) {
               console.log( 'Creating a new recipe' );
               db.insertRecipe( account.id, title, callback );
            }, function( err ) { 
               console.log( 'Done creating recipes' );
               if( err ) {
                  throw( err );
               }
               recipe = new Recipe;
               var recipes = recipe.instances( db.con, account,
                  function( err, recipes ) {
                     if (err) {
                        throw(err);
                     }
                     assert.equal( recipes.length, 10 );
                     async.each(recipes, function(r, callback) {
                        console.log( 'Deleting the recipe' );
                        recipe.delete( r, db.con, function( err ) {
                           callback( err );
                        });
                        }, function( err ) {
                           console.log( 'Done!');
                           if (err ){
                              throw(err);
                           }
                           user.delete( account, db.con, function( err ) {
                              if (err) {
                                 throw(err);
                              }
                              console.log( 'Closing database connection...' );
                              db.disconnect();
                           });
                     });
                  });
               });
      });
   });
}

function main() {
   testUser();
   testUserRename();
   testRecipes();
}

main();
