document.getElementById('loginForm').addEventListener('submit', loginForm);

function loginForm(event) {
    event.preventDefault();


    let email = document.getElementById('email').value;
    let password = document.getElementById('password').value;

    const user = {
        "email": email,
        "password": password,
    }

    fetch('https://my-epic-mail.herokuapp.com/api/v2/auth/login', {
        method: 'POST',
        headers: {
            'content-type': 'application/json'
        },
        body: JSON.stringify(user)
    })
    .then((res) => res.json())
    .then((data) => {
        if (data.status != 200){

            document.getElementById('myStatus').style.display = "block";
            document.getElementById('myStatus').innerHTML = data.error;
            alert(data.error)
        }
        if (data.status === 200){

            document.getElementById('myStatus').style.display = "none";
            alert("Successfully logged in.");

            localStorage.setItem('epicMailToken', data.token);

            window.location.replace('user.html');
        }
    })
    .catch((err) => console.log(err))
}
