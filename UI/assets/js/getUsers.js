function appUsers(){
    token = localStorage.getItem('token');
    
    if (token === null) {
        alert('You must log in');
        window.location.replace('index.html');
    }
    fetch('https://my-epic-mail.herokuapp.com/api/v2/auth/users', {
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
            let allUsers = "";
            data.data.forEach((user) => {
                allUsers +=
                    `<tr class="row">
                        <td class="senders">User ID: ${user.user_id} </td>
                        <td><a href ="oneUser.html?user_id=${user.user_id}">${user.first_name}</a></td>
                        <td>${user.last_name}</td>
                        <td class="date"> ${user.email} </td>
                    </tr>`;
                });
            document.getElementById('allUsers').innerHTML = allUsers;
        }
    })
}
