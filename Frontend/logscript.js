// Get the modal



var modal = document.getElementById('id01');
document.getElementById('id01').style.display='block';
//// When the user clicks anywhere outside of the modal, close it
//window.onclick = function(event) {
//    if (event.target == modal) {
//        modal.style.display = "none";
//var check = new XMLHttpRequest();
//check.onreadystatechange = function() {
//    if (this.readyState == 4 && this.status == 200){
//        if (this.responseText == "Yes") {
//            window.location = "index.html";
//        }
//    }
//};
//check.open("GET", "http://127.0.0.1:5000/logincheck");
//check.send();
//console.log("HI");


function submit_data() {

    var name = document.getElementById("name").value;
    var pwd = document.getElementById("pwd").value;
    console.log(name, pwd)
    var x = new XMLHttpRequest();
    x.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200){
                if (this.responseText == "Success") {
                    window.location = "index.html";
                }
                else {
                    document.getElementById("response").innerText = this.responseText;
                }
            }
        };
    x.open("POST","http://127.0.0.1:5000/login");
    var y = {"username" : name, "password" : pwd};
    var z = JSON.stringify(y);
    x.send(z);
}

function entersubmit() {
    if(event.key === 'Enter') {
        submit_data();
    }
}