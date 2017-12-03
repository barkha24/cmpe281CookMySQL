<?php ?>
<!DOCTYPE html>
<html lang="en">


<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="">
    <meta name="keywords" content="">
    <title> About Us  </title>
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
</head>

<body>
      <!-- top-bar -->
    <div class="top-bar">
        <div class="container">
            <div class="row">
                <div class="col-lg-3 col-md-4 col-sm-5 hidden-xs">
                    <div class="support-bar">
                        <h1>Help To Cook-Chef Polly</h1>
                        
                    </div>
                </div>
                <div class="col-lg-6 col-md-4 col-sm-2 col-xs-12">
                    <!--logo-->
                    <!-- <div class="logo"><a href="index.html"><img src="images/logo.png" alt=""></a></div> -->
                </div>
                <div class="col-lg-3 col-md-4 col-sm-5 hidden-xs">
                    <div class="support-bar">
                        
                    </div>
                </div>
            </div>
        </div>
    </div>
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
    <!-- /. header-section-->
    <!-- page-header -->
    <!--
    <div class="page-header">
        <div class="container">
            <div class="row">
                <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
                    <div class="page-section">
                        <h1 class="page-title">About</h1>
                    </div>
                </div>
            </div>
        </div>
        
    </div>
    -->
    <!-- /.page-header-->
    <!-- about -->
    <div class="content">
        <div class="container">
            <div class="row">
                <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
                    <div class="section-title">
                        <h2>Help to Cook-Chef Polly</h2>
                        <p>The application allows user to save recipe to the cloud, and play the recipe instructions to the user when the user is cooking. This allows the user to focus on cooking, and avoid the need to browse through the phone or website to read the instructions</p>
                        
                        <p>
For reciting the recipe, we plan to use Amazon Polly which can read out in natural sounding void the recipe information to the user. For storing the recipe data to the server, we plan to use Amazon S3 as storage, and CloudFront to fetch recipe data. Whenever a user initiates a new task Lambda Function will be responsible for initializing the process to generate new MP3. We also plan to use Amazon Lex for listening to users instructions to slow down, skip or pause. For mapping recipe to the user information and keeping metadata of the recipes, we plan to use Amazon RDS. Other Amazon components such as Kinesis, EC2, SNS and ELB are used to build and deploy the application that is scalable and highly available.
</p>
<centre>
                        <p><h3>Team members</h3></p>
                        <p>Mojdeh Keykhanzadeh</p>
                        <p>Vidhi Sharma </p>
                        <p>Hyunwook Shin</p>
                        <p>Barkha Choithani </p>
                        </centre>
                       
    <div class="space-medium bg-light">
        <div class="container">
            <div class="row">
                <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
                    <div class="section-title">
                        <h2></h2>
                    </div>
                </div>
            </div>
           
        </div>
    </div>
    <!-- /.about -->
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
