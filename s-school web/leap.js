// Store frame for motion functions
var previousFrame = null;
var paused = false;
var pauseOnGesture = false;

// Setup Leap loop with frame callback function
var controllerOptions = {enableGestures: true};

// to use HMD mode:
// controllerOptions.optimizeHMD = true;

Leap.loop(controllerOptions, function(frame) {
  if (paused) {
    return; // Skip this update
  }

  // Display Hand object data
  var handOutput = document.getElementById("handData");
  var handString = "";
  var forward = "", backward ="", breaker="", vel="", direction = "", total_data="";
  var one = document.getElementById("one");
  var two = document.getElementById("two");
  var three = document.getElementById("three");
  var left = document.getElementById("left");
  var right = document.getElementById("right");
  var speed = document.getElementById("speed");

  handString += "<div style='width:300px; float:left; padding:5px; border : 1px solid black;'>";
  
	
  if (frame.hands.length > 0) {
    for (var i = 0; i < frame.hands.length; i++) {
      var hand = frame.hands[i];	  
	 
		if(hand.type=="right"){
			
			var handx = hand.palmPosition[0];
			handString += hand.type;
			
			if (handx<=50){
				direction = "-3";
				left.style.opacity="1";
				right.style.opacity="0.2";
			}
			else if(handx<=70){
				direction = "-2";
				left.style.opacity="1";
				right.style.opacity="0.2";
			}
			else if(handx<=90){
				direction = "-1";
				left.style.opacity="1";
				right.style.opacity="0.2";
				
			}
			else if(handx<=110){
				direction ="00";
				left.style.opacity="1";
				right.style.opacity="1";
			}
			else if(handx<=125){
				direction ="+1";
				left.style.opacity="0.2";
				right.style.opacity="1";
			}
			else if(handx<=145){
				direction ="+2";
				left.style.opacity="0.2";
				right.style.opacity="1";
			}
			else if(handx<=300){
				direction = "+3";
				left.style.opacity="0.2";
				right.style.opacity="1";
			}	
			handString+=direction;
				
		}		
		else if(hand.type=="left"){
			handString += hand.type;
			var dist = hand.palmPosition[1];
			
			if(hand.grabStrength==0){
				breaker ="00";
				if(dist<=120)
					{
						forward="+1";
						backward ="00";
						one.style.opacity = "0.2";
						two.style.opacity="0.2";
						three.style.opacity = "1";
					}
				else{
					forward="00";
					backward="+1";
					one.style.opacity = "0.2";
					two.style.opacity="1";
					three.style.opacity = "0.2";
				}
			}
			else if(hand.grabStrength==1)
				{
					breaker="+1";
					forward ="00";
					backward="00";
					one.style.opacity = "1";
					two.style.opacity="0.2";
					three.style.opacity = "0.2";
				
				}
			
		total_data = forward+backward+direction+breaker;
			handString+=total_data;

		}
		
	  handString+="</div>";
	  
	}
  
  }
  else {
    handString += "No hands";
	one.style.opacity = "0.2";
	two.style.opacity="0.2";
	three.style.opacity = "0.2";
  }
	
  //handOutput.innerHTML = handString;


	
	//color change

})



function vectorToString(vector, digits) {
  if (typeof digits === "undefined") {
    digits = 1;
  }
	return vector[0];
}

function togglePause() {
  paused = !paused;

  if (paused) {
    document.getElementById("pause").innerText = "Resume";
  } else {
    document.getElementById("pause").innerText = "Pause";
  }
}

function pauseForGestures() {
  if (document.getElementById("pauseOnGesture").checked) {
    pauseOnGesture = true;
  } else {
    pauseOnGesture = false;
  }
}