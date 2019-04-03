function allGroups(){
    token = localStorage.getItem('token');
    
    if (token === null) {
        alert('You must log in');
        window.location.replace('index.html');
    }
    fetch('https://my-epic-mail.herokuapp.com/api/v2/messages/sent', {
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
            console.log(data.data)
            let allSent = "";
            data.data.forEach((msg) => {
                allSent +=
                    `<tr>
                     <td class="senders">To User: ${msg.receiver_id} </td>
                     <td><a href ="oneMsg.html?entry_id=${msg.message_id}">${msg.subject}</a></td>
                     <td class="date"> ${msg.created_on} </td>
                    </tr>`;
                });
            document.getElementById('allSent').innerHTML = allSent;
        }
    })
}
