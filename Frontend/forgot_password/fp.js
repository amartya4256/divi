function forgotPassword(){
    var email = document.querySelector("#email").value;
    var data = {
        email : email
    };
    fetch("http://127.0.0.1:5000/forgot-password", {
        method : 'POST',
        body : JSON.stringify(data)
    }).then((response) => response.json())
    .then((response) => {
        document.querySelector("#message").innerHTML = response.message;
    });
}