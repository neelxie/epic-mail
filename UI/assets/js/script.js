function checkAdminEmail(){

    let response = document.getElementById("email").value;
    if (response == "admin@epic-mail.com"){
        location = "admin.html";
    }
    else{
        location = "user.html";
    }
    return false;
}