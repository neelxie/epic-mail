document.getElementById('save').addEventListener('onclick', saveMsg);

function saveMsg(event) {
    event.preventDefault();

    token = localStorage.getItem('token');
    
    if (token === null) {
        alert('You must log in');
        window.location.replace('index.html');
    }

    let reciever = document.getElementById('reciever').value;
    let subject = document.getElementById('subject').value;
    let message = document.getElementById('message').value;

    let contact = parseInt(reciever);

    const send = {
        "receiver_id": contact,
        "subject": subject,
        "message": message,
    }

    fetch('https://my-epic-mail.herokuapp.com/api/v2/messages/save', {
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

            document.getElementById('myStatus').innerHTML = data.error;
            setTimeout(() => { 
                document.getElementById('myStatus').style.display = "block";
            }, 4000);
        }

        if (data.status === 201){

            document.getElementById('myStatus').style.display = "Account successfully created";
            setTimeout(() => { 
                document.getElementById('myStatus').style.display = "block";
            }, 4000);

            window.location.replace('user.html');
            alert("Message saved.");
        }
    })
    .catch((err) => console.log(err))
}
