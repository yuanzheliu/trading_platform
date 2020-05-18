function validateForm() {
    if (checkPassword()){
        send_form();
    }
}


function checkPassword(){
    let p1 = document.forms["signup"]["pwd"].value;
    let p2 = document.forms["signup"]["cpwd"].value;
    if (p1 !== p2){ 
        alert("Passwords are not the same!");
        return false;
    }
    if (p1.length < 8){
        alert("Passwords must be longer than 8 characters!");
        return false;
    }
    return true;
}

function send_form(){
    let data = {
                username: document.forms["signup"]["username"].value,
                password: document.forms["signup"]["pwd"].value,
                email:document.forms["signup"]["email"].value,
                // phone:document.forms["signup"]["phone"].value
                }
    let dataToSend = JSON.stringify(data);
    alert("sending");
    $.ajax({
        type: 'POST',
        url: 'http://127.0.0.1:8888/test/',
        data: dataToSend,
        dataType: 'JSON',
        success: function(response){
            var res = eval(response);
            alert(res.name);
            //console.log(res);
            //document.getElementById('response').setAttribute('value',res);
        },
        error: function() {
            alert("Sign up Failed!");
        }
    });
}

