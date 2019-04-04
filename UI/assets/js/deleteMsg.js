function deleteMsg(msg_id){
    token = localStorage.getItem('token');
    
    if (token === null) {
        alert('You must log in');
        window.location.replace('index.html');
    }
    fetch('https://my-epic-mail.herokuapp.com/api/v2/messages/'+msg_id, {
        method: 'DELETE',
        headers: {

            'Authorization': `Bearer ${token}`
        }
    })
    .then((res) => res.json())
    .then((data) => {
        if (data.status === 400){

            document.getElementById('blank').innerHTML = "No email by that ID.";
            setTimeout(() => { 
                document.getElementById('blank').style.display = "block";
            }, 4000);
            window.location.replace('user.html');
        }
        if (data.status === 200){
            alert("Message successfully deleted.")
            document.getElementById('blank').innerHTML = "Message successfully deleted.";
            setTimeout(() => { 
                document.getElementById('blank').style.display = "block";
            }, 4000);
            window.location.replace('user.html');
        }
    })
    .catch((err) => console.log(err))
}