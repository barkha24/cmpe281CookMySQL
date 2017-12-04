$(document).ready(function() {
  $('#loginform').submit(function(e) {
    e.preventDefault();
    $.ajax({
    type: 'POST',
    url: 'http://cmpe281p2b-2f1e7577f6424524.elb.us-east-2.amazonaws.com/authenticate',
    data:{
            username: $("#username").val(),
            password: $("#password").val()
        },
    success: function(resultdata){
      console.log(resultdata);
      //result =  JSON.parse(resultdata)
      $.ajax({
          type: 'GET',
          url: 'http://dock2.hyunwookshin.com:8044/about.php?userId=' + resultdata.response.userId +"&token=" +  resultdata.response.token,
          headers: {"x-access-token": resultdata.token},
          success: function(newData){
              console.log('success');
              //console.log(newData);
              window.location= 'about.php?userId=' + resultdata.response.userId +"&token=" +  resultdata.response.token;
         }
       });
  },
  error: function( xhr, exception ) {
     if (xhr.status === 401) {
        alert( 'Authentication error' );
     }
  },

  complete: function () {
        // Schedule the next request when the current one has been completed

        setTimeout(this.ajaxRequest, 4000);
    }
  
  });
 });
 $('#signup').submit(function(e) {
    e.preventDefault();
    $.ajax({
    type: 'POST',
    url: 'http://cmpe281p2b-2f1e7577f6424524.elb.us-east-2.amazonaws.com/signup',
    data:{
		       firstname:$("fname").val(),
			     lastnmae :$("lname").val(),
            username: $("#username").val(),
            mobile: $("#mobile").val(),
            password: $("#password").val()
        },
    success: function(data){
      // $.ajax({
      //     type: 'GET',
      //     url: 'http:google.com'//'http://cmpe281p2b-2f1e7577f6424524.elb.us-east-2.amazonaws.com',
      //     headers: {"x-access-token": resultdata.token},
      //     success: function(newData){
      //         console.log('Success and Please login ');
      //         //console.log(newData);
      window.refresh
      //   }
      // });
  },
  complete: function () {
        // Schedule the next request when the current one has been completed

        setTimeout(this.ajaxRequest, 4000);
    }
  
  });
 });
});
