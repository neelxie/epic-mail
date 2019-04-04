function allGroups(){
    token = localStorage.getItem('token');
    
    if (token === null) {
        alert('You must log in');
        window.location.replace('index.html');
    }
    fetch('https://my-epic-mail.herokuapp.com/api/v2/groups', {
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
            let myGroups = "";
            data.data.forEach((group) => {
                myGroups +=
                    `<tr>
                     <td class="senders">Group ID: ${group.group_id} </td>
                     <td><a href ="oneGroup.html?group_id=${group.group_id}">${group.group_name}</a></td>
                     <td class="date"> ${group.created_on} </td>
                    </tr>`;
                });
            document.getElementById('myGroups').innerHTML = myGroups;
        }
    })
}
