function inbox(){
    token = localStorage.getItem('token');
    
    if (token === null) {
        alert('You must log in');
        window.location.replace('index.html');
    }
    fetch('./api/v2/messages', {
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
            let everyThng = "";
            data.data.forEach((msg) => {
                everyThng +=
                    `<tr class="row">
                        <td class="senders">From User: ${msg.sender_email} </td>
                        <td><a href ="oneMsg.html?message_id=${msg.message_id}">${msg.subject}</a></td>
                        <td class="date"> ${msg.created_on} </td>
                        <td><button onclick="deleteMsg(${msg.message_id})">Delete</button></td>
                    </tr>`;
                });
            document.getElementById('everyThng').innerHTML = everyThng;
        }
    })
}
