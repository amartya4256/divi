function getAddDeviceContainer(){
    document.querySelector('#addDevice').style.display = "block";
}

function closeAddDeviceContainer(){
    document.querySelector("#message").innerHTML = "";
    document.querySelector("#addDeviceBtn").disabled = false;
    document.querySelector('#dname').value = "";
    document.querySelector('#ipname').value = "";
    document.querySelector('#addDevice').style.display = "none";
}

function addDevice(deviceName, deviceIp){

    fetch("http://127.0.0.1:5000/addDevice", {
        method : 'post',
        body : JSON.stringify({
            "name" : deviceName,
            "ip" : deviceIp
        })
    }).then((responseText) => responseText.json()).then((data) => {

        console.log(data);

        if(data.success == true){
            document.querySelector("#message").innerHTML = data.message;
            document.querySelector("#addDeviceBtn").disabled = true;
	    getDevices();
        }
        else{
            document.querySelector("#message").innerHTML = data.message;
        }

    })
}

function removeDevice(device){
    fetch("http://127.0.0.1:5000/removeDevice", {
        method : 'post',
        body : JSON.stringify({
            "name" : device
        })
    }).then((response)=> {
        getDevices();
    })
}
