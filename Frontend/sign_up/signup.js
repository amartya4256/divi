function signup(){
    document.querySelector("#message").innerHTML = `Verifying...`;
    var name = document.querySelector("#Name").value;
    var username = document.querySelector('#Username').value;
    var email = document.querySelector('#Email').value;
    var password = document.querySelector('#Password').value;
    var password2 = document.querySelector('#Password2').value;
    var data = {
       name : name,
       username : username,
       email : email,
       password : password,
       password2 : password2
    };

    console.log(data);

    if(password != password2) {
         alert ("\nPassword did not match: Please try again.")
                    return false;
    }
    else{
        fetch("http://127.0.0.1:5000/signup", {
            method : 'POST',
            body : JSON.stringify(data)
        }).then((response) => response.json())
        .then((response) => {
            document.querySelector("#message").innerHTML = response.message;
        });
    }
}