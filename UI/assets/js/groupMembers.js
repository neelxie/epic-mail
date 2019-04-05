window.onload = function(){
    let my_url = location.href
    let url = new URL(my_url)
    let group_id = url.searchParams.get('group_id')
    groupMembas(group_id);
}
function groupMembas(group_id){
    token = localStorage.getItem('token');
    
    if (token === null) {
        alert('You must log in');
        window.location.replace('index.html');
    }
    fetch('http://my-epic-mail.herokuapp.com/api/v2/groups/'+group_id+'/users', {
        headers: {
            'Authorization': `Bearer ${token}`
        }
    })
    .then((res) => res.json())
    .then((data) => {
        if (data.status === 404){
            document.getElementById('blank').style.display = "block";
            document.getElementById('blank').innerHTML = "You have no group members yet";
        }
        if (data.status === 401){
            document.getElementById('blank').style.display = "block";
            document.getElementById('blank').innerHTML = data.error;
            window.location.replace('index.html');
        }
        if (data.status === 200){
            console.log(data.data)
            let myGmembas = "";
            data.data.forEach((member) => {
                myGmembas +=
                    `<tr>
                        <td class="senders">Group ID: ${member.group_id} </td>
                        <td>Group Member ID: ${member.member_id}</td>
                        <td>Member Email: ${member.receiver_email}</td>
                        <td>Added On: ${member.added_on}</td>
                        <td><a href ="deleteGroupUser.html?group_id=${member.group_id}">Delete</a></td>
                    </tr>`;
                });
            document.getElementById('myGmembas').innerHTML = myGmembas;
        }
    })
}
