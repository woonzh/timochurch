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
      frame=document.getElementById('myframe');
      frame.src = url;
      document.getElementById("loading").style.display="none";
    },
    error: function(jqxhr, status, exception) {
        alert('Exception:', exception);
        document.getElementById("loading").style.display="none";
    }
  });
}
