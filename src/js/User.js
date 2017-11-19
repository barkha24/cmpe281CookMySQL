var assert = require( 'assert' );

function User() {
}

User.prototype.instance = function( con, username, callback ) {
   /*
   User represents the user object uploading, modifying and accessing the
   recipe information.
   */
   var select = 'SELECT * from User where username=?'
   console.log( 'Searching for the user ' + username );
   con.query( select, [ username ],
      function( err, cur ){
         self = {}
         if ( err ) {
            callback( err, null );
         }
         if( cur.length > 0 ){
            self.id = cur[0].id;
            self.username = cur[0].username;
            self.dateCreated = cur[0].dateCreated;
            self.active = true;
            console.log( 'User ' + self.username + ' found.' );
         }
         callback( null, self );
      });
}

User.prototype.print = function( self ) {
   /*
    * Print account information
    */
   assert.ok( self.active, 'Object is no longer accessible' );
   console.log( 'Username:', self.username );
   console.log( 'User Id:', self.id ); 
   console.log( 'Created On:', self.dateCreated ); 
}

User.prototype.usernameIs = function( self, username ) {
   /*
    * Update username of the account
    */
   assert.ok( self.active, 'Object is no longer accessible' );
   self.username = username;
}

User.prototype.save = function( self, con, callback ) {
   /*
    * Syncs user information to database.
    * triggers a callback function once done
    */
   assert.ok( self.active, 'Object is no longer accessible' );
   var update = 'UPDATE User set username = ? where id= ?'
   con.query( update, [ self.username, self.id ],
      function( err, cur ) {
         if ( err ) {
            callback( err );
         }
         console.log( 'User updated.' );
         callback( null );
      });
   con.commit();
}

User.prototype.delete = function( self, con, callback ) {
   /*
    * Delete User from database.
    * triggers a callback function once done
    */
   assert.ok( self.active, 'Object is no longer accessible' );
   var deletes = 'DELETE from User where id=?';
   con.query( deletes, [ self.id ],
      function( err, cur ) {
         if ( err ) {
            callback( err );
         }
         console.log( 'User ' + self.username + ' deleted.' );
         callback( null );
      });
   con.commit();
   self.active = false;
}


module.exports = User;
