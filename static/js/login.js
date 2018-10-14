function login(){
  var email=document.getElementById('email').value;
  var password=document.getElementById('password').value;

  var url="http://127.0.0.1:5000/login";
  $.ajax({
    url: url,
    type: 'POST',
    data:{
      email: email,
      password: password
    },
    success: function (data) {
      var resp=JSON.parse(data);
      var result=resp['result'];
      var msg=resp['msg'];
      alert(msg);
    },
    error: function(jqxhr, status, exception) {
        alert('Exception:', exception);
    }
  });
}
