window.onload = function(){
    let my_url = location.href
    let url = new URL(my_url)
    let message_id = url.searchParams.get('message_id')
    getOneMessage(message_id);
}

function getOneMessage(msg_id){
    token = localStorage.getItem('token');
    
    if (token === null) {
        alert('You must log in');
        window.location.replace('index.html');
    }
    fetch('https://my-epic-mail.herokuapp.com/api/v2/messages/'+msg_id, {
        headers: {
            'Authorization': `Bearer ${token}`
        }
    })
    .then((res) => res.json())
    .then((data) => {
        if (data.status === 400){
            document.getElementById('blank').style.display = "block";
            document.getElementById('blank').innerHTML = data.error;
        }
        if (data.status === 401){
            document.getElementById('blank').style.display = "block";
            document.getElementById('blank').innerHTML = data.error;
            window.location.replace('index.html');
        }
        if (data.status === 200){
            console.log(data['data'])
            data.data.forEach((msg) => {
                document.getElementById("message_id").innerHTML=`${msg.message_id}`;
                document.getElementById("sender_id").innerHTML=`${msg.sender_id}`;
                document.getElementById("receiver_id").innerHTML=`${msg.receiver_id}`;
                document.getElementById("subject").innerHTML=`${msg.subject}`;
                document.getElementById("created_on").innerHTML=`${msg.created_on}`;
                document.getElementById("message").innerHTML=`${msg.message}`;
            })    
        }
    });
    
}