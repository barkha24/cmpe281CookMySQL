<?php
  $userId = $_GET['userId'];
  $token = $_GET['token'];
?>
<!DOCTYPE html>
<html lang="en">


<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="">
    <meta name="keywords" content="">
    <title> Contact Us  </title>
    <!-- Bootstrap -->
    <link href="css/bootstrap.min.css" rel="stylesheet">
    <!-- Style CSS -->
    <link href="css/style.css" rel="stylesheet">
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css?family=Lato:100,100i,300,300i,400,400i,700,700i,900,900i%7cZilla+Slab:300,300i,400,400i,500,500i,600,600i,700,700i" rel="stylesheet">
    <!-- FontAwesome CSS -->
    <link rel="stylesheet" type="text/css" href="css/fontello.css">
    <link href="css/font-awesome.min.css" rel="stylesheet">
    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
    <script type="text/javascript" src="userinfo.js"></script>
    <script type="text/javascript" src="recipes.js"></script>
    <script type="text/javascript" src="delete.js"></script>
    <script type="text/javascript" src="upload.js"></script>
    <link href="css/recipe.css" rel="stylesheet">
</head>

<body onload="
       userInfo( '<?php echo $userId ?>', '<?php echo $token ?>', getRecipes );"
>
      <!-- top-bar -->
    <?php include "banner.php";?>
    <!-- /.top-bar -->
    <!-- header-section-->
    <div class="header-wrapper">
        <div class="container">
            <div class="row">
                <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
                    <!-- navigations-->
                    <?php include "navigation.php"; ?>
                    <!-- /.navigations-->
                </div>
            </div>
        </div>
    </div>
    </div>
    <!-- /. header-section-->
    <!-- contact us -->
    <div class="content">
        <div class="container">
            <div class="row">
                <div class="col-lg-8 col-lg-8 col-sm-7 col-xs-12 mb60">
                    <div class="book-form">
                        <div class="row">
                            <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12 mb30">
                                <h2>Want To Get In Touch With Us?</h2>
                                <p>Please complete the fields below and we'll get back to you as soon as possible.</p>
                            </div>
                            
                        </div>
                    </div>
                </div>
                
            </div>
            <div class="row">
                <!-- about-us -->
                <div class="col-lg-offset-1 col-lg-10 col-md-offset-1 col-md-10 col-sm-12 col-xs-12 ">
                    <div class="section-title">
                        <h2 class="text-primary">Thank You For Visiting Website.</h2>
                        <p class="lead">We value your comments and suggestions. The information you provide will be used only to help us better serve you and will not be sold or shared for any other purpose.</p>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col-lg-3 col-md-3 col-sm-6 col-xs-12">
                    <div class="contact-block">
                        <div class="contact-info-icon">
                            <i class="icon-placeholder"></i>
                        </div>
                        <div class="contact-info-text">
                            <h5>Address</h5>
                            <p>San Jose State University, USA</p>
                        </div>
                    </div>
                </div>
                <div class="col-lg-3 col-md-3 col-sm-6 col-xs-12">
                    <div class="contact-block">
                        <div class="contact-info-icon">
                            <i class="icon-telephone"></i>
                        </div>
                        <div class="contact-info-text">
                            <h5>Phone</h5>
                            <p>+281-281-2811 / 20
                                <br> +1281-281-2815 / 20</p>
                        </div>
                    </div>
                </div>
                <div class="col-lg-3 col-md-3 col-sm-6 col-xs-12">
                    <div class="contact-block">
                        <div class="contact-info-icon">
                            <i class="icon-letter"></i>
                        </div>
                        <div class="contact-info-text">
                            <h5>Email</h5>
                            <p>info@
                                <br>info@group5.cmpe281.com</p>
                        </div>
                    </div>
                </div>
                
            </div>
        </div>
    </div>
    
    <!-- /.contact us -->
    <div class="footer">
        <div class="container">
            <div class="row">
                <!-- about-us -->
                <div class="col-lg-4 col-md-4 col-sm-6 col-xs-12">
                    <div class="footer-widget">
                        <div class="ft-logo"><img src="./images/ft-logo.png" alt=""></div>
                    </div>
                </div>
                <!-- /.about us -->
                <!-- footer-hosting-services-links -->
                <div class=" col-lg-2 col-md-2 col-sm-6 col-xs-12">
                    
                </div>
                <!-- /.footer-useful links -->
                <!-- footer-useful links -->
                <div class=" col-lg-4 col-md-4 col-sm-6 col-xs-12">
                    <div class="footer-widget">
                        <h3 class="footer-title">Contact Info </h3>
                        <div class="contact-info">
                            <span class="contact-icon"><i class="icon-placeholder"></i></span>
                            <span class="contact-text">San Jose State University, USA</span>
                        </div>
                        <div class="contact-info">
                            <span class="contact-icon"><i class="icon-telephone"></i></span>
                            <span class="contact-text">+281-281-2811</span>
                        </div>
                        <div class="contact-info">
                            <span class="contact-icon"><i class="icon-letter"></i></span>
                            <span class="contact-text">info@group5.cmpe281.com</span>
                        </div>
                        <div class="ft-social">
                            <span><a href="https://www.facebook.com/" class="btn-social btn-facebook" ><i class="fa fa-facebook"></i></a></span>
                            <span><a href="https://twitter.com/" class="btn-social btn-twitter"><i class="fa fa-twitter"></i></a></span>
                            <span><a href="https://plus.google.com/" class="btn-social btn-googleplus"><i class="fa fa-google-plus"></i></a></span>
                            <span><a href="https://www.pinterest.com/" class=" btn-social btn-pinterest"><i class="fa fa-pinterest-p"></i></a></span>
                            <span><a href="https://www.instagram.com/accounts/login/" class=" btn-social btn-instagram"><i class="fa fa-instagram"></i></a></span>
                        </div>
                    </div>
                </div>
                <!-- /.footer-useful links -->
            </div>
        </div>
        <!-- tiny-footer -->
        <div class="container">
            <div class="row">
                <div class="tiny-footer">
                    <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
                        <p>Copyright © All Rights Reserved 2017 
                            <a href="https://easetemplate.com/" target="_blank" class="copyrightlink">Group5_CMPE-281</a></p>
                    </div>
                </div>
            </div>
            <!-- /. tiny-footer -->
        </div>
    </div>
    <!-- /.footer -->
    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="js/jquery.min.js" type="text/javascript"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src="js/bootstrap.min.js" type="text/javascript"></script>
    <script src="js/menumaker.js" type="text/javascript"></script>
    <script type="text/javascript" src="js/jquery.sticky.js"></script>
    <script type="text/javascript" src="js/sticky-header.js"></script>
</body>

</html>
<? ?>
