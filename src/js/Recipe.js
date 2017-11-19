var assert = require( 'assert' );

function Recipe() {
}

Recipe.prototype.instance = function( con, ownerId, title, callback ) {
   /* 
   Recipe class represents a single recipe the user can upload, modify or delete
   */
   var select = 'SELECT * from Recipe where ownerId=? and title= ?';
   console.log( 'Searching for the recipe ' + title );
   con.query( select, [ ownerId, title ],
      function( err, cur ){
         if ( err ) {
            callback( err, nil );
         }
         self = {}
         if( cur.length > 0 ){
            console.log( 'Recipe ' + self.title + ' found.' );
            self.id = cur[0].id;
            self.title = cur[0].title;
            self.ownerId = cur[0].ownerId;
            self.createdOn = cur[0].createdOn;
            self.updatedOn = cur[0].updatedOn;
            self.bucket = cur[0].bucket;
         }
         self.active = true;
         callback( null, self );
      });
}

Recipe.prototype.print = function( self ) {
   /*
    * Print recipe information
    */
   assert.ok( self.active, 'Object is no longer accessible' );
   console.log( 'Recipe Id:', self.id ); 
   console.log( 'Owner Id:', self.ownerId );
   console.log( 'Updated On:', self.updatedOn ); 
   console.log( 'Title:', self.title ); 
   console.log( 'Created On:', self.createdOn ); 
   console.log( 'Updated On:', self.updatedOn ); 
   console.log( 'bucket:', self.bucket ); 
}

Recipe.prototype.titleIs = function( self, title ) {
   /*
    * Update title of the recipe
    */
   assert.ok( self.active, 'Object is no longer accessible' );
   self.title = title;
}

Recipe.prototype.save = function( self, con, callback ) {
   /*
    * Syncs recipe information to database.
    * triggers a callback function once done
    */
   assert.ok( self.active, 'Object is no longer accessible' );
   update = 'UPDATE Recipe set title = ? where id= ?'
   con.query( update, [ self.title, self.id ],
      function( err, cur ) {
         if ( err ) {
            callback( err );
         }
         console.log( 'Recipe updated.' );
         callback( null );
      });
   con.commit();
}

Recipe.prototype.delete = function( self, con, callback ) {
   /*
    * Delete recipe from database.
    * triggers a callback function once done, with a list of recipes
    */
   assert.ok( self.active, 'Object is no longer accessible' );
   var deletes = 'DELETE from Recipe where id=?'
   con.query( deletes, [ self.id ],
      function( err, cur ) {
         if ( err ) {
            callback( err );
         }
         console.log( 'Recipe ' + self.title + ' deleted.' );
         callback( null );
      });
   con.commit();
   self.active = false;
}

Recipe.prototype.instances = function( con, user, callback ) {
   /*
    * Return a list of recipe objects for the user,
    * triggers a callback function once done, with a list of recipes
    */
   var select = 'SELECT * from Recipe where ownerId=?'
   var recipes = []
   con.query( select, [ user.id ],
      function( err, cur ) {
         if ( err ) {
            callback( err, [] );
         }
         for ( var i = 0; i < cur.length; i++ ) {
            self = {}
            self.id = cur[i].id;
            self.ownerId = cur[i].ownerId;
            self.title = cur[i].title;
            self.createdOn = cur[i].createdOn;
            self.updatedOn = cur[i].updatedOn;
            self.bucket = cur[i].bucket;
            self.active = true;
            recipes.push( self );
         }
         console.log( 'Recipes ' + recipes.length + ' fetched' );
         callback( null, recipes );
      });
}
module.exports = Recipe;
