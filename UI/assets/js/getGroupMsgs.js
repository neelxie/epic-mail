document.getElementById('gropMsgForm').addEventListener('submit', gropMsgForm);

function gropMsgForm(event) {
    event.preventDefault();

    token = localStorage.getItem('token');
    
    if (token === null) {
        alert('You must log in');
        window.location.replace('index.html');
    }

    let reciever = document.getElementById('group_id').value;
    let subject = document.getElementById('subject').value;
    let message = document.getElementById('message').value;

    var group_id = parseInt(reciever);

    const URL = 'https://my-epic-mail.herokuapp.com/api/v2/groups/'+group_id+'/messages'

    fetch(URL, {
        headers: {
            'Authorization': `Bearer ${token}`
        }
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

            document.getElementById('myStatus').style.display = "none";

            window.location.replace('groups.html');
            alert("Message sent.");
        }
    })
    .catch((err) => console.log(err))
}
