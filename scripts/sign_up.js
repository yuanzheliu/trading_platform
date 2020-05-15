function validateForm() {
    checkPassword();
}


function checkPassword(){
    let p1 = document.forms["signup"]["pwd"].value;
    let p2 = document.forms["signup"]["cpwd"].value;
    if (p1 !== p2){ 
        alert("Passwords are not the same!")
    }
    if (p1.length < 8){
        alert("Passwords must be longer than 8 characters!")
    }
}

