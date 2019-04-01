document.getElementById('composeForm').addEventListener('submit', composeForm);

function composeForm(event) {
    event.preventDefault();

    token = localStorage.getItem('epicMailToken');
    
    if (token === null) {
    alert('You must log in');
    window.location.replace('index.html');
    }

    let contact = document.getElementById('contact').value;
    let subject = document.getElementById('subject').value;
    let message = document.getElementById('message').value;

    const send = {
        "contact": contact,
        "subject": subject,
        "message": message,
    }

    fetch('https://my-epic-mail.herokuapp.com/api/v2/messages', {
        method: 'POST',
        headers: {
            'content-type': 'application/json'
        },
        body: JSON.stringify(send)
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
            alert("Message sent.");

            window.location.replace('user.html');
        }
    })
    .catch((err) => console.log(err))
}
