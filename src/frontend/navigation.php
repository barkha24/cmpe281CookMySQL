<?php
  $userId = $_GET['userId'];
  $token = $_GET['token'];
  $queryString = sprintf("?userId=%s&token=%s", $userId, $token); //+ (string)$userId + "&token=" + (string)$token;
?>
   <div class="navigation">
       <div id="navigation">
           <ul>
               <li class="active"><a href="home.php<?php echo $queryString; ?>">Home</a></li>
               <li><a href="add-recipe.php<?php echo $queryString; ?>">My Recipes</a></li>
               <li><a href="trending-recipes.php<?php echo $queryString; ?>">Trending</a>
               <li><a href="about.php<?php echo $queryString; ?>">About Us</a>
               <li><a href="contact-us.php<?php echo $queryString; ?>">Contact Us</a>
               </li>
           </ul>
       </div>
   </div>
<?php ?>
