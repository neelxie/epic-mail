function checkAdminEmail(){
// function checks for email value and redirects to appropriate email
    let response = document.getElementById("email").value;
    if (response == "admin@epic-mail.com"){
        location = "admin.html";
    }
    else{
        location = "user.html";
    }
    return false;
}
function resetPassword(){
    //confirmaton for reset password
    alert("Link has been sent to your email");
}