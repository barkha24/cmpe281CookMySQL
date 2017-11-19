// node.js rds/mysql application

var mysql = require( 'mysql' );
var assert = require( 'assert' );
var User = require( './User' );
var Recipe = require( './Recipe' );

MYSQL_HOST = 'cmpe281p2db.cmqx6tpknayx.us-east-2.rds.amazonaws.com';
MYSQL_USER = 'root';
MYSQL_DB = 'cook';
MYSQL_PASS = process.env.MYSQL_PASS || null;

/* APIs
 * - RecipeDb ctor - generates a RecipeDb handle instance
 * - disconnect - disconnect from MySQL
 * - insert functions - insert data directly to database
 */

function RecipeDb () {
   /* 
    * Creates connection to MySQL and returns handle.
    */
   assert.notEqual( MYSQL_PASS, null, 'MYSQL_PASS env variable not set' );
   var con = mysql.createConnection({
      host: MYSQL_HOST,
      user: MYSQL_USER,
      password : MYSQL_PASS,
      database : MYSQL_DB });
   con.connect();
   this.con = con;
}

RecipeDb.prototype.disconnect = function() {
   /*
    * Disconnect from MySQL
    */
   this.con.end();
}


RecipeDb.prototype.insertUser = function( username, callback ) {
   /*
    * Inserts a new user with username as a parameter,
    * triggers callback function once operation is complete
    */
   var insert = 'INSERT into User ( username ) values ( ? )'
   this.con.query( insert, [ username ],
      function( err, cur ){
         if ( err ) {
            callback( err );
         }
         console.log( 'User ' + username + ' inserted.' );
         callback( null );
      });
   this.con.commit();
}

RecipeDb.prototype.insertRecipe = function( ownerId, title, callback ) {
   /*
    * Inserts a new recipe with ownerId, title as parameters,
    * triggers callback function once operation is complete
    */
   var insert = 'INSERT into Recipe (ownerId,title) values ( ?, ? )';
   this.con.query( insert, [ ownerId, title ],
      function( err, cur ){
         if ( err ) {
            callback( err );
         }
         console.log( 'Recipe ' + title + ' inserted.' );
         callback( null );
      });
   this.con.commit();
}
module.exports = RecipeDb;
