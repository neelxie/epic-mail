document.getElementById('epicRegister').addEventListener('submit', epicRegister);

function epicRegister(event) {
    event.preventDefault();

    let firstName = document.getElementById('firstName').value;
    let lastName = document.getElementById('lastName').value;
    let email = document.getElementById('email').value;
    let phoneNumber = document.getElementById('phoneNumber').value;
    let password = document.getElementById('password').value;

    const user = {
        "first_name": firstName,
        "last_name": lastName,
        "phone_number": phoneNumber,
        "email": email,
        "password": password,
    }

    fetch('https://my-epic-mail.herokuapp.com/api/v2/auth/signup', {
        method: 'POST',
        headers: {
            'content-type': 'application/json'
        },
        body: JSON.stringify(user)
    })
    .then((res) => res.json())
    .then((data) => {
        if (data.status != 201){

            document.getElementById('myStatus').style.display = "block";
            alert(data.error)
            document.getElementById('myStatus').innerHTML = data.error;
            setTimeout(() => { 
                document.getElementById('myStatus').style.display = "none";
            }, 4000);
        }
        if (data.status === 201){
            document.getElementById('myStatus').style.display = "none";
            alert("Account successfully created.");
            window.location.replace('index.html');
        }
    })
    .catch((err) => console.log(err))
}
