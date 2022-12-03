
// Code to implement like and dislike
var lcount = 21,
	maxlikecount = lcount+1,
	dcount = 3,
	mindislikecount = dcount-1 

document.getElementById("l-counter").innerHTML = lcount; 
var likebutton = document.getElementById('like-button');

likebutton.addEventListener('click', function(){ 
	//limit for maximum number of likes 
	if(lcount < maxlikecount){ 
		lcount += 1;
		document.getElementById("l-counter").innerHTML= lcount;
		//change the color of the icon
		$('#like-button').addClass("likeddisliked");
	}
	
})

//repeat for thumbs down
document.getElementById("d-counter").innerHTML = dcount;

var dislikebutton = document.getElementById('dislike-button');
dislikebutton.addEventListener('click', function(){
	//limit for max dislikes
	if((dcount > mindislikecount) && (dcount > 0)){ //negative likes not permitted
		dcount -= 1;
	document.getElementById("d-counter").innerHTML= dcount;
	$('#dislike-button').addClass("likeddisliked");
	}
	
	
});

// Creating a comment
function createcomment(userText) {
	//extract comment from user
	var catchComment = userText.parentElement,
		userComment = catchComment.getElementsByTagName("input"),
		//create p tag in parent element and add the text to it
		elementComment = document.createElement("p"),
		commentText = document.createTextNode('guestuser100: '+userComment[0].value);

	//add the comments to the bottom
	elementComment.appendChild(commentText);
	catchComment.appendChild(elementComment);

}

// Submitting solution will not work.
document.getElementById('submit-button').addEventListener('click', function(){
	alert("Sorry, this does not work yet. Please try commenting!")
})
