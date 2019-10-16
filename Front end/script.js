autolisten();
var today = new Date();
var time = today.getHours() + ":" + today.getMinutes();



function senddata(){

	var today = new Date();
	var time = today.getHours() + ":" + today.getMinutes();
	var msg = new SpeechSynthesisUtterance();
  	var voices = window.speechSynthesis.getVoices();
  	msg.voice = voices[0];
  	msg.voiceURI = "native";
  	msg.volume = 2;
  	msg.rate = 1;
  	msg.pitch = 0.8;
  	msg.text = '';
  	msg.lang = 'en-US';
        var x = new XMLHttpRequest();
        x.onreadystatechange = function() {

        	if (this.readyState == 4 && this.status == 200) {
            		document.getElementById("scroller").innerHTML +=
             	`<div class="container">
  		<img src="divi_logo.png" alt="Avatar">
  		<p>` + this.responseText + `</p>
  		<span class="time-right">`+ time + `</span>
		</div>`;
    		scroller(document.getElementById("scroller"));

            	msg.text = this.responseText;
            	speechSynthesis.speak(msg);
       }}

        x.open("POST","http://127.0.0.1:5000/type");
        x.send(document.getElementsByClassName("inputbar")[0].value);
        console.log(document.getElementsByClassName("inputbar")[0].value);
    }


function speakdata(){

	var today = new Date();
	var time = today.getHours() + ":" + today.getMinutes();
	var msg = new SpeechSynthesisUtterance();
  	var voices = window.speechSynthesis.getVoices();
  	msg.voice = voices[0];
  	msg.voiceURI = "native";
  	msg.volume = 2;
  	msg.rate = 1;
  	msg.pitch = 0.8;
  	msg.text = '';
  	msg.lang = 'en-US';
        var x = new XMLHttpRequest();
        x.onreadystatechange = function() {
        
		if (this.readyState == 4 && this.status == 200) {
            		let obj = JSON.parse(this.responseText);


            		if (obj['request'] != undefined)  {
            			document.getElementById("scroller").innerHTML += `<div class='container darker'>
  				<img src='user.png' alt='Avatar' class='right'>
  				<p>` + obj['request'] +  `</p>
  				<span class='time-left'>` + time + `</span></div>`;
  			}

            		document.getElementById("scroller").innerHTML +=
             		`<div class="container">
  			<img src="divi_logo.png" alt="Avatar">
  			<p>` + obj['reply'] + `</p>
  			<span class="time-right">` + time + `</span>
			</div>`;


    			scroller(document.getElementById("scroller"));
            		msg.text = obj['reply'];
            		speechSynthesis.speak(msg);
       			}
     		}
        	x.open("POST","http://127.0.0.1:5000/speak");
        	x.send();
    	}
    

function enterlistener(query){
	
	if(event.key === 'Enter'){

        	document.getElementById("scroller").innerHTML += `<div class='container darker'>
  		<img src='user.png' alt='Avatar' class='right'>
  		<p>` + document.getElementsByClassName("inputbar")[0].value +  `</p>
  		<span class='time-left'>` + time +`</span></div>`;

  		scroller(document.getElementById("scroller"));
  		console.log(document.getElementById("scroller").value);



        	senddata();
    		document.getElementsByClassName("inputbar")[0].value = '';
    		}
    	}

function scroller(elem){

        elem.scrollTop = elem.scrollHeight;
    }






function autolisten() {

console.log("chalta hai");


var SpeechRecognition = window.webkitSpeechRecognition;

var recognition = new SpeechRecognition();
 console.log(recognition);
var Content = '';

recognition.continuous = true;

recognition.onresult = function(event) {

  var current = event.resultIndex;

  var transcript = event.results[current][0].transcript;

    Content = transcript;
    if(Content.includes("time to talk")){
	speakdata();
}
console.log("hi" + Content);

};

recognition.onerror = function() {
  if(event.error == 'no-speech') {
  }
}

recognition.start();
}