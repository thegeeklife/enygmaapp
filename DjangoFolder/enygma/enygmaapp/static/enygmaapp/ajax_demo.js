$(document).ready(function(){
  // Should execute when the button is clicked
  $("#ajax-btn").click(function(){
      // reading the Json file based on the code in the Ajax tutorial
      var xhr = new XMLHttpRequest();
      xhr.open('GET', '/static/enygmaapp/mydata.json', true);
      xhr.send();
      xhr.onload = function(){
      	if (xhr.status == 200){
      		console.log(xhr.responseText);
      		document.getElementById("ajax-test").innerHTML = this.responseText;
      	}else if(this.status == 404){
      		document.getElementById("ajax-test").innerHTML = this.statusText;
      	}
      }
  	})

});

// Something I tried but didn't work
// $(document).ready(function(){
//   $("#ajax-btn").click(function(){
//     $.ajax({
//     	method: "GET", // default
//     	url: "/static/enygmaapp/mydata.json",
//       dataType: 'json',
//     }).done(function( data,status ) {
//     	console.log("data: ",data);
//     	console.log("status: ",status);
//       $('span').append(data);
//     });
//   });
// });
