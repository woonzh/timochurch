var $TABLE = $('#table');
var $BTN = $('#export-btn');
var $EXPORT = $('#export');

function onload(){
  url="https://chenguobin.herokuapp.com/geturl";
  $.ajax({
    url: url,
    type: 'GET',
    success: function (data) {
      var jidraw=JSON.parse(data);
      var url=jidraw['result'];
      urlfield=document.getElementById('url');
      urlfield.innerHTML=url;
      document.getElementById("loading").style.display="none";
    },
    error: function(jqxhr, status, exception) {
        alert('Exception:', exception);
        document.getElementById("loading").style.display="none";
    }
  });
}

function seturl(){
  newurl=document.getElementById("url").innerHTML;
  $.ajax({
    url: url,
    type: 'POST',
    data:{
      "url": newurl;
    },
    success: function (data) {
      var jidraw=JSON.parse(data);
      var result=jidraw['result'];
      alert(result);
      document.getElementById("loading").style.display="none";
    },
    error: function(jqxhr, status, exception) {
        alert('Exception:', exception);
        document.getElementById("loading").style.display="none";
    }
  });
}
