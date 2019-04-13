function unRead(){
    token = localStorage.getItem('token');
    
    if (token === null) {
        alert('You must log in');
        window.location.replace('index.html');
    }
    fetch('./api/v2/messages/unread', {
        headers: {
            'Authorization': `Bearer ${token}`
        }
    })
    .then((res) => res.json())
    .then((data) => {
        if (data.status === 400){
            document.getElementById('blank').style.display = "block";
            document.getElementById('blank').innerHTML = "You have no unread messages";
        }
        if (data.status === 401){
            document.getElementById('myStatus').innerHTML = data.error;
            setTimeout(() => { 
                document.getElementById('myStatus').style.display = "block";
            }, 4000);
            window.location.replace('./index.html');
        }
        if (data.status === 200){
            console.log(data)
            let allUnread = "";
            data.data.forEach((msg) => {
                allUnread +=
                    `<tr>
                     <td class="senders">To User: ${msg.receiver_email} </td>
                     <td><a href ="oneMsg.html?message_id=${msg.message_id}">${msg.subject}</a></td>
                     <td class="date"> ${msg.created_on} </td>
                     <td><button onclick="deleteMsg(${msg.message_id})">Delete</button></td>
                    </tr>`;
                });
            document.getElementById('unRead').innerHTML = allUnread;
        }
    })
}
unRead()