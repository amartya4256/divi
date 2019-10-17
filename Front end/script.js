

get_saved_state();

var today = new Date();
var time = today.getHours() + ":" + (today.getMinutes() < 10 ? '0' : '' ) + today.getMinutes();


/* Open when someone clicks on the span element */
function openNav() {
    document.getElementById("myNav").style.height = "100%";
    get_saved_state();
}

/* Close when someone clicks on the "x" symbol inside the overlay */
function closeNav() {
    document.getElementById("myNav").style.height = "0%";
}



function senddata(){

	var today = new Date();
	var time = today.getHours() + ":" + (today.getMinutes() < 10 ? '0' : '') + today.getMinutes();
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
	var time = today.getHours() + ":" + (today.getMinutes() < 10 ? '0' : '') + today.getMinutes();
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

    /*var today = new Date();
        var time = today.getHours() + ":" + (today.getMinutes() < 10 ? '0' : '' ) + today.getMinutes();*/
	
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






//creatingbuttonactions
function doalert(changeelem){

    if(changeelem.checked){
        autolisten(0);
        var x = new XMLHttpRequest();
        x.onreadystatechange = function() {};
        x.open("POST", "http://127.0.0.1:5000/autolisten/1");
        x.send();
    }
    else{
        autolisten(1);
        var x = new XMLHttpRequest();
        x.onreadystatechange = function() {};
        x.open("POST", "http://127.0.0.1:5000/autolisten/0");
        x.send();
    }
}

function autolisten(checker) {

    var today = new Date();
    var time = today.getHours() + ":" + (today.getMinutes() < 10 ? '0' : '' ) + today.getMinutes();
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
	        console.log("hi" + Content);
        }
    };

    recognition.onerror = function() {
        if(event.error == 'no-speech') {
        }
    }
    recognition.start();
    console.log("shuru");
    if(checker == 1){
        console.log("band");
        recognition.stop();
    }
}


function get_saved_state(){
    var x = new XMLHttpRequest();
    x.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            if(this.responseText=="1"){
            console.log(document.getElementsByClassName("state")[0]);
            autolisten(0);
            console.log("activated");
            try{
            document.getElementById("state").checked = true;
            console.log(document.getElementById("state").checked);
            }
            catch {}
            }
        }
    }
    x.open("GET","http://127.0.0.1:5000/autolisten/getdata");
    x.send();
}