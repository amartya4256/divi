//var check = new XMLHttpRequest();
//check.onreadystatechange = function() {
//    if (this.readyState == 4 && this.status == 200){
//        if (this.responseText != "Yes") {
//            window.location = "login.html";
//        }
//    }
//};
//check.open("GET", "http://127.0.0.1:5000/logincheck");
//check.send();
//console.log("HI");

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


function senddata() {

	var today = new Date();
	var time = today.getHours() + ":" + (today.getMinutes() < 10 ? '0' : '') + today.getMinutes();
	var msg = new SpeechSynthesisUtterance();
  	var voices = window.speechSynthesis.getVoices();
  	msg.voice = voices[2];
  	msg.voiceURI = "native";
  	msg.volume = 2;
  	msg.rate = 1;
  	msg.pitch = 1.0;
  	msg.text = '';
  	msg.lang = 'en-US';
        var x = new XMLHttpRequest();
        x.onreadystatechange = function() {

        	if (this.readyState == 4 && this.status == 200) {

                var check = {"nothing":"nothing"};
        	    try{var check = JSON.parse(this.responseText);}
        	    catch(err) {}
        	    finally{
        	    if (check['parsable'] != undefined)
        	        {

        	        var add_text = "&nbsp;";
        	        for (var key in check) {
                        if (key!='parsable'){

        	            add_text += `<button class = 'appbutton' onclick = "app_executer('` + check[key] + `', '` + key + `')">` + key + `</button> &nbsp;`;
        	         }
        	         }

        	         console.log(add_text);
                        document.getElementById("scroller").innerHTML +=
             	    `<div class="container">
  		            <img src="divi_logo.png" alt="Avatar">` + add_text + `<span class="time-right">`+ time + `</span>
		            </div>`;





        	        msg.text = "Which one do you want?";
            	    speechSynthesis.speak(msg);
        	        }
        	 else {
            		document.getElementById("scroller").innerHTML +=
             	`<div class="container">
  		<img src="divi_logo.png" alt="Avatar">
  		<p>` + this.responseText + `</p>
  		<span class="time-right">`+ time + `</span>
		</div>`;

		msg.text = this.responseText;
        speechSynthesis.speak(msg);
		    }

		scroller(document.getElementById("scroller"));
		    }
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
  	msg.voice = voices[2];
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
            		console.log(obj);


            		if (obj['request'] != undefined)  {
            			document.getElementById("scroller").innerHTML += `<div class='container darker'>
  				<img src='user.png' alt='Avatar' class='right'>
  				<p>` + obj['request'] +  `</p>
  				<span class='time-left'>` + time + `</span></div>`;
  			}
                var check = {"nothing":"nothing"};
  			    try{var check = obj['reply'];}
  			    catch(err) {}
                finally{
        	    if (check['parsable'] != undefined)
        	        {

        	        var add_text = "&nbsp;";
        	        for (var key in check) {
                        if (key!='parsable'){

        	            add_text += `<button class = 'appbutton' onclick = "app_executer('` + check[key] + `', '` + key + `')">` + key + `</button> &nbsp;`;
        	         }
        	         }

        	         console.log(add_text);
                        document.getElementById("scroller").innerHTML +=
             	    `<div class="container">
  		            <img src="divi_logo.png" alt="Avatar">` + add_text + `<span class="time-right">`+ time + `</span>
		            </div>`;





        	        msg.text = "Which one do you want?";
            	    speechSynthesis.speak(msg);
        	        }
        	        else {
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
            		    scroller(document.getElementById("scroller"));
        	        }

       			}
     		}
        	x.open("POST","http://127.0.0.1:5000/speak");
        	x.send();
    	}
    

function enterlistener(query){

    var today = new Date();
    var time = today.getHours() + ":" + (today.getMinutes() < 10 ? '0' : '' ) + today.getMinutes();
	
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
            document.getElementById("scroller").innerHTML +=
             		`<div class="container">
  			<img src="divi_logo.png" alt="Avatar">
  			<p>Yeah! I am listening...</p>
  			<span class="time-right">` + time + `</span>
			</div>`;
			scroller(document.getElementById("scroller"));
			//var audio = new Audio('audio_file.mp3');
            //audio.play();
	        speakdata();
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


function navigator() {
    console.log("nav")
    if(document.getElementById("myNav").style.height == "100%") {
        closeNav();
    }
    else {
        openNav();
    }
}

function minimize(response) {

}

function logout(){
console.log("logout")
    var x = new XMLHttpRequest();
    x.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            console.log("ho gaya");
            window.location = "login.html";
            }
    };
    x.open("GET","http://127.0.0.1:5000/logout");
    x.send();
}

function app_executer(path, key){
    console.log(path, key);
    var today = new Date();
	var time = today.getHours() + ":" + (today.getMinutes() < 10 ? '0' : '') + today.getMinutes();
    var msg = new SpeechSynthesisUtterance();
  	var voices = window.speechSynthesis.getVoices();
  	msg.voice = voices[2];
  	msg.voiceURI = "native";
  	msg.volume = 2;
  	msg.rate = 1;
  	msg.pitch = 1.0;
  	msg.text = '';
  	msg.lang = 'en-US';

    document.getElementById("scroller").innerHTML += `<div class='container darker'>
  				<img src='user.png' alt='Avatar' class='right'>
  				<p>` + key +  `</p>
  				<span class='time-left'>` + time + `</span></div>`;
  	scroller(document.getElementById("scroller"));

    var x = new XMLHttpRequest();
    x.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            if (this.responseText=="Success"){
            document.getElementById("scroller").innerHTML +=
             	`<div class="container">
  		<img src="divi_logo.png" alt="Avatar">
  		<p>` + "Starting " + key + `</p>
  		<span class="time-right">`+ time + `</span>
		</div>`;
        var say = "Starting " + key;
		msg.text = say;
        speechSynthesis.speak(msg);

        scroller(document.getElementById("scroller"));

            }
            else{
            document.getElementById("scroller").innerHTML +=
             	`<div class="container">
  		<img src="divi_logo.png" alt="Avatar">
  		<p>` + "Failed to start" + key + `</p>
  		<span class="time-right">`+ time + `</span>
		</div>`;
        var say = "Failed to start" + key;
		msg.text = say;
        speechSynthesis.speak(msg);

        scroller(document.getElementById("scroller"));
            }
            }
    };
    x.open("POST", "http://127.0.0.1:5000/app_executer");
    x.send(JSON.stringify({'path' : path}));
}
