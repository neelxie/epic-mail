document.getElementById('gropForm').addEventListener('submit', gruopForm);

function gruopForm(event) {
    event.preventDefault();

    token = localStorage.getItem('token');
    
    if (token === null) {
        window.location.replace('index.html');
    }

    let reciever = document.getElementById('group_id').value;
    let subject = document.getElementById('subject').value;
    let message = document.getElementById('message').value;

    var group_id = parseInt(reciever);

    const send = {
        "subject": subject,
        "message": message
    }
    const URL = 'https://my-epic-mail.herokuapp.com/api/v2/groups/'+group_id+'/messages'

    fetch(URL, {
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
            document.getElementById('myStatus').innerHTML = "Message successfully sent to Group";
            setTimeout(() => { 
                document.getElementById('myStatus').style.display = "block";
            }, 4000);

            window.location.replace('groups.html');
        }
    })
    .catch((err) => console.log(err))
}
