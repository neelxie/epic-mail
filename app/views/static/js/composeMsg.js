document.getElementById('composeForm').addEventListener('submit', composeForm);

function composeForm(event) {
    event.preventDefault();

    token = localStorage.getItem('token');
    
    if (token === null) {
        alert('You must log in');
        window.location.replace('index.html');
    }

    let contact = document.getElementById('receiver').value;
    let subject = document.getElementById('subject').value;
    let message = document.getElementById('message').value;


    const send = {
        "receiver_email": contact,
        "subject": subject,
        "message": message,
    }

    fetch('./api/v2/messages', {
        method: 'POST',
        cache: 'no-cache',
        headers: {
            'content-type': 'application/json',
            'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify(send)
    })
    .then((res) => res.json())
    .then((data) => {
        if (data.status != 201){

            document.getElementById('myStatus').style.display = "block";
            document.getElementById('myStatus').innerHTML = data.error;
            setTimeout(() => { 
                document.getElementById('myStatus').style.display = "none";
            }, 4000);
        }

        if (data.status === 201){

            document.getElementById('myStatus').innerHTML = "Message sent successfully";
            setTimeout(() => { 
                document.getElementById('myStatus').style.display = "block";
            }, 4000);

            window.location.replace('sent.html');
        }
    })
    .catch((err) => console.log(err))
}
