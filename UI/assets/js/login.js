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
        cache: 'no-cache',
        headers: {
            'content-type': 'application/json'

        },
        body: JSON.stringify(user)
    })
    .then((res) => res.json())
    .then((data) => {
        if (data.status === 200){

            document.getElementById('myStatus').style.display = "none";

            localStorage.setItem('token', data.token);

            window.location.replace('user.html');
        }
        if (data.status === 403){

            document.getElementById('myStatus').style.display = "none";
            document.getElementById('myStatus').innerHTML = data.error;

            setTimeout(() => { 
                document.getElementById('myStatus').style.display = "block";
            }, 4000);

            window.location.replace('signup.html');
        }
        if (data.status === 400){

            document.getElementById('myStatus').style.display = "block";
            alert(data.error)
            document.getElementById('myStatus').innerHTML = data.error;
            setTimeout(() => { 
                document.getElementById('myStatus').style.display = "none";
            }, 4000);
        }
        
    })
    .catch((err) => console.log(err))
}
